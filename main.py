import os
import disnake
from dotenv import load_dotenv
from disnake.ext import commands

load_dotenv()

bot = commands.Bot(
    command_prefix='#$',
    intents=disnake.Intents.all()
)


@bot.event
async def on_ready():
    print("Bot started!")


@bot.slash_command()
async def ping(inter):
    await inter.response.send_message("Pong!")


bot.run(os.environ["BOT_TOKEN"])