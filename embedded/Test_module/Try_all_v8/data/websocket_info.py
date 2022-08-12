from this import s
import threading
import websocket
import json
websocket.enableTrace(True)

class ws_proc:
    def __init__(self, **kwargs):
        super(ws_proc, self).__init__(**kwargs)
        self.ws = websocket.WebSocket()

    def ws_connect(self, room_num, send_msg=""):
        self.ws.connect("ws://127.0.0.1:8000/api/ws/chat/" + str(room_num) + "/")
        self.ws.send(json.dumps(send_msg))
        self.data = self.ws.recv()
        self.ws.close()

class wsapp_proc():
    def on_open(self, send_msg):
        self.wsapp.send(send_msg)

    def on_message(self, recv_msg):
        def run(*args):
            print(recv_msg)
            print("메세지 수신됨")
        threading.Thread(target=run).start()

    def on_close(self):
        self.wsapp.close()

    def wsapp_connect(self, room_num):
        def run(*args):
            self.wsapp = websocket.WebSocketApp(
                "ws://127.0.0.1:8000/api/ws/chat/" + 
                str(room_num) + "/",
                on_open=self.on_open,
                on_message=self.on_message,
                on_close=self.on_close
            )
            print("소켓연결")
            self.wsapp.run_forever()
        threading.Thread(target=run).start()