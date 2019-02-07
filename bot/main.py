import discord
from discord.ext import commands
from discord.ext.commands import bot
from discord import utils
from discord.utils import get
import asyncio

bot = commands.Bot(command_prefix="d?")

blacklisted_users = ["288810189266616320"]

@bot.event
async def on_ready():
	bot.change_presence(game=discord.Game(name="cool"))
	print("cool\ncool")
	print("{} server(s)".format(len(bot.servers)))
	for server in bot.servers:
		print(server.name)

@bot.event
async def on_message(message):

	if message.author == bot.user:
		return

	if message.author.id in blacklisted_users:
		return

	nm = message.content.split(" ")
	for x in nm:
		if x.lower() == "cool":
			await bot.send_message(message.channel, "cool")
			return
	
	await bot.process_commands(message)

@bot.command(pass_context=True, name = "cool")
async def _cool(ctx):
	await bot.send_message(ctx.message.channel, "cool")

@bot.command(pass_context=True, name = "number")
async def _number(ctx):
	await bot.say("7")

@bot.command(pass_context=True, name = "stressed")
async def _stressed(ctx):
	await bot.say("throw egg")

@bot.command(pass_context=True, name = "sheriff")
async def _sheriff(ctx):
	await bot.say("DAIDEN THE SHERIFF, EVERYBODY!")

@bot.command(pass_context=True, name = "lord")
async def _lord(ctx):
	await bot.say("<@288131015745208321>")

@bot.command(pass_context=True, name = "nevergonna")
async def _nevergonna(ctx):
	await bot.say("give you up")

##################
#                #
# ADMIN COMMANDS #
#                #
##################

@bot.command(pass_context=True, name = "blist")
async def _blist(ctx, public: int = 0):
	message = ""
	if len(blacklisted_users) == 0:
		await bot.say("Nobody is banned")
		return
	for x in blacklisted_users:
		message = message + "<@{}> ".format(x)
	msg = discord.Embed(title = "**Banned Users**", description = message, color = 0x00D2FF)
	if public == 0:
		await bot.send_message(ctx.message.author, embed = msg)
	elif public == 1:
		if ctx.message.author.id == '223592612588814336':
			await bot.say(embed = msg)
	return

@bot.command(pass_context=True, name = "ban")
async def _ban(ctx, user: discord.User = None):	
	if ctx.message.author.id == '223592612588814336':
		if user is None:
			await bot.say("`Invalid Syntax: d?ban <user>`")
			return
		else:
			if user.id in blacklisted_users:
				await bot.say("`{}` is already blacklisted".format(user))
				return
			else:
				blacklisted_users.append(user.id)
				await bot.say("`{}` has been blacklisted".format(user))
				return
			
@bot.command(pass_context=True, name = "id")
async def _id(ctx, user: discord.User = None):	
	if ctx.message.author.id == '223592612588814336':
		if user is None:
			await bot.say(ctx.message.author.id)
			return
		else:
			await bot.say(user.id)
			return

bot.run("NTQyNDg3MDE4NjY4NTU2Mjk5.DzvB0w.WsVV5eoQCo4Yb8HuVIxc0XoN45U")
