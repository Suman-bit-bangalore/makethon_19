from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import asyncio

app = FastAPI()

# Store connected WebSocket clients
clients = []

async def broadcast_message(message: str):
    for client in clients:
        await client.send_text(message)

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    clients.append(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await broadcast_message(data)  # Echo the received message to all clients
    except WebSocketDisconnect:
        clients.remove(websocket)  # Remove client on disconnect
        await broadcast_message("A client has disconnected.")  # Notify others about the disconnection