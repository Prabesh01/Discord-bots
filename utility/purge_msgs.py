import discord
from discord.ext import commands
import datetime
import asyncio
import logging

logging.basicConfig(level=logging.INFO)

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready() -> None:
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.command()
@commands.has_permissions(manage_messages=True)
async def clean2(ctx):
    if not  ctx.channel.id==1003685620947890266: return

    before_date = datetime.datetime(2024, 8, 1, tzinfo=datetime.timezone.utc)
    async for message in ctx.channel.history(before=before_date, limit=None):
        try:
            if message.id==1120249846050340884: break
            await message.delete()
            await asyncio.sleep(1.0)
        except discord.Forbidden:
            print(f"Missing permissions to delete message: {message.id}")
        except discord.HTTPException as e:
            print(f"Failed to delete message {message.id}: {e}")
            await asyncio.sleep(5.0)

bot.run("")
