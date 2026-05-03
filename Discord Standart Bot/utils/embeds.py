import discord

def simpleEmbed(title, desc, color=discord.Color.blue()):
    em = discord.Embed(title=title, description=desc, color=color)
    em.set_footer(text="Server Manager Bot")
    return em

def errorEmbed(text):
    return discord.Embed(title="Error", description=text, color=discord.Color.red())

def success_embed(text):
    return discord.Embed(title="Success", description=text, color=discord.Color.green())
