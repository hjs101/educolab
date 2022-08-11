from re import L
from mysql import connector

class db_proc:
    def create_db(self):
        self.db = connector.connect(
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
            host = '3.36.69.192',
            user = 'educolab',
            password = 'c102_edu',
=======
            host = '13.125.213.119',
            user = 'educolab',
            password = 'educolab',
>>>>>>> 210a2e8 (Feat : 메인화면 추가)
=======
            host = '3.36.69.192',
            user = 'educolab',
            password = 'c102_edu',
>>>>>>> dbee603 (Refactor: login token 발급)
=======
            host = '3.36.69.192',
            user = 'educolab',
            password = 'c102_edu',
>>>>>>> d61ea9f (fix: embedded update)
            database = 'educolab'
        )
        self.cur = self.db.cursor()
        print("db 연결 성공!")

    def execute(self, query, args=()):
        self.cur.execute(query, args)
        return self.cur

    def db_close(self):
        print("db 연결 해제")
        self.db.close()
        self.cur.close()