from fastapi import Depends
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorCollection
from app_conf import app_conf
from typing import Annotated

__client = AsyncIOMotorClient(str(app_conf.db_url))


async def __get_db_connection() -> AsyncIOMotorCollection:
    return __client[app_conf.db_name]["portfolio"]


MyDb = Annotated[AsyncIOMotorCollection, Depends(__get_db_connection)]
