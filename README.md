# Discord Server Setup Bot for krtrim

This Python script uses the `discord.py` library to automatically set up a Discord server with a predefined structure of categories, channels, roles, and permissions. It's designed to create a professional and organized server for the "krtrim" community.

## Features

- **Automated Server Setup:** Creates categories, text channels, and voice channels based on a predefined structure.
- **Role Management:** Creates a set of roles with specific names, colors, and permissions.
- **Permission Control:** Sets up channel-specific permissions for roles, including private staff channels.
- **Welcome & Onboarding:** Posts welcome messages and instructions in designated channels.
- **Reaction Roles:** Allows users to self-assign roles by reacting to a message in the `#start-here` channel.
- **Themed Design:** Uses a consistent black and orange theme for embeds and roles.
- **Safe & Idempotent:** The script is designed to be run multiple times without causing issues. It checks for existing roles and channels.

## Prerequisites

- Python 3.8 or higher
- A Discord Account

## Setup and Usage

### 1. Create your Discord Server
- In your Discord client, click the `+` icon in the server list.
- Select "Create My Own" -> "For a club or community".
- Give it a name (e.g., "krtrim") and click "Create".

### 2. Enable Developer Mode
- Go to User Settings > Advanced.
- Toggle on "Developer Mode".
- Right-click on your newly created server's icon and select "Copy Server ID".

### 3. Create a Discord Bot Application
- Go to the [Discord Developer Portal](https://discord.com/developers/applications).
- Click "New Application", give it a name (e.g., "krtrim-setup-bot"), and click "Create".
- In the left sidebar, go to the "Bot" tab.
- Click "Add Bot", then "Yes, do it!".
- Click "Reset Token" and copy the token. **Treat this like a password and do not share it.**

### 4. Invite the Bot to Your Server
- In the Developer Portal, go to OAuth2 > URL Generator.
- Under "Scopes", select `bot`.
- Under "Bot Permissions", select `Administrator`.
- Copy the generated URL, paste it into your browser, select your server, and click "Authorize".

### 5. Configure and Run the Script
1.  **Clone the repository:**
    ```bash
    git clone https://github.com/YOUR-USERNAME/krtrim-discord-bot.git
    cd krtrim-discord-bot
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Set Environment Variables:**
    Before running, you need to provide the bot token and server ID to the script. It is best practice to use environment variables.

    **On macOS/Linux:**
    ```bash
    export DISCORD_BOT_TOKEN="YOUR_BOT_TOKEN_HERE"
    export DISCORD_GUILD_ID="YOUR_SERVER_ID_HERE"
    ```

    **On Windows (PowerShell):**
    ```powershell
    $env:DISCORD_BOT_TOKEN="YOUR_BOT_TOKEN_HERE"
    $env:DISCORD_GUILD_ID="YOUR_SERVER_ID_HERE"
    ```
    
    Alternatively, if you choose not to use environment variables, you can hardcode these values directly into the `krtrim-discord-bot.py` file. **This is not recommended for security reasons.**
    
    Edit these lines at the top of `krtrim-discord-bot.py`:
    ```python
    # Use env vars instead of hardcoding
    YOUR_BOT_TOKEN = "PASTE_YOUR_TOKEN_HERE"  # set this in your shell
    YOUR_GUILD_ID = 123456789012345678   # set this in your shell
    ```

4.  **Run the bot:**
    ```bash
    python krtrim-discord-bot.py
    ```

## ⚠️ Important: What This Script Does
- **Deletes existing channels and roles:** This script is designed for a fresh server and will delete all channels (except 'general') and roles before starting.
- **Creates a full server structure:** It builds the categories, channels, and roles defined in the script.
- **Sets up reaction roles:** Configures a message in `#start-here` for self-assigning roles.

**Run this script only on a server that you own or have full control over.**

## 🔧 Troubleshooting
- **Bot offline?** Double-check that your `DISCORD_BOT_TOKEN` is correct and has no extra spaces.
- **Permissions errors?** Ensure the bot was invited with `Administrator` permissions and that its role is high up in your server's role hierarchy.
- **"Guild not found"?** Make sure the `DISCORD_GUILD_ID` is correct.
- **Reactions not working?** Go to your bot's page in the Discord Developer Portal, click the "Bot" tab, and ensure the "Message Content Intent" is enabled.

## Configuration
The script is configured through several Python variables at the top of the `krtrim-discord-bot.py` file:
- `YOUR_BOT_TOKEN`: Your Discord bot's secret token.
- `YOUR_GUILD_ID`: The ID of the Discord server you want to set up.
- `ROLE_NAMES`: A list of role names to be created.
- `CHANNEL_STRUCTURE`: A dictionary defining the categories and the text channels within them.
- `VOICE_CHANNELS`: A dictionary defining the voice channels and their categories.
- `ROLE_COLOR_MAP`: A mapping of role names to their hex color codes.
- `ROLE_HIERARCHY_ORDER`: The desired order of roles in the server's role list.
- `CHANNEL_WELCOMES`: A dictionary containing the welcome messages and topics for specific channels.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any bugs or feature requests.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
