#############################################################
##   Valkirye Bot by lowgod - https://github.com/lowg0d    ##
##                   date: 17/01/2022                      ##
##                     version: 0.1                        ##
#############################################################  

from email import message
from turtle import title
import discord
import datetime
from discord.ext import commands
from datetime import date, datetime
from discord_slash.utils.manage_components import create_button, create_actionrow
from discord_slash.model import ButtonStyle

#Bot token
TOKEN = 'OTMxMTQ2OTU0NTc3MTc0NTI4.YeAMLQ.2UWTleh_FKjwt--zGw5DlZWpt9E'
#Bot Prefix
PREFIX = '$'
#Bot Description
DESCRIPTION = """This is Valkyrie Bot"""
#Bot Name
BOTNAME = "Valkirye Bot"

intents = discord.Intents().all()

#################################################################################

bot = commands.Bot(command_prefix=PREFIX, description=DESCRIPTION) # start bot

# Dont Touch
project_version = " v0.1" # Project Version
# Log
date = datetime.utcnow().strftime("%d"+"/"+"%m"+"/"+"%y "+"%H"+":"+"%M"+":"+"%S") # get date 
log = f"[{date} INFO]: " # log format
# Color
embed_color = discord.Color.from_rgb(252, 15, 252)

#################################################################################

def DiscorBot():
    # On Ready Event
    @bot.event
    async def on_ready():
        print(log+"Starting " + BOTNAME + project_version)
        print("-------------------------------")
        print(log+"Logged in as:")
        print(log+'Username: {0}'.format(bot.user.name))
        print(log+'ID: {0}'.format(bot.user.id))
        print("-------------------------------")
        print(log+BOTNAME + " Sucesfully Started")

    ###### COMMANDS ######
    # Ping Command
    @bot.command()
    async def ping(ctx): 
        await ctx.send('pong') # send "pong" to channel
    # SlowMode Command
    @bot.command()
    @commands.has_permissions(administrator=True)
    async def slowmode(ctx, seconds: int):
        await ctx.channel.edit(slowmode_delay=seconds)
        await ctx.send(f"Slow mode is  on, you can only talk every {seconds} seconds.")
    # Clear Command
    @bot.command(aliases = [ 'delete'])
    @commands.has_permissions(manage_messages=True)
    async def clear(ctx, amount : int):
        if amount is None:
            await ctx.channel.purge(limit=100)
        else:
            await ctx.channel.purge(limit=amount)
    # Ban Command
    @bot.command()
    @commands.has_permissions(ban_members=True)
    async def ban(ctx,member: discord.Member,*,reason = "No specified reason."):
        await member.send("You have been banned from the Discord! Reason: " + reason)
        await member.ban(reason = reason)
    # Kick Command
    @bot.command()
    @commands.has_permissions(kick_members=True)
    async def kick(ctx,member: discord.Member,*,reason = "No specified reason."):
        await member.send("You have been kicked from the Discord! Reason: " + reason)
        await member.kick(reason = reason)
    # Announcement Command
    @bot.command()
    @commands.has_permissions(administrator=True)
    async def announcement(ctx, *, description):
        embed = discord.Embed(title="__**Announcement**__", description=f"Created by {ctx.author.mention}",
            color=discord.Color.purple())
        embed.add_field(name="Description", value=description)
        channel = ctx.guild.get_channel(928713167620669573)
        msg = await channel.send(embed=embed)
    # Pool Command
    @bot.command()
    @commands.has_permissions(administrator=True)
    async def poll(ctx, *, description):
        embed = discord.Embed(title="__**Pool**__", description=f"Created by {ctx.author.mention}",
            color=discord.Color.purple())
        embed.add_field(name="Description", value=description)
        channel = ctx.guild.get_channel(928713167620669573)
        msg = await channel.send(embed=embed)
        await msg.add_reaction("✅")
        await msg.add_reaction("❌")
if __name__ == '__main__':
    DiscorBot()
    bot.run(TOKEN)

