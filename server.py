import asyncio
import random
from websockets.server import serve

# Handler function for incoming connections
async def handle_message(websocket):
    async for message in websocket:
        # Modify the incoming message by appending msg "i got it"
        modified_message = f"{message} - {'Received! By Server.'}"
        # Send the modified message back to the client
        await websocket.send(modified_message)

# Function to start the WebSocket server
async def start_server():
    async with serve(handle_message, "localhost", 8765):
        await asyncio.Future()  # Run the server forever

# Main function to run the WebSocket server
if __name__ == "__main__":
    asyncio.run(start_server())