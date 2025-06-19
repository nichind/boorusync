from boorusync import *
from asyncio import run
from boorusync.core.config import Config
from boorusync.core.boards import DanbooruAPI
import asyncio

async def main():
    config = Config()
    danbooru_api = DanbooruAPI(config)
    user_id = 12345  # Replace with the actual user ID
    favorites = await danbooru_api.get_favorites(user_id)
    favorite_groups = await danbooru_api.get_favorite_groups(user_id)
    print("Favorites:", favorites)
    print("Favorite Groups:", favorite_groups)
        
if __name__ == "__main__":
    run(main())
    