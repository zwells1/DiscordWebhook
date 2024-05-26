# example code
# https://www.youtube.com/watch?v=hbxeZdOHUbA

#another example:
#https://github.com/ezioruan/midjourney-python-api
import asyncio
import discord
from discord import Webhook
import aiohttp

async def anything(url):
    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url(url, session=session)
        embed = discord.Embed(title="FooBar")
        await webhook.send(embed=embed, username="Zwells")#user name might need to be set

if __name__ == "__main__":
    url = "https://discord.com/api/webhooks/1196679598889508935/K_vQOWsJZS-wfeGmFvvCXKhmHDuqSt7WLWzjzXTA0EXi_KLqIRzvyNNpU_YWMifSJTT0"

    loop = asyncio.new_event_loop()
    loop.run_until_complete(anything(url))
    loop.close()
