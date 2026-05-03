import discord
from discord.ext import commands
from discord import app_commands
from utils.config import loadConfig
from utils.embeds import simpleEmbed

class TicketCloseButton(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Close Ticket", style=discord.ButtonStyle.red, custom_id="close_ticket_btn")
    async def closeTicket(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("Ticket will be deleted in 5 seconds...", ephemeral=True)
        # Log who closed it (simply to log channel)
        try:
            cfg = loadConfig()
            logChannel_id = cfg.get("logChannel")
            if logChannel_id:
                ch = interaction.guild.get_channel(logChannel_id)
                if ch:
                    await ch.send(f"Ticket `{interaction.channel.name}` was closed by {interaction.user.mention}.")
        except Exception as e:
            print("log error:", e)
            
        import asyncio
        await asyncio.sleep(5)
        await interaction.channel.delete()

class TicketCreateButton(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        
    @discord.ui.button(label="Open Ticket", style=discord.ButtonStyle.blurple, custom_id="open_ticket_btn", emoji="🎫")
    async def open_ticket(self, interaction: discord.Interaction, button: discord.ui.Button):
        config = loadConfig()
        guild = interaction.guild
        
        # set permissions
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(read_messages=False),
            interaction.user: discord.PermissionOverwrite(read_messages=True, send_messages=True)
        }
        
        # check if staff role is set
        staff_id = config.get("staffRole")
        if staff_id:
            staff_role = guild.get_role(staff_id)
            if staff_role:
                overwrites[staff_role] = discord.PermissionOverwrite(read_messages=True, send_messages=True)
                
        category_id = config.get("ticketCategory")
        category = guild.get_channel(category_id) if category_id else None

        channel = await guild.create_text_channel(
            name=f"ticket-{interaction.user.name}",
            category=category,
            overwrites=overwrites
        )
        
        await interaction.response.send_message(f"Ticket created: {channel.mention}", ephemeral=True)
        
        em = simpleEmbed("New Ticket", f"Hey {interaction.user.mention}, please describe your issue. A team member will help you shortly.")
        view = TicketCloseButton()
        await channel.send(embed=em, view=view)


class Tickets(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    # command to send the ticket panel
    @app_commands.command(name="ticket_panel", description="Sends the ticket system panel")
    @app_commands.default_permissions(administrator=True)
    async def ticket_panel(self, interaction: discord.Interaction):
        em = simpleEmbed("Support Tickets", "Click the button below to open a ticket and talk to support.")
        view = TicketCreateButton()
        await interaction.response.send_message("Ticket panel sent!", ephemeral=True)
        await interaction.channel.send(embed=em, view=view)
        
    @commands.Cog.listener()
    async def on_ready(self):
        # register views so they still work after bot restart
        self.bot.add_view(TicketCreateButton())
        self.bot.add_view(TicketCloseButton())

async def setup(bot):
    await bot.add_cog(Tickets(bot))
