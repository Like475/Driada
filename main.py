import os
import disnake
from dotenv import load_dotenv
from disnake.ext import commands
from tools.keep_alive import keep_alive  # Required for deployment in repl.it

bot = commands.Bot(
    command_prefix=commands.when_mentioned_or('#$'),
    intents=disnake.Intents.all()
)


@bot.event
async def on_ready():
    bot.load_extensions('cogs')
    bot.load_extension('jishaku')
    print('Bot started!')


if __name__ == '__main__':
    if os.path.exists('./.env'):
        load_dotenv()  # Required for test
    else:
        keep_alive()  # Required for deployment in repl.it
    bot.run(os.environ['BOT_TOKEN'])
