import websocket
import threading

websocket.enableTrace(True)

def on_open(ws):
    ws.send("hi")

def on_message(ws, message):
    def run(*args):
        print(message)
        ws.close()
        print("Message received...")

    threading.Thread(target=run).start()

def on_close(ws, close_status_code, close_msg):
    print(">>>>>>CLOSED")

wsapp = websocket.WebSocketApp("wss://api.bitfinex.com/ws/1", on_open=on_open, on_message=on_message, on_close=on_close)
wsapp.run_forever()