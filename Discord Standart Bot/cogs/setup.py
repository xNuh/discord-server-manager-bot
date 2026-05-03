import discord
from discord.ext import commands
from discord import app_commands
from utils.config import update_config
from utils.embeds import success_embed

class Setup(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    setup_group = app_commands.Group(name="setup", description="Commands to set up the bot", default_permissions=discord.Permissions(administrator=True))

    @setup_group.command(name="logchannel", description="Sets the log channel")
    async def set_log(self, interaction: discord.Interaction, channel: discord.TextChannel):
        update_config("logChannel", channel.id)
        await interaction.response.send_message(embed=success_embed(f"Log channel has been set to {channel.mention}!"))

    @setup_group.command(name="welcomechannel", description="Sets the channel for welcome messages")
    async def set_welcome(self, interaction: discord.Interaction, channel: discord.TextChannel):
        update_config("welcomeChannel", channel.id)
        await interaction.response.send_message(embed=success_embed(f"Welcome channel is now {channel.mention}."))

    @setup_group.command(name="staffrole", description="Sets the staff role (for tickets)")
    async def set_staff(self, interaction: discord.Interaction, role: discord.Role):
        update_config("staffRole", role.id)
        await interaction.response.send_message(embed=success_embed(f"Staff role has been changed to {role.mention}."))
        
    @setup_group.command(name="ticketcategory", description="Sets the category for tickets")
    async def set_category(self, interaction: discord.Interaction, category: discord.CategoryChannel):
        update_config("ticketCategory", category.id)
        await interaction.response.send_message(embed=success_embed(f"Tickets will now be created in {category.mention}."))

async def setup(bot):
    await bot.add_cog(Setup(bot))
