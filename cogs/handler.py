from disnake.ext import commands
import disnake


class Handler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, inter, error: commands.CommandError):
        if isinstance(error, commands.NotOwner):
            await inter.send(file=disnake.File('./media/not_owner.gif'))


def setup(bot):
    bot.add_cog(Handler(bot))
