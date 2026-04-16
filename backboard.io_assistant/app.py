import asyncio
from services.backboard_service import BackboardService

async def main():
    service = BackboardService()

    assistant = await service.create_assistant()
    print(f"Created assistant: {assistant.assistant_id}")

    thread = await service.create_thread(assistant.assistant_id)
    print(f"Created thread: {thread.thread_id}")

    response = await service.send_message(thread.thread_id, "say Hello World")
    print(f"Assistant: {response.content}")

if __name__ == "__main__":
    asyncio.run(main())