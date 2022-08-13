import websocket
import json
from threading import *
websocket.enableTrace(True)

class ws_proc:
    def __init__(self, **kwargs):
        super(ws_proc, self).__init__(**kwargs)
        self.ws = websocket.WebSocket()
        self.lock = Lock()

    def connect_ws(self, room_num, send_msg):
        self.ws.connect("ws://127.0.0.1:8000/api/ws/chat/" + str(room_num) + "/")
        print("보낸 메세지: {}".format(json.dumps(send_msg)))
        self.ws.send(json.dumps(send_msg))

    def recv_data(self):
        self.data = self.ws.recv()
        print("받은 메세지: {}".format(self.data))
        return self.data

    def close_ws(self):
        print("디스커넥트")
        self.ws.close()