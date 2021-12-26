#!/usr/bin/env python
# coding: utf-8

# In[1]:
import asyncio
import discord
from discord import Client, Intents, Embed
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_option, create_choice
from discord_slash.model import SlashCommandPermissionType
import os
import json
import atexit
bot = commands.Bot(command_prefix="$")
user = discord.user
slash = SlashCommand(bot, sync_commands=True)
global i
i = 0
print("angekommen1")


async def wait_i_0():
    global i
    print(i)
    while i > 0:
        await asyncio.sleep(1)
        i -= 1
        print(i)


if os.path.exists('languageG.json'):
    with open('languageG.json') as json_file:
        languageG = json.load(json_file)
else:
    languageG = {
        '801144147720404992': 'eng',
        '919576368918974544': 'eng',
        }
timer = {
     "801144147720404992": "0"
    }
if os.path.exists("Perms.json"):
    with open("Perms.json")as json_file:
        Perms = json.load(json_file)

else:
    Perms = {
        "hallo": "test"
    }


@bot.event
async def on_message(message):
    global i
    guild = str(message.guild.id)
    channel = message.channel
    print(guild)
    print("message detected")
    if message.content.startswith("$p") and i == 0:
        await channel.send(message.content)
    elif message.content.startswith("$s"):
        i = 4
        asyncio.create_task(wait_i_0())
    if guild in languageG:
        languageG[guild] = "eng"


@slash.slash(
    name="perms",
    description="changes the perms to use /act",
    options=[create_option(
        name="neededperm",
        description="the perm you need to use /act",
        option_type=3,
        required=True
        )])
async def perms(ctx, neededperm):
    if ctx.message.author.guild_permissions.administrator:
        guild = str(ctx.message.guild.id)
        Perms[guild] =needeperm
        if languageG[guild] == "de":
            text="die Berechtigungen wurden auf " + neededperm + " gesetzt."
        else:
            text="the perm have been updated to" + neededperm
    else:
        if languageG[guild]=="de":
            text = "dir fehlt die Berechtigung dafür"
        else:
            text = "missing perms"
    ctx.send(text)

@slash.slash(name="act",
            description="This is just a test command, nothing more.",
            options=[
                create_option(
                 name="optone",
                 description="here the Word to spam.",
                 option_type=3,
                 required=True
               )
             ])
async def act(ctx, optone: str):
    guild=str(ctx.guild.id)
    #if guild in Perms:
        #if (member.haspermission(Perms[guild]):
            #await ctx.send("$p " + optone)
        #else:
            #if languageG[guild]=="de":
                #text = "fehlende Berechtigung"
            #else:
                #text = "missing Perms"
            #await ctx.send(text)
    #else:
    await ctx.send("$p " + optone)


@slash.slash(name = "help",
        description="you need help then its useful for you"
        )
async def help(ctx: SlashContext):
    guild=str(ctx.guild.id)
    if guild in Perms:
        if ctx.message.author.Permissions.Perms[guild]:
            if languageG[guild] == "de":
                Title="Die Commands sind"
                value1="spammt die Nachricht mehrere male"
                value2="stopt den Spam"
                value3="lade den Bot auf deinen Server ein"
                value4="rufe dieses hier auf"
                value5="habt spaß"
            else:
                Title="The Commands are"
                value1="spam the message several times"
                value2="stop it from spamming"
                value3="invite the bot to your Server"
                value4="get to this here"
                value5="have fun"
        else:
            if languageG[guild]=="de":
                text = "fehlende Berechtigung"
            else:
                text = "missing Perms"
            await ctx.send(text)
    else:
        guild=str(ctx.guild.id)
        if languageG[guild] == "de":
            Title="Die Commands sind"
            value1="spammt die Nachricht mehrere male"
            value2="stopt den Spam"
            value3="lade den Bot auf deinen Server ein"
            value4="rufe dieses hier auf"
            value5="ändert die Sprache auf dem Server"
            value6="ein Feature, dass hoffentlich bald kommen wird, lasst am besten die pfoten davon"
            value7="habt spaß"
        else:
            Title="The Commands are"
            value1="spam the message several times"
            value2="stop it from spamming"
            value3="invite the bot to your Server"
            value4="get to this here"
            value5="changes the language on this server"
            value6="a new Feature, coming hopefully soon. please do not use it, it maybe breaks the Bot on your Server"
            value7="have fun"
        Embed=discord.Embed(title=Title, color=0xe5a50a)
        Embed.add_field(name="/act or $p(message)", value=value1, inline=True)
        Embed.add_field(name="/stop or $s", value=value2, inline=True)
        Embed.add_field(name="/invite", value=value3, inline=True)
        Embed.add_field(name="/help", value=value4, inline=True)
        Embed.add_field(name="/language", value=value5, inline=True)
        Embed.add_field(name="/perms", value=value6, inline=True)
        Embed.set_footer(text=value7)
        await ctx.send(embed=Embed)


@slash.slash(name = "stop")
async def stop(ctx: SlashContext):
    global i
    i = 4
    asyncio.create_task(wait_i_0())
    guild=str(ctx.guild.id)
    if  languageG[guild]=="de":
    	text="der Spam wurde gestoppt"
    else:
    	text="the Spam has been stoped"
    await ctx.send(text)



@slash.slash(name="language",
            description="change the language to.",
            options=[
                create_option(
                 name="code",
                 description="changes the language to",
                 option_type=3,
                 required=True,
                 choices=[create_choice(
                    name="Deutsch - German",
                    value="de"
                    ),
                 create_choice(
                    name="Englisch - english",
                    value="eng"
               )]
             )])
async def language(ctx, code: str):
    print(code)
    guild=str(ctx.guild.id)
    if guild in Perms:
        if ctx.message.author.Permissions.Perms[guild]:
            languageG[guild]=code
            if languageG[guild]=="de":
                Text="Die Sprache wurde auf Deutsch gesetzt"
            else:
                Text="The Language has been et to english"
            await ctx.send(Text)
        else: 
            if languageG[guild]=="de":
                text = "fehlende Berechtigung"
            else:
                text = "missing Perms"
            await ctx.send(text)
    else:
        languageG[guild] = code
        if languageG[guild]=="de":
            Text="Die Sprache wurde auf Deutsch geändert"
        else:
            Text="The language has been changed to english"
        await ctx.send(Text)




@slash.slash(name="invite")
async def invite(ctx: SlashContext):
    await ctx.send("https://discord.com/api/oauth2/authorize?client_id=919201478357418074&permissions=8&scope=applications.commands%20bot")

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="Pingspam", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ"))
    print("My Ready is Body")

@atexit.register
def googbye():
    print("goodbye")
    with open("languageG.json","w") as fp:
        json.dump(languageG,fp)
    with open("Perms.json","w") as fp:
        json.dump("Perms",fp)

bot.run(TOKEN)
