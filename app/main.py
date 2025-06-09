from fastapi import FastAPI
from app.routes import threats, websocket
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(threats.router)
app.include_router(websocket.router)

@app.get("/")
def root():
    return {"message": "Phantom Radar Backend Running"}
