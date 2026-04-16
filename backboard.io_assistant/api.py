from fastapi import FastAPI
import asyncio
from services.backboard_service import BackboardService

app = FastAPI()
service = BackboardService()

@app.get("/")
def home():
    return {"message": "AI Assistant Running 🚀"}

@app.post("/chat")
async def chat(message: str):
    assistant = await service.create_assistant()
    thread = await service.create_thread(assistant.assistant_id)
    response = await service.send_message(thread.thread_id, message)

    return {"response": response.content}