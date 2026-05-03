import discord
from discord.ext import commands
from utils.config import loadConfig

class Logs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def get_log_channel(self, guild):
        config = loadConfig()
        chan_id = config.get("logChannel")
        if chan_id:
            return guild.get_channel(chan_id)
        return None

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if message.author.bot: return
        
        channel = self.get_log_channel(message.guild)
        if channel:
            em = discord.Embed(title="🗑️ Message Deleted", color=discord.Color.red())
            em.add_field(name="User", value=message.author.mention, inline=False)
            em.add_field(name="Channel", value=message.channel.mention, inline=False)
            em.add_field(name="Content", value=message.content or "No text (maybe an image)", inline=False)
            await channel.send(embed=em)

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        if before.author.bot: return
        if before.content == after.content: return # sometimes triggers for links or embeds
        
        channel = self.get_log_channel(before.guild)
        if channel:
            em = discord.Embed(title="✏️ Message Edited", color=discord.Color.yellow())
            em.add_field(name="User", value=before.author.mention, inline=False)
            em.add_field(name="Old", value=before.content or "-", inline=False)
            em.add_field(name="New", value=after.content or "-", inline=False)
            await channel.send(embed=em)

async def setup(bot):
    await bot.add_cog(Logs(bot))
