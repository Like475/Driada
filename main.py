import os
import disnake
from dotenv import load_dotenv
from disnake.ext import commands
from tools.keep_alive import keep_alive  # Required for deployment in repl.it

if os.path.exists('./.env'):
    load_dotenv()

bot = commands.Bot(
    command_prefix='#$',
    intents=disnake.Intents.all()
)


@bot.event
async def on_ready():
    print('Bot started!')


@bot.slash_command()
async def ping(inter):
    await inter.response.send_message('Pong!')

if __name__ == '__main__':
    keep_alive()  # Required for deployment in repl.it
    bot.run(os.environ['BOT_TOKEN'])
