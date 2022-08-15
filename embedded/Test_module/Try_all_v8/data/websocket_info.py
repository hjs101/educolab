import websocket
import json
websocket.enableTrace(True)

class ws_proc:
    def __init__(self, **kwargs):
        super(ws_proc, self).__init__(**kwargs)
        self.ws = websocket.WebSocket()
        self.next_flag = 0

    def connect_ws(self, room_num, send_msg):
        self.ws.connect("wss://i7c102.p.ssafy.io/api/ws/chat/" + str(room_num) + "/")
        print("보낸 메세지: {}".format(json.dumps(send_msg)))
        self.ws.send(json.dumps(send_msg))

    def recv_data(self):
        while True:
            self.data = self.ws.recv()
            print("받은 메세지: {}".format(self.data))
            if json.loads(self.data)["message"] == "퀴즈 시작":
                print("다음문제 메세지")
                self.quiz_pk = json.loads(self.data)["proc_pk"]
                self.next_flag=1
                return self.data
            elif json.loads(self.data)["message"] == "결과 보기":
                print("퀴즈 종료 메세지")
                self.next_flag=-1
                return self.data

    def close_ws(self):
        print("디스커넥트")
        self.ws.close()