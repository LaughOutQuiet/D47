import discord
from discord import utils
from discord.utils import get
from discord.ext import commands
import asyncio

class textcmds:

  def __init__(self, bot):
          self.bot = bot

  @commands.command(pass_context=True, name = "cool")
  async def _cool(self, ctx):
    await self.bot.send_message(ctx.message.channel, "cool")

  @commands.command(pass_context=True, name = "number")
  async def _number(self, ctx):
    await self.bot.say("7")

  @commands.command(pass_context=True, name = "stressed")
  async def _stressed(self, ctx):
    await self.bot.say("throw egg")

  @commands.command(pass_context=True, name = "sheriff")
  async def _sheriff(self, ctx):
    await self.bot.say("DAIDEN THE SHERIFF, EVERYBODY!")

  @commands.command(pass_context=True, name = "lord")
  async def _lord(self, ctx):
    await self.bot.say("<@288131015745208321>")

  @commands.command(pass_context=True, name = "nevergonna")
  async def _nevergonna(self, ctx):
    await self.bot.say("give you up")
    
def setup(bot):
    bot.add_cog(textcmds(bot))
    print("textcmds loaded")
