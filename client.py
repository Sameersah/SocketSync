import asyncio
import websockets

# Function to send and receive messages from the WebSocket server
async def communicate():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        for i in range(10000):
            # Send a message to the server
            await websocket.send(f"Hello, server! Message {i+1}")
            # Wait for a response from the server
            response = await websocket.recv()
            print(f"Received from server: {response}")

# Main function to run the WebSocket client
if __name__ == "__main__":
    asyncio.run(communicate())