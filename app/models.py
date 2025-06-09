from fastapi import APIRouter, WebSocket
from typing import List

router = APIRouter()

clients: List[WebSocket] = []

@router.websocket("/threats/live")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    clients.append(websocket)
    try:
        while True:
            await websocket.receive_text()  # Ping loop
    except:
        clients.remove(websocket)

async def broadcast_threat(data: dict):
    for ws in clients:
        await ws.send_json(data)

