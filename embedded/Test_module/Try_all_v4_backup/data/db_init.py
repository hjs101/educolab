from re import L
from mysql import connector

class db_proc:
    def create_db(self):
        self.db = connector.connect(
            host = '3.36.69.192',
            user = 'educolab',
            password = 'c102_edu',
            database = 'educolab'
        )
        self.cur = self.db.cursor()
        print("db 연결 성공!")

    def execute(self, query, args=()):
        self.cur.execute(query, args)
        return self.cur

<<<<<<< HEAD
<<<<<<< HEAD
    def db_commit(self):
        self.db.commit()
        
=======
>>>>>>> 207a577 (Refactor : v4_backup 추가)
=======
    def db_commit(self):
        self.db.commit()
        
>>>>>>> c9b8538 (Refactor : 기능 및 화면 조정)
    def db_close(self):
        print("db 연결 해제")
        self.db.close()
        self.cur.close()