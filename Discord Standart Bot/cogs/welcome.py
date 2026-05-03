import discord
from discord.ext import commands
from utils.config import loadConfig
from utils.embeds import simpleEmbed

class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        config = loadConfig()
        welcome_id = config.get("welcomeChannel")
        
        if welcome_id:
            channel = member.guild.get_channel(welcome_id)
            if channel:
                em = simpleEmbed(
                    f"Welcome {member.name}!", 
                    f"Hey {member.mention}, welcome to **{member.guild.name}**!\nWe now have {member.guild.member_count} users.",
                    color=discord.Color.green()
                )
                em.set_thumbnail(url=member.display_avatar.url)
                await channel.send(embed=em)
                
        # log channel join msg
        log_id = config.get("logChannel")
        if log_id:
            log_ch = member.guild.get_channel(log_id)
            if log_ch:
                await log_ch.send(f"➡️ {member.mention} has joined.")

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        config = loadConfig()
        log_id = config.get("logChannel")
        
        if log_id:
            log_ch = member.guild.get_channel(log_id)
            if log_ch:
                await log_ch.send(f"⬅️ {member.name} ({member.id}) has left the server.")

async def setup(bot):
    await bot.add_cog(Welcome(bot))
