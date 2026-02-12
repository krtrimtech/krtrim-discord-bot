import os
import asyncio
import discord
from discord.ext import commands

# =========================
# CONFIG
# =========================

# Load credentials from environment variables if they exist.
# This is the recommended and most secure method.
# If not found, it falls back to the hardcoded values below.
# YOUR_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN", "")
# YOUR_SERVER_ID = os.getenv("DISCORD_SERVER_ID")

# If you are not using environment variables, **uncomment and fill in the lines below**.
# This is **not recommended** for security reasons.
YOUR_BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"
YOUR_SERVER_ID = 1234567890123456789 # Replace with your actual server ID (as an integer)

# Convert Guild ID to integer
try:
    YOUR_SERVER_ID = int(YOUR_SERVER_ID)
except (ValueError, TypeError):
    YOUR_SERVER_ID = None

ORANGE = 0xFF6200
BLACK = 0x1E1B1B
DARK_ORANGE = 0xFF8C42

# Keep your original role names so reaction-role onboarding still works
ROLE_NAMES = [
    "👑 Owner", "⚙️ Co-Admin", "🛡️ Moderator", "🎯 Event Manager",
    "📚 Course Mentor", "🔧 Tool Curator", "💻 Developer",
    "🎨 Designer", "✨ Animator", "✅ Verified", "👥 Member", "🔇 Muted"
]

CHANNEL_STRUCTURE = {
    "🚀 WELCOME": ["📋start-here", "📜rules", "📢announcements", "👋introductions"],
    "🧠 AI TOOLS": ["🔥free-tools", "☁️free-hosting", "🎓free-courses", "⚙️workflows", "⚡playground"],
    "📚 ACADEMY": ["📺youtube", "📝notes", "❓qna"],
    "💬 CHAT": ["🌐general", "🚀progress", "🤝networking"],
    "💼 PROJECTS": ["📂showcase", "💾github", "👥teams"],
    "🎯 EVENTS": ["📅calendar", "🥇weekly", "🏆monthly", "⚡hackathon"],
    "📢 PROMOTE": ["📺youtube-ads", "📦assets"],
    "🎨 CREATIVE": ["🖌️designs", "🎬animation", "🎯requests"],
    "🎉 LOUNGE": ["🎂personal"],
    "🔒 STAFF": ["🛡️modlog", "📋tickets", "⚠️reports"],
}

VOICE_CHANNELS = {
    "🎯 EVENTS": ["🔴 Event Stage", "🗣️ Live Voice"],
    "📚 ACADEMY": ["👨🏫 Lecture Hall", "🎤 Stage Talk"],
    "🎉 LOUNGE": ["😌 Chill Zone", "🎧 Music Lounge"],
}

# =========================
# OPTIONAL: Role colors/permissions phase (adapted safely)
# - We map your existing role names to colors/perms without renaming them.
# =========================

ENABLE_ROLE_POPULATE_PHASE = True

ROLE_COLOR_MAP = {
    "👑 Owner": ORANGE,
    "⚙️ Co-Admin": ORANGE,
    "🛡️ Moderator": 0x5865F2,
    "🎯 Event Manager": 0x00D2FF,
    "📚 Course Mentor": 0xFAF0E6,
    "🔧 Tool Curator": 0x9C84EF,
    "💻 Developer": 0xFEE75C,
    "🎨 Designer": 0xED4245,
    "✨ Animator": 0xF47DDD,
    "✅ Verified": 0x57F287,
    "👥 Member": BLACK,
    "🔇 Muted": 0x808080,
}

ROLE_HIERARCHY_ORDER = [
    "👑 Owner",
    "⚙️ Co-Admin",
    "🛡️ Moderator",
    "🎯 Event Manager",
    "📚 Course Mentor",
    "🔧 Tool Curator",
    "✅ Verified",
    "💻 Developer",
    "🎨 Designer",
    "✨ Animator",
    "🔇 Muted",
    # "👥 Member" is @everyone and is handled via guild.default_role
]

# =========================
# BOT INIT (fixed: only once)
# =========================

# IMPORTANT: You MUST go to your bot's page on the Discord Developer Portal
# (https://discord.com/developers/applications/), click on your bot, go to the "Bot"
# tab, and enable the "SERVER MEMBERS INTENT" toggle. This is required for the
# reaction-based role assignment to work.
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="!", intents=intents)

# 🖤 BLACK/ORANGE THEMED WELCOME MESSAGES
CHANNEL_WELCOMES = {
    "📋start-here": {
        "topic": "🎉 React to get roles & unlock channels! | 💻🎨✨📚✅",
        "embed": {
            "title": "🧠 krtrim AI Community",
            "description": "**Select your role to unlock channels:**\n\n💻 **Developer** - Projects & GitHub\n🎨 **Designer** - Creative showcase\n✨ **Animator** - Motion graphics\n📚 **Mentor** - Courses & lectures\n✅ **Verified** - Full access",
            "color": 0xFF6200
        }
    },
    "📜rules": {
        "topic": "📜 Server Rules - Read before chatting! ✅",
        "embed": {
            "title": "📜 krtrim AI Community Rules",
            "description": "1. **No spam** - Keep channels on-topic\n2. **English only** in main channels\n3. **Self-promo** → #📺youtube-ads only\n4. **No toxicity** - Be respectful\n5. **No illegal content**",
            "color": 0xFF6200
        }
    },
    "🔥free-tools": {
        "topic": "🔥 Free AI Tools, APIs, Resources | Share + upvote!",
        "embed": {
            "title": "🔥 FREE AI TOOLS",
            "description": "**Drop your favorite:**\n• Free AI APIs\n• Open-source tools\n• No-signup playgrounds\n• Budget hosting\n\n`Format: **Tool Name** | [link] | description`",
            "color": 0xFF6200
        }
    },
    "☁️free-hosting": {
        "topic": "☁️ Free Hosting: Vercel, Render, Railway, Fly.io",
        "embed": {
            "title": "☁️ FREE HOSTING",
            "description": "**Tier lists:**\n`Tier S: Vercel, Render`\n`Tier A: Railway, Fly.io`\n\n**Share your setups!** 🚀",
            "color": 0xFF6200
        }
    },
    "🎓free-courses": {
        "topic": "🎓 Free Courses: Udemy, Coursera, YouTube, fast.ai",
        "embed": {
            "title": "🎓 FREE COURSES",
            "description": "**Drop links:**\n• AI/ML courses\n• Coding bootcamps\n• No-signup certificates\n\n`**[Course]** | [link] | 🎓 Level: Beginner/Intermediate/Advanced`",
            "color": 0xFF6200
        }
    },
    "⚙️workflows": {
        "topic": "⚙️ n8n, Make.com, Zapier workflows | Copy-paste ready",
        "embed": {
            "title": "⚙️ AI WORKFLOWS",
            "description": "**Share your automations:**\n• n8n JSON exports\n• Make.com templates\n• Zapier clones\n\n`Paste → Test → Share results!`",
            "color": 0xFF6200
        }
    },
    "📺youtube": {
        "topic": "📺 AI YouTube: 3Blue1Brown, Sentdex, Two Minute Papers",
        "embed": {
            "title": "📺 AI YOUTUBE",
            "description": "**Latest bangers:**\n• Algorithm visuals\n• Tool tutorials\n• Research breakdowns\n\n`Drop timestamped gems! ⏰`",
            "color": 0xFF6200
        }
    },
    "🌐general": {
        "topic": "🌐 General AI chat | Memes, news, hot takes",
        "embed": {
            "title": "🌐 GENERAL CHAT",
            "description": "**What's trending in AI today?**\n• New models\n• Tool releases\n• Hot takes\n\n`Keep it chill & on-topic! 😎`",
            "color": 0xFF6200
        }
    },
    "📺youtube-ads": {
        "topic": "📺 Self-promo: Your AI YouTube | 1 link per week",
        "embed": {
            "title": "📺 PROMOTE YOUR YOUTUBE",
            "description": "**Format:**\n`[**Channel Name**] | [link] | Latest video + why watch`\n\n`Verified creators get priority! ✅` **(1/week)**",
            "color": 0xFF6200
        }
    },
    "📂showcase": {
        "topic": "💼 Project showcase | Live demos + screenshots",
        "embed": {
            "title": "💼 PROJECT SHOWCASE",
            "description": "**Drop your work:**\n• Live demos\n• Screenshots\n• GitHub links\n• Tech stack\n\n`Format: **Project** | [link/demo] | **Made with:**`",
            "color": 0xFF6200
        }
    },
    "💾github": {
        "topic": "💾 GitHub drops | Open-source AI projects",
        "embed": {
            "title": "💾 GITHUB DROPS",
            "description": "**Share repos:**\n• AI tools\n• Automation scripts\n• ML models\n• Cool libraries\n\n`**Repo** | ⭐ Stars | What it does`",
            "color": 0xFF6200
        }
    },
    "👥teams": {
        "topic": "👥 Team building | Hackathons + collabs",
        "embed": {
            "title": "👥 TEAM BUILDING",
            "description": "**Looking for:**\n• Frontend devs\n• AI specialists\n• Designers\n• Hackathon teams\n\n`**[Role]** | Project idea | DM to join`",
            "color": 0xFF6200
        }
    }
}

ORANGE = 0xFF6200

async def safe_get_guild() -> discord.Guild:
    guild = bot.get_guild(YOUR_SERVER_ID)
    if guild is None:
        raise RuntimeError("Guild not found. Check DISCORD_GUILD_ID and that the bot is in the server.")
    return guild


async def clean_slate_keep_general(guild: discord.Guild):
    # same intent as your original: delete everything except 'general'
    for channel in list(guild.channels):
        if isinstance(channel, (discord.TextChannel, discord.VoiceChannel)) and channel.name != "general":
            try:
                await channel.delete()
            except discord.Forbidden:
                pass
            await asyncio.sleep(0.2)


async def create_base_roles(guild: discord.Guild) -> dict:
    print("Checking and creating roles...")
    roles = {}
    for role_name in ROLE_NAMES:
        existing_role = discord.utils.get(guild.roles, name=role_name)
        if existing_role:
            print(f"✅ Role '{role_name}' already exists. Skipping creation.")
            roles[role_name] = existing_role
        else:
            print(f"✨ Creating role '{role_name}'...")
            color = ORANGE if "Owner" in role_name else BLACK
            try:
                role = await guild.create_role(
                    name=role_name,
                    color=color,
                    hoist=True,
                    mentionable=False
                )
                roles[role_name] = role
                await asyncio.sleep(0.3)
            except discord.Forbidden:
                print(f"❌ No permission to create role '{role_name}'. Skipping.")

    # Rename @everyone to Member if not already done
    if guild.default_role.name != "👥 Member":
        try:
            print("✨ Renaming @everyone role to '👥 Member'...")
            await guild.default_role.edit(name="👥 Member", color=BLACK)
        except discord.Forbidden:
            print("❌ No permission to rename @everyone role. Skipping.")
    else:
        print("✅ @everyone role is already named '👥 Member'. Skipping.")


    return roles


async def create_categories_and_channels(guild: discord.Guild, roles: dict):
    print("Checking and creating categories and text channels...")
    for cat_name, channels in CHANNEL_STRUCTURE.items():
        existing_category = discord.utils.get(guild.categories, name=cat_name)
        
        if existing_category:
            print(f"✅ Category '{cat_name}' already exists. Checking channels inside.")
            category = existing_category
        else:
            print(f"✨ Creating category '{cat_name}'...")
            overwrites_for_category = {
                guild.default_role: discord.PermissionOverwrite(read_messages=True)
            }
            try:
                category = await guild.create_category(cat_name, overwrites=overwrites_for_category)
            except discord.Forbidden:
                print(f"❌ No permission to create category '{cat_name}'. Skipping.")
                continue
        
        for ch_name in channels:
            existing_channel = discord.utils.get(category.text_channels, name=ch_name)
            if existing_channel:
                print(f"✅ Text channel '{ch_name}' in '{cat_name}' already exists. Skipping.")
                continue

            print(f"✨ Creating text channel '{ch_name}' in '{cat_name}'...")
            overwrites = {
                guild.default_role: discord.PermissionOverwrite(read_messages=True, send_messages=True),
            }

            muted = roles.get("🔇 Muted") or discord.utils.get(guild.roles, name="🔇 Muted")
            moderator = roles.get("🛡️ Moderator") or discord.utils.get(guild.roles, name="🛡️ Moderator")

            if muted:
                overwrites[muted] = discord.PermissionOverwrite(send_messages=False)
            if moderator:
                overwrites[moderator] = discord.PermissionOverwrite(manage_messages=True, kick_members=True)

            if any(x in cat_name.lower() for x in ["staff", "🔒"]):
                overwrites[guild.default_role] = discord.PermissionOverwrite(read_messages=False)
                if moderator:
                    overwrites[moderator] = discord.PermissionOverwrite(read_messages=True)
            
            try:
                await category.create_text_channel(ch_name, overwrites=overwrites)
                await asyncio.sleep(0.2)
            except discord.Forbidden:
                print(f"❌ No permission to create channel '{ch_name}' in '{cat_name}'. Skipping.")


async def create_voice_channels(guild: discord.Guild):
    print("Checking and creating voice channels...")
    for cat_name, voices in VOICE_CHANNELS.items():
        category = discord.utils.get(guild.categories, name=cat_name)
        if not category:
            print(f"⚠️ Category '{cat_name}' not found for voice channels. Skipping.")
            continue
            
        for voice_name in voices:
            existing_channel = discord.utils.get(category.voice_channels, name=voice_name)
            if existing_channel:
                print(f"✅ Voice channel '{voice_name}' in '{cat_name}' already exists. Skipping.")
            else:
                print(f"✨ Creating voice channel '{voice_name}' in '{cat_name}'...")
                try:
                    await category.create_voice_channel(voice_name)
                    await asyncio.sleep(0.1)
                except discord.Forbidden:
                    print(f"❌ No permission to create voice channel '{voice_name}' in '{cat_name}'. Skipping.")


async def post_onboarding_embeds(guild: discord.Guild):
    print("Checking and posting onboarding messages...")
    # --- Onboarding Roles Message ---
    start_channel = discord.utils.get(guild.text_channels, name="📋start-here")
    if start_channel:
        has_posted = False
        try:
            async for msg in start_channel.history(limit=50):
                if msg.author == bot.user and msg.embeds and msg.embeds[0].title == "🧠 krtrim AI Community":
                    print("✅ Onboarding roles message in '#start-here' already exists. Skipping.")
                    has_posted = True
                    break
        except discord.Forbidden:
            print("❌ No permission to read '#start-here' history. Cannot check for existing messages.")
            has_posted = True # Assume it's posted to avoid duplicates
        
        if not has_posted:
            print("✨ Posting onboarding roles message in '#start-here'...")
            embed = discord.Embed(
                title="🧠 krtrim AI Community",
                description=(
                    "**Select your role to unlock channels:**\n\n"
                    "💻 **Developer** - Projects & GitHub\n"
                    "🎨 **Designer** - Creative showcase\n"
                    "✨ **Animator** - Motion graphics\n"
                    "📚 **Mentor** - Courses & lectures\n"
                    "✅ **Verified** - Full access"
                ),
                color=ORANGE,
            )
            embed.set_thumbnail(url="https://i.imgur.com/ai-brain.gif")
            embed.set_footer(text="krtrim • Black/Orange Edition", icon_url="https://i.imgur.com/logo.png")
            try:
                msg = await start_channel.send(embed=embed)
                reactions = ["💻", "🎨", "✨", "📚", "✅"]
                for emoji in reactions:
                    await msg.add_reaction(emoji)
            except discord.Forbidden:
                print("❌ No permission to post in '#start-here'. Skipping.")

    # --- Rules Message ---
    rules_ch = discord.utils.get(guild.text_channels, name="📜rules")
    if rules_ch:
        has_posted_rules = False
        try:
            async for msg in rules_ch.history(limit=10):
                if msg.author == bot.user and msg.embeds and msg.embeds[0].title == "📜 Server Rules":
                    print("✅ Rules message in '#rules' already exists. Skipping.")
                    has_posted_rules = True
                    break
        except discord.Forbidden:
            print("❌ No permission to read '#rules' history. Cannot check for existing messages.")
            has_posted_rules = True # Assume it's posted to avoid duplicates

        if not has_posted_rules:
            print("✨ Posting rules message in '#rules'...")
            rules_embed = discord.Embed(
                title="📜 Server Rules",
                description=(
                    "1. **No spam** - Keep channels on-topic\n"
                    "2. **Respect everyone** - No toxicity\n"
                    "3. **Self-promo** in designated channels only\n"
                    "4. **English** for main channels\n"
                    "5. **No illegal content**"
                ),
                color=ORANGE,
            )
            try:
                await rules_ch.send(embed=rules_embed)
            except discord.Forbidden:
                print("❌ No permission to post in '#rules'. Skipping.")


async def populate_roles_permissions_and_hierarchy(guild: discord.Guild):
    # Only touches roles that already exist (won't rename/delete your structure)
    roles = {r.name: r for r in guild.roles}

    # Ensure colors/hoist/mentionable
    for name, color in ROLE_COLOR_MAP.items():
        role = roles.get(name)
        if not role:
            continue
        try:
            await role.edit(color=color, hoist=True, mentionable=False)
        except discord.Forbidden:
            pass
        await asyncio.sleep(0.2)

    # @everyone visuals
    try:
        await guild.default_role.edit(name="👥 Member", color=ROLE_COLOR_MAP["👥 Member"])
    except discord.Forbidden:
        pass

    # Permissions (safe: assigns only if role exists)
    owner = roles.get("👑 Owner")
    coadmin = roles.get("⚙️ Co-Admin")
    moderator = roles.get("🛡️ Moderator")
    muted = roles.get("🔇 Muted")

    if owner:
        try:
            await owner.edit(permissions=discord.Permissions.all())
        except discord.Forbidden:
            pass

    if coadmin:
        try:
            await coadmin.edit(permissions=discord.Permissions.all())
        except discord.Forbidden:
            pass

    if moderator:
        mod_perms = discord.Permissions()
        mod_perms.manage_messages = True
        mod_perms.kick_members = True
        mod_perms.moderate_members = True
        mod_perms.manage_nicknames = True
        try:
            await moderator.edit(permissions=mod_perms)
        except discord.Forbidden:
            pass

    # Muted: keep view_channel true like your second file’s intention
    if muted:
        muted_perms = discord.Permissions.none()
        muted_perms.view_channel = True
        try:
            await muted.edit(permissions=muted_perms)
        except discord.Forbidden:
            pass

    # Hierarchy ordering (only among roles present)
    positions = {}
    usable = [name for name in ROLE_HIERARCHY_ORDER if name in roles]
    bot_top_role = guild.me.top_role
    for i, role_name in enumerate(usable):
        role = roles[role_name]
        if role >= bot_top_role:
            print(f"⚠️ Cannot reorder role '{role.name}' because it is higher than or equal to the bot's role.")
            continue
        positions[role] = len(guild.roles) - 2 - i

    if positions:
        print("✨ Attempting to reorder roles...")
        try:
            await guild.edit_role_positions(positions=positions)
            print("✅ Roles reordered successfully.")
        except discord.HTTPException as e:
            if e.code == 50013: # Missing Permissions
                print("❌ No permission to reorder roles. Please move the bot's role higher in the server settings for this to work.")
            else:
                print(f"❌ An HTTP error occurred while reordering roles: {e}")
        except Exception as e:
            print(f"❌ An unexpected error occurred while reordering roles: {e}")


@bot.event
async def on_ready():
    if not YOUR_BOT_TOKEN or not YOUR_SERVER_ID:
        raise RuntimeError("Configuration error: DISCORD_BOT_TOKEN and DISCORD_SERVER_ID must be set either as environment variables or directly in the script.")

    guild = await safe_get_guild()
    print(f"🎨 Setting up krtrim PRO - {guild.name}...")

    await clean_slate_keep_general(guild) # This is disabled to prevent deleting existing channels.
    roles = await create_base_roles(guild)
    await create_categories_and_channels(guild, roles)
    await create_voice_channels(guild)
    await post_onboarding_embeds(guild)

    if ENABLE_ROLE_POPULATE_PHASE:
        await populate_roles_permissions_and_hierarchy(guild)
    print(f"🖤🧡 Populating {guild.name} channels with welcome messages...")
    
    count = 0
    for category in guild.categories:
        for channel in category.text_channels:
            if channel.name in CHANNEL_WELCOMES:
                try:
                    # Check if message already exists
                    has_message = False
                    try:
                        async for msg in channel.history(limit=5):
                            if msg.author == bot.user and msg.embeds and msg.embeds[0].title == CHANNEL_WELCOMES[channel.name]["embed"]["title"]:
                                print(f"✅ Welcome message in '{channel.name}' already exists. Skipping.")
                                has_message = True
                                break
                    except discord.Forbidden:
                        print(f"❌ No permission to read '{channel.name}' history. Cannot check for existing messages.")
                        has_message = True # Assume it's populated to avoid duplicates
                    
                    if has_message:
                        continue

                    print(f"✨ Posting welcome message in '{channel.name}'...")
                    welcome = CHANNEL_WELCOMES[channel.name]
                    
                    # Set topic
                    await channel.edit(topic=welcome["topic"])
                    
                    # Send styled embed
                    embed = discord.Embed(
                        title=welcome["embed"]["title"],
                        description=welcome["embed"]["description"],
                        color=welcome["embed"]["color"]
                    )
                    embed.set_footer(text="krtrim AI Community 🖤🧡")
                    await channel.send(embed=embed)
                    
                    count += 1
                    await asyncio.sleep(1)  # Rate limit
                    
                except Exception as e:
                    print(f"❌ Failed to populate channel '{channel.name}': {e}")
    
    print(f"🎉 COMPLETED! {count} channels populated with pro messages 🖤🧡")
    print("✅ krtrim PRO setup complete! 🎨🖤")
    print("🎨 Next: Set server icon + enable Community features")

    print("\\n🎉 Setup script finished!")
    print("Bot is shutting down...")
    await bot.close()


@bot.event
async def on_raw_reaction_add(payload: discord.RawReactionActionEvent):
    if payload.user_id == bot.user.id:
        return

    guild = bot.get_guild(payload.guild_id)
    if not guild:
        return

    channel = guild.get_channel(payload.channel_id)
    if channel and channel.name != "📋start-here":
        return

    role_map = {
        "💻": "💻 Developer",
        "🎨": "🎨 Designer",
        "✨": "✨ Animator",
        "📚": "📚 Course Mentor",
        "✅": "✅ Verified",
    }

    role_name = role_map.get(str(payload.emoji))
    if not role_name:
        return

    role = discord.utils.get(guild.roles, name=role_name)
    member = guild.get_member(payload.user_id)
    if role and member:
        try:
            await member.add_roles(role)
        except discord.Forbidden:
            pass


bot.run(YOUR_BOT_TOKEN)
