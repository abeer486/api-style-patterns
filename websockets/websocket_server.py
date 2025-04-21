import asyncio
import websockets

async def echo(websocket, path):
    print("Client connected")
    try:
        async for message in websocket:
            print(f"Received: {message}")
            await websocket.send(f"Echo: {message}")
    except websockets.ConnectionClosed:
        print("Client disconnected")

# Start the WebSocket server
async def main():
    async with websockets.serve(echo, "localhost", 8765):
        print("WebSocket server started on ws://localhost:8765")
        await asyncio.Future()  # Run forever

if __name__ == "__main__":
    asyncio.run(main())