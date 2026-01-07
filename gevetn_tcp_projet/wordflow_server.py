"""
    tcp async server
    1. 可以查询翻译
    2. 需要登陆认证
    3. 需要保存查询信息， name , 查询的单词 , 查询的时间
"""
import gevent
from gevent import monkey
monkey.patch_all()

import threading
import json
import bcrypt
from socket import *
from python_advanced.gevent_tcp_dict.mysql_mode import PymysqlMode as MysqlMode


class TCPServer:
    def __init__(self, host='0.0.0.0', port=8888):
        self.host = host
        self.port = port
        self.addr = (host, port)
        self.db = MysqlMode(db="words_dict", user="root", passwd="asdf@1024")
        self.socket = socket(AF_INET, SOCK_STREAM)

    def hash_passwd(self, passwd: str):
        """
            将明文密码加密成 bcrypt 哈希
            返回字符串（便于存入数据库）
        :param passwd: 用户注册时输入的明文密码
        :return: 使用bcrypt 加盐后的密钥
        """
        # 加盐
        hashed = bcrypt.hashpw(passwd.encode(), bcrypt.gensalt(12))
        return hashed.decode()

    def check_passwd(self, input_passwd: str, stored_hash: str) -> bool:
        """
            验证用户输入的密码是否正确
            :param input_passwd: 用户登录时输入的明文密码
            :param stored_hash: 从数据库取出的已加密密码（字符串）
            :return: True if match
        """
        return bcrypt.checkpw(input_passwd.encode(), stored_hash.encode())

    def check_user(self, username: str) -> bool:
        sql = "select * from user where name = %s"
        if self.db.select(sql, (username,)):
            return True
        return False

    def login(self, c, data: dict[str, str]):
        """
            用户登陆处理逻辑
        :param c: socket
        :param data:
            from client user info
            data：{"data": {"name": "sd", "passwd": "sda"}}
        """
        name = data.get('name')
        passwd = data.get('passwd')
        sql = "select passwd from user where name = %s"
        # [{'id': 2, 'name': 'zx', 'passwd': 'sadfr', 'create_time': datetime.datetime(2026, 1, 5, 18, 18, 48)}]
        # 需要加盐，然后验证
        result = self.db.select(sql, (name,))  # list[dicti{str,str}]
        if result:
            stored_hash = result[0].get('passwd')
            if self.check_passwd(passwd, stored_hash):
                c.send(json.dumps({"success": True, 'msg': "user login"}).encode())
            else:
                c.send(json.dumps({"success": False, 'msg': "Incorrect password"}).encode())
        else:
            c.send(json.dumps({"success": False, 'msg': "User not found"}).encode())

    def register(self, c, data):
        name = data.get('name')
        if not self.check_user(name):
            passwd = self.hash_passwd(data.get('passwd'))
            sql = "insert into user(name,passwd) values(%s,%s)"
            if self.db.insert(sql, (name, passwd)):
                c.send(json.dumps({"success": True, 'msg': 'User created successfully'}).encode())
            else:
                c.send(json.dumps({"success": False, 'msg': 'Network error'}).encode())
        else:
            c.send(json.dumps({"success": False, 'msg': 'user already exists'}).encode())

    def query(self, c, data):
        sql = "select * from words where word = %s"
        word = data.get('word')
        username = data.get('username')
        result = self.db.select(sql, (word,))
        if result:
            translation = result[0].get("translation")
            c.send(json.dumps({"success": True, 'translation': translation}).encode())
            sql = "insert into user_queries (name,content,words) values(%s,%s,%s)"
            self.db.insert(sql, (username, translation, word))
        else:
            c.send(json.dumps({"success": False, 'msg': 'word not found'}).encode())

    def history(self, c, data):
        username = data.get('username')
        sql = "select * from user_queries where name = %s limit 3"
        result = self.db.select(sql, (username,))
        if result:
            c.send(json.dumps({"success": True, 'msg': result}, default=str, ensure_ascii=False).encode() + b"##")
        else:
            print("查询历史")
            c.send(json.dumps({"success": False, 'msg': 'User not query'}).encode() + b"##")

    def _handle(self, c):
        """
            login {'name': 'ds', 'passwd': 'sds'}
        :param c: connection
        """
        try:
            handle_dict = {
                "login": self.login,
                "register": self.register,
                "query": self.query,
                "history": self.history
            }
            while True:
                msg = c.recv(1024).decode()
                print("from client:", msg)
                try:
                    msg = json.loads(msg)
                except json.JSONDecodeError as e:
                    c.send(json.dumps({"success": False, "msg": "JSON格式错误"}).encode())
                    continue
                if not msg:
                    c.close()
                    break
                if msg.get('type') in handle_dict:
                    reqs_type = msg.get('type')
                    reqs_data = msg.get('data')
                    handle_dict[reqs_type](c, reqs_data)
        except Exception as e:
            print(e)
        finally:
            c.close()
    def main(self):
        self.socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.socket.bind(self.addr)
        self.socket.listen(5)
        while True:
            try:
                conn, addr = self.socket.accept()
                print("connected from", addr)
                gevent.spawn(self._handle, conn)
                # thread = threading.Thread(target=self._handle, args=(conn,))
                # thread.start()
                # thread.daemon = True
            except Exception as e:
                print(e)


if __name__ == '__main__':

    server = TCPServer()
    server.main()

