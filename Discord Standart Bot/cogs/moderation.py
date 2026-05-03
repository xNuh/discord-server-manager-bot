import discord
from discord.ext import commands
from discord import app_commands
import datetime

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="ban", description="Bans a user")
    @app_commands.default_permissions(ban_members=True)
    async def banUser(self, interaction: discord.Interaction, member: discord.Member, reason: str = "No reason provided"):
        if member.top_role >= interaction.user.top_role:
            return await interaction.response.send_message("You cannot ban this user!", ephemeral=True)
            
        await member.ban(reason=reason)
        em = discord.Embed(title="User Banned", description=f"{member.mention} was banned.\nReason: {reason}", color=discord.Color.red())
        await interaction.response.send_message(embed=em)

    @app_commands.command(name="timeout", description="Times out a user")
    @app_commands.default_permissions(moderate_members=True)
    async def timeoutUser(self, interaction: discord.Interaction, member: discord.Member, minutes: int, reason: str = None):
        if member.top_role >= interaction.user.top_role:
            return await interaction.response.send_message("Cannot timeout this user.", ephemeral=True)
            
        time = datetime.timedelta(minutes=minutes)
        await member.timeout(time, reason=reason)
        
        await interaction.response.send_message(f"Timed out {member.mention} for {minutes} minutes. Reason: {reason}")

    @app_commands.command(name="warn", description="Warns a user (text only)")
    @app_commands.default_permissions(kick_members=True)
    async def warn(self, interaction: discord.Interaction, member: discord.Member, reason: str):
        # just send a simple embed, a full warning system might be too much right now
        em = discord.Embed(title="⚠️ Warning", description=f"{member.mention} has been warned!\n**Reason:** {reason}", color=discord.Color.orange())
        em.set_footer(text=f"By {interaction.user.name}")
        await interaction.response.send_message(embed=em)
        
        try:
            await member.send(f"You were warned on **{interaction.guild.name}**. Reason: {reason}")
        except:
            pass # user has DMs off, doesn't matter

    @app_commands.command(name="clear", description="Deletes messages in the chat")
    @app_commands.default_permissions(manage_messages=True)
    async def clearChat(self, interaction: discord.Interaction, amount: int):
        if amount > 100:
            return await interaction.response.send_message("Cannot delete more than 100 at once!", ephemeral=True)
            
        # we have to respond first or we'll get an error
        await interaction.response.defer(ephemeral=True)
        deleted = await interaction.channel.purge(limit=amount)
        await interaction.followup.send(f"Deleted {len(deleted)} messages 👍")

async def setup(bot):
    await bot.add_cog(Moderation(bot))
