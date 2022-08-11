import asyncio
import websockets

async def connect():
  async with websockets.connect("ws://127.0.0.1:8000/api/chat/1234") as websocket:
    for i in range(1,10,1):
      await websocket.send("hello socket!!")
      data = await websocket.recv()
      print(data)
asyncio.get_event_loop().run_until_complete(connect())
