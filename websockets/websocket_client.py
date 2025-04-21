import asyncio
import websockets

async def communicate():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        await websocket.send("Hello, Server!")
        response = await websocket.recv()
        print(f"Server says: {response}")

if __name__ == "__main__":
    asyncio.run(communicate())