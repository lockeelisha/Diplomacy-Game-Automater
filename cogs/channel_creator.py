from datetime import datetime
import discord
from discord.ext import commands
import json
import traceback
import re
import os
from dotenv import load_dotenv
from discord import Embed, Member

import urllib

import asyncio

import DiscordUtils

# Load API key
load_dotenv()
class In_Game_Builds(commands.Cog):
    """Displays in-game info for a specific summoner"""
    def __init__(self, client):
        self.client = client   

    # Command "all_live"
    @commands.command()
    async def ping(self, ctx):
        await ctx.send('Pong!')