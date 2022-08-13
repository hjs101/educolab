from this import s
import threading
import websocket
import json
websocket.enableTrace(True)

class ws_proc:
    def __init__(self, **kwargs):
        super(ws_proc, self).__init__(**kwargs)
        self.ws = websocket.WebSocket()

    def connect_ws(self, room_num, send_msg=""):
        self.ws.connect("ws://127.0.0.1:8000/api/ws/chat/" + str(room_num) + "/")
        self.ws.send(json.dumps(send_msg))

    def recv_data(self):
        return self.ws.recv()

    def close_ws(self):
        self.ws.close()

# class wsapp_proc:
#     def __init__(self, **kwargs):
#         super(wsapp_proc, self).__init__(**kwargs)

#     def on_open(self, send_msg):
#         self.wsapp.send(send_msg)

#     def on_message(self, recv_msg):
#         def run(*args):
#             print(recv_msg)
#             print("Message received...")
#         threading.Thread(target=run).start()

#     def on_close(self, close_status_code, close_msg):
#         print("Closed")

#     def wsapp_connect(self, room_num):
#         print("진입")
#         self.wsapp = websocket.WebSocketApp(
#                 "ws://127.0.0.1:8000/api/ws/chat/" + 
#                 str(room_num) + "/",
#                 on_open=self.on_open,
#                 on_message=self.on_message,
#                 on_close=self.on_close
#             )
#         self.wsapp.run_forever()