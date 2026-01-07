"""
    dict client
"""
import json
from socket import *


class TCPClient:
    def __init__(self, host: str, port: int):
        self.addr = (host, port)
        self.sock = socket(AF_INET, SOCK_STREAM)
        try:
            self.sock.connect(self.addr)
        except Exception as e:
            print(e)
            exit()

    def send_request(self, reqs_type: str, data: dict[str, str]):
        try:
            req = {'type': reqs_type, 'data': data}
            packet = json.dumps(req).encode() + b'\n'
            self.sock.send(packet)
        except Exception as e:
            raise e

    def recv_request(self):
        while True:
            resp = self.sock.recv(1024).decode()
            if resp.endswith("##"):
                return resp.rstrip("##")

    def _login(self):
        name = input("请输入用户名：")
        passwd = input("请输入密码：")
        self.send_request("login", {'name': name, 'passwd': passwd})
        resp = self.sock.recv(1024).decode()
        resp = json.loads(resp)
        if resp.get('success'):
            print(resp.get('msg'))
            return name
        print(resp.get('msg'))
        return False

    def _register(self):
        name = input("请输入用户名：")
        passwd = input("请输入密码：")
        self.send_request("register", {'name': name, 'passwd': passwd})
        resp = self.sock.recv(1024).decode()
        resp = json.loads(resp)
        print(resp)
        if resp.get('success'):
            return True
        else:
            return False

    def query_word(self, word: str, username: str):
        self.send_request("query", {'word': word, 'username': username})
        resp = self.sock.recv(1024).decode()
        resp = json.loads(resp)
        if resp.get('success'):
            print(f"{word} translation：{resp.get('translation')}")
        else:
            print(f"{word} Sorry, the word cannot be found.")

    def show_history(self, username: str):
        self.send_request("history", {'username': username})
        resp = json.loads(self.recv_request())
        print(resp)
        if resp.get('success'):
            for i, record in enumerate(resp.get('msg')):
                content = record['content'].strip()
                word = record['words']
                time = record['search_time']
                print(f"第{i + 1}次查询的单词是：{word},翻译内容是：{content},查询时间：{time}")
        else:
            print(f"用户{username} 无查询历史")

    def show_search_menu(self, username: str):
        while True:
            print("\n" + "=" * 40)
            print(f"{'1. 查询单词':^40}")
            print(f"{'2. 查看历史':^40}")
            print(f"{'3. 注销账户':^40}")
            print(f"{'4. 退出系统':^40}")
            print("=" * 40)
            choice = input("请选择 > ").strip()
            if choice == "1":
                word = input("请输入单词: ").strip()
                self.query_word(word, username)
            elif choice == "2":
                self.show_history(username)
            elif choice == "3":
                return  # 返回登录页
            elif choice == "4":
                print("👋 再见！")
                exit()
            else:
                print("⚠️ 输入无效，请重试")

    def run(self):
        while True:
            print("\n🔥 欢迎使用在线词典")
            print("1. 登录")
            print("2. 注册")
            print("3. 退出")
            choice = input("请选择 > ").strip()
            if choice == "1":
                username = self._login()
                if username:
                    self.show_search_menu(username)
                else:
                    print("\n ##### 输入有误，请重新选择 ##### \n")
                    continue
            elif choice == "2":
                if self._register():
                    continue
                else:
                    print("用户已存在，请重新输入")
                    continue
            elif choice == "3":
                print("👋 再见！")
                break
            else:
                print("❌ 无效选择")


if __name__ == "__main__":
    tcp_client = TCPClient("127.0.0.1", 8888)
    tcp_client.run()

