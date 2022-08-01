from re import L
from mysql import connector

class db_proc:
    def create_db(self):
        self.db = connector.connect(
            host = '13.125.213.119',
            user = 'educolab',
            password = 'educolab',
            database = 'educolab'
        )
        self.cur = self.db.cursor()
        print("db 연결 성공!")

    def execute(self, query, args=()):
        self.cur.execute(query, args)
        return self.cur

    def db_close(self):
        self.db.close()
        self.cur.close()