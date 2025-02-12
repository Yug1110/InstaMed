import asyncio
import websockets

async def test_chat():
    uri = "ws://127.0.0.1:8000/ws/chatbot"
    async with websockets.connect(uri) as websocket:
        await websocket.send("hello")
        response = await websocket.recv()
        print("Chatbot:", response)

asyncio.run(test_chat())
