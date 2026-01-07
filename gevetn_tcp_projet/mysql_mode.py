"""
    pymysql mode
"""

import pymysql
from contextlib import contextmanager

class PymysqlMode:
    def __init__(self, host='localhost',
                 port=3306,
                 user='root',
                 passwd=None, db=None, charset='utf8',autocommit=True,):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.db = db
        self.charset = charset
        self.autocommit = autocommit

    @contextmanager
    def get_connection(self):
        """上下文管理器：统一获取连接"""
        conn = None
        try:
            conn = pymysql.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                passwd=self.passwd,
                db=self.db,
                charset=self.charset,
                autocommit=self.autocommit,
                cursorclass=pymysql.cursors.DictCursor  # 返回字典格式
            )
            yield conn
        except Exception as e:
            if conn:
                conn.rollback()
            raise e
        finally:
            if conn:
                conn.close()

    def _execute_read(self, sql, params=None):
        with self.get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(sql, params)
                result = cursor.fetchall()
                return result if result else []

    def _execute_write(self, sql, params=None):
        with self.get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(sql, params)
                return cursor.rowcount  # 返回影响行数

    def insert(self, sql, params=None):
        return self._execute_write(sql, params)

    def update(self, sql, params=None):
        return self._execute_write(sql, params)

    def delete(self, sql, params=None):
        return self._execute_write(sql, params)

    def select(self, sql, params=None):
        return self._execute_read(sql, params)


