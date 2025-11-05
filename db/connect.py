from dotenv import load_dotenv
import os
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from blog import model_list

load_dotenv()

_client = None

async def connect_db():
    try:
        global _client

        MONGO_URI = os.getenv("MONGODB_URI")
        # print("Mongouri", MONGO_URI)

        _client = AsyncIOMotorClient(MONGO_URI, tz_aware=True)
        await _client.server_info() 

        await init_beanie(
            database=_client["Cluster"],
            document_models=model_list
        )

        print("Connected to database")

    except Exception as e:
        print("MongoDB connection failed: ", e)
        raise e
    
    
def get_client():
    if not _client:
        raise Exception("Database client not initialized. Call connect_db() first.")
    return _client