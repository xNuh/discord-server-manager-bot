import discord
from discord.ext import commands
import os
import json
from dotenv import load_dotenv

# load dotenv for token
load_dotenv()

class MyBot(commands.Bot):
    def __init__(self):
        # enable intents or nothing will work
        intents = discord.Intents.default()
        intents.message_content = True
        intents.members = True
        
        super().__init__(command_prefix="!", intents=intents, help_command=None)

    async def setup_hook(self):
        # load all cogs from the folder
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                await self.load_extension(f'cogs.{filename[:-3]}')
                print(f"Loaded {filename}")
        
        # sync slash commands
        await self.tree.sync()
        print("Slash commands synced!")

bot = MyBot()

@bot.event
async def on_ready():
    print(f"Bot is online as {bot.user.name}")
    print("Ready to go!")
    await bot.change_presence(activity=discord.Game(name="Server Manager | /help"))

if __name__ == '__main__':
    token = os.getenv("DISCORD_TOKEN")
    if not token:
        print("NO TOKEN FOUND! Please check .env")
    else:
        bot.run(token)
