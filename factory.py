from fastapi import FastAPI
from dotenv import load_dotenv
import os
from api.chat_bot_apis import teams_chat_bot



def create_app():
    if not os.getenv('ENVIRONMENT', None):
        dotenv_path = 'config/.env'
        load_dotenv(dotenv_path)
    app = FastAPI(title='chatbot_app')
    app.include_router(teams_chat_bot.TEAMS_CHAT_BOT, prefix='/api/v1')
    return app