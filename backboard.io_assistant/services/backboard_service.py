from utils.config import Config
from backboard import BackboardClient

class BackboardService:
    def __init__(self):
        self.client = BackboardClient(
            api_key = Config.BACKBOARD_API_KEY
        )

    async def create_assistant(self):
        return await self.client.create_assistant(
            name="My First Assistant",
            system_prompt="You are a helpful assistant that responds concisely."
        )

    async def create_thread(self, assistant_id):
        return await self.client.create_thread(assistant_id)

    async def send_message(self, thread_id, message):
        return await self.client.add_message(
            thread_id=thread_id,
            content=message,
            stream=False
        )