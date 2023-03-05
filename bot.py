import os
import discord
from dotenv import load_dotenv
import asyncio
from discord.ext import tasks
from discord.ext import commands


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='/', intents=intents)

@tasks.loop(seconds=10.0)
async def my_background_task():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=f'You are awesome'))
    await asyncio.sleep(5)
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=f'I like you'))

@client.event
async def on_ready():
    print("Backstabbr Automation is running")
    await client.wait_until_ready()
    my_background_task.start()

@client.command()
async def channelcreator(ctx, arg1, a: int, b: int, c):
    guild = ctx.message.guild
    print(guild.categories)
    for item in guild.categories:
        print(item)
    channel = discord.utils.get(ctx.guild.channels, name=c)
    channel_id = channel.id    
    for i in range(b):
        gamenumber = a + i
        
        if c!= "punk":
            new_cat = await guild.create_category(c)
        await guild.create_text_channel(f'{arg1}-{gamenumber}', category=channel_id)

@channelcreator.error
async def channelcreator_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('Make sure you have the type of game, the number where you are starting, and the number of games you want.')
        
client.run(TOKEN)

