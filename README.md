# 🤖 krtrim Discord Server Setup Bot 🤖

<p align="center">
  <img src="https://img.shields.io/badge/python-3.8%2B-blue?style=for-the-badge&logo=python" alt="Python 3.8+">
  <img src="https://img.shields.io/badge/discord.py-v2.6.4-blue?style=for-the-badge&logo=discord" alt="discord.py">
  <img src="https://img.shields.io/badge/license-MIT-green?style=for-the-badge" alt="License: MIT">
</p>

Ever wanted to build a professional Discord server from scratch with just one command? Tired of clicking through menus to create channels and roles? **Say no more!**

This bot is your personal server-building sidekick. It takes a boring, empty server and transforms it into a fully-featured, organized, and themed community hub for **krtrim**. It's like a server blueprint in a bottle! 🚀

---

## ✨ Features Dropping In!

*   **💥 Automated Server Nuke & Build:** Deletes old channels and roles (you've been warned!) and builds a fresh, new server structure.
*   **🎨 Role Variety Pack:** Creates a full set of roles with custom colors and permissions, from `👑 Owner` to `💻 Developer`.
*   **🚦 Permission Perfect:** Automatically sets up channel permissions. Your staff channels are secret, and your public channels are... well, public!
*   **👋 Welcome Party:** Posts slick, embedded welcome messages and rules to get new members started.
*   **✅ Reaction Roles:** Lets users grab their own roles by reacting to a message in `#start-here`. It's self-service for server roles!
*   **🧡 Black & Orange Everything:** A cool, consistent theme for embeds and roles to keep things looking sharp.

---

## 🚀 Level 1: The Setup Quest

Your quest, should you choose to accept it, is to get this bot running. Here are your objectives:

### 🎯 Objective 1: Create Your Server
1.  In your Discord app, hit the `+` icon on the server list.
2.  Choose **"Create My Own"** -> **"For a club or community"**.
3.  Name it something cool (like "krtrim") and click **"Create"**.

### 🎯 Objective 2: Activate Developer Mode & Get Your Server ID
1.  Go to **User Settings** > **Advanced**.
2.  Flick the **"Developer Mode"** switch to ON. It's like enabling cheat codes!
3.  Right-click your new server's icon and **"Copy Server ID"**. Keep it handy!

### 🎯 Objective 3: Summon Your Bot
1.  Head to the [Discord Developer Portal](https://discord.com/developers/applications).
2.  Click **"New Application"**, name it "krtrim-setup-bot", and hit **"Create"**.
3.  Go to the **"Bot"** tab on the left.
4.  Click **"Reset Token"** and **COPY THE TOKEN**.
    > **⚠️ IMPORTANT:** This token is super-secret! Treat it like your password. Don't share it with anyone! and enable the **Presence Intent**, **"SERVER MEMBERS INTENT"** and **Message Content Intent**.
5.  Click **"Add Bot"**, then **"Yes, do it!"**. Your bot is born!

### 🎯 Objective 4: Invite Your Bot to the Party
1.  In the Developer Portal, go to **OAuth2 > URL Generator**.
2.  Under "Scopes", check the `bot` box.
3.  Under "Bot Permissions", check `Administrator`. Your bot needs OP privileges for this mission.
4.  Copy the generated URL, paste it into your browser, select your server, and click **"Authorize"**. *Poof!* Your bot has joined the server.

### 🎯 Objective 5: Configure & LAUNCH!
1.  **Clone the repo:**
    ```bash
    git clone https://github.com/krtrimtech/krtrim-discord-bot.git
    cd krtrim-discord-bot
    ```

2.  **Install the necessary spells (dependencies):**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Give the bot its credentials (Environment Variables):**
    This is the safest way to tell the bot its token and server ID.

    **On macOS/Linux:**
    ```bash
    export DISCORD_BOT_TOKEN="YOUR_BOT_TOKEN_HERE"
    export YOUR_SERVER_ID="YOUR_SERVER_ID_HERE"
    ```

    **On Windows (PowerShell):**
    ```powershell
    $env:DISCORD_BOT_TOKEN="YOUR_BOT_TOKEN_HERE"
    $env:YOUR_SERVER_ID="YOUR_SERVER_ID_HERE"
    ```
    > *(Psst... if you're feeling risky, you can hardcode these in the `.py` file, but we don't recommend it!)*

4.  **Press the big red button (run the script):**
    ```bash
    python krtrim-discord-bot.py
    ```

**🎉 CONGRATULATIONS! You've completed the setup quest! Your server is now a masterpiece. 🎉**

---

## 🚨 WARNING ZONE 🚨

*   **This script is DESTRUCTIVE!** It's designed for a fresh server. It will **DELETE** all existing channels (except 'general') and roles before it starts building.
*   **Use it on servers you own.** Don't be that person who nukes a server you don't control. Seriously.

---

## 🐜 Bug Hunting & Troubleshooting

Running into issues? Don't rage-quit! Here are some common fixes:

-   **"Bot is offline!"**: Did you copy the `DISCORD_BOT_TOKEN` correctly? No extra spaces!
-   **"Permissions? What permissions?"**: Make sure you invited the bot with `Administrator` checked. Also, check that its role is at the top of your server's role list.
-   **"Guild not found"**: Your `DISCORD_GUILD_ID` might be wrong. It's a long number—double-check it!
-   **"Reactions aren't working!"**: You might need to enable the "Message Content Intent" for your bot. Go to your bot's page in the Developer Portal, click the "Bot" tab, and toggle it on.

---

## 🤝 Contributing

Got an idea to make this bot even more awesome? Found a bug? Feel free to open an issue or submit a pull request. All contributions are welcome!

## 📜 License

This project is under the MIT License. Check out the `LICENSE` file for the full legal-speak.