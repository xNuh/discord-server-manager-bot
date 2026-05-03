# My Discord Server Manager Bot

Hey! This is my own Discord bot that I wrote in Python using `discord.py`. I built it to manage my server a bit better and because I wanted to learn more about programming.

## 🚀 Features
- **Ticket System**: Users can open tickets via a button, and a private channel is created.
- **Moderation**: Commands like `/ban`, `/timeout`, `/warn`, and `/clear` to get rid of trolls.
- **Logs**: When someone deletes or edits a message or joins/leaves, it's logged directly into a log channel.
- **Welcome System**: New users are greeted with a cool embed.
- **Setup Commands**: Everything can be configured directly via Discord (Log channel, Welcome channel, roles, etc.).

## 🛠️ Installation & Setup

1. Download Python (version 3.10 or newer)
2. Clone the repo or download the files
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Rename the `.env.example` file to `.env` and enter your Discord bot token. You can get it from the [Discord Developer Portal](https://discord.com/developers/applications).
5. Start the bot!
   ```bash
   python main.py
   ```

## 💻 Commands
Most things run via slash commands (`/`).
- `/setup ...` (Admin only to set channels, e.g., `/setup logchannel`)
- `/ticket_panel` (Sends the message with the ticket button)
- `/ban`, `/timeout`, `/warn`, `/clear` (Standard mod commands)

## 💡 It is working?
It's not completely perfect, but it works really well and was a lot of fun to make! If you find any bugs, feel free to let me know.
