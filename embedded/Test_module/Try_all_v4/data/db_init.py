from re import L
from mysql import connector

class db_proc:
    def create_db(self):
        self.db = connector.connect(
<<<<<<< HEAD
<<<<<<< HEAD
            host = '3.36.69.192',
            user = 'educolab',
            password = 'c102_edu',
=======
            host = '13.125.213.119',
            user = 'educolab',
            password = 'educolab',
>>>>>>> dbdcd45 (Refactor : v3, v4 구분)
=======
            host = '3.36.69.192',
            user = 'educolab',
            password = 'c102_edu',
>>>>>>> 4c23f18 (안올라온 파일들 있어서...)
            database = 'educolab'
        )
        self.cur = self.db.cursor()
        print("db 연결 성공!")

    def execute(self, query, args=()):
        self.cur.execute(query, args)
        return self.cur

<<<<<<< HEAD
    def db_commit(self):
        self.db.commit()

=======
>>>>>>> dbdcd45 (Refactor : v3, v4 구분)
    def db_close(self):
        print("db 연결 해제")
        self.db.close()
        self.cur.close()