import os
import discord
from dotenv import load_dotenv
import asyncio
from discord.ext import tasks
from discord.ext import commands
from discord import app_commands


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
# GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='/', intents=intents)
# tree = app_commands.CommandTree(client)

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
async def create_channels(ctx, category_name, channel_base_name, start_number, num_channels):
    guild = ctx.guild
    category = await guild.create_category(category_name)

    for i in range(int(start_number), int(start_number) + int(num_channels)):
        channel_name = f'{channel_base_name}-{i}'
        channel = await guild.create_text_channel(channel_name, category=category)
        print(f'Created channel: {channel.name}')

@client.command()
async def create_tourney_channels(ctx, category_name, channel_base_name, start_set_number, number_in_set, num_channels):
    guild = ctx.guild
    category = await guild.create_category(category_name)

    for i in range(int(start_set_number), int(start_set_number) + int(num_channels)):
        for x in range (int(number_in_set)):
            channel_name = f'{channel_base_name} Set {i} Game {x+1}'
            channel = await guild.create_text_channel(channel_name, category=category)
            print(f'Created channel: {channel.name}')        

""" @channelcreator.error
async def channelcreator_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('Make sure you have the type of game, the number where you are starting, and the number of games you want.') """
        
client.run(TOKEN)

