import asyncio
import os

from aiogram import Bot, Dispatcher, Router
from aiogram.types import Message
from dotenv import load_dotenv

# Load environment variables from .env file (e.g., your bot token)
load_dotenv()

# Initialize the bot with the token from environment variables
bot = Bot(token=os.getenv("token"))

# Create a router to group message handlers
user_router = Router()


# Define a simple echo handler: replies with the same message text
@user_router.message()
async def echo(message: Message):
    await message.answer(message.text)


# Create the main Dispatcher that will handle all updates
dp = Dispatcher()

# Register the router with the dispatcher
dp.include_router(user_router)


# Main entry point of the bot: starts polling for updates
async def main():
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


# Run the bot when the script is executed directly
if __name__ == "__main__":
    asyncio.run(main())
