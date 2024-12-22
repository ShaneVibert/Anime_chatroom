from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict
import asyncio
import requests
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    fetch_anime_data()
    yield

# Rename `main` to `app`
app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

anime_data: Dict[int, Dict] = {}
chat_rooms: Dict[int, List[Dict]] = {}
connected_clients: Dict[int, List[WebSocket]] = {}

# Fetch Anime Data from AniList
def fetch_anime_data():
    url = "https://graphql.anilist.co"
    query = """
    query {
        Page(page: 1, perPage: 50) {
            media(type: ANIME) {
                id
                title {
                    romaji
                }
                genres
                description
                coverImage {
                    large
                }
            }
        }
    }
    """
    response = requests.post(url, json={"query": query})
    if response.status_code == 200:
        result = response.json()
        for anime in result["data"]["Page"]["media"]:
            anime_data[anime["id"]] = {
                "title": anime["title"]["romaji"],
                "genres": anime["genres"],
                "description": anime["description"],
                "coverImage": anime["coverImage"]["large"],
            }
            chat_rooms[anime["id"]] = []

@app.get("/anime")
async def get_anime():
    return {"anime": anime_data}

@app.websocket("/ws/{anime_id}")
async def websocket_endpoint(websocket: WebSocket, anime_id: int):
    anime_id = int(anime_id)
    await websocket.accept()

    if anime_id not in connected_clients:
        connected_clients[anime_id] = []
    connected_clients[anime_id].append(websocket)

    try:
        while True:
            data = await websocket.receive_json()
            message = {
                "user": data["user"],
                "content": data["content"],
                "timestamp": data["timestamp"],
            }
            chat_rooms[anime_id].append(message)

            for client in connected_clients[anime_id]:
                await client.send_json(message)

    except WebSocketDisconnect:
        # Remove disconnected client
        connected_clients[anime_id].remove(websocket)

# Get chat history for an anime
@app.get("/chat/{anime_id}")
async def get_chat_history(anime_id: int):
    return {"chat_history": chat_rooms.get(anime_id, [])}
