import discord
from discord.ext import commands
from datetime import datetime, timedelta

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

# CONFIGURATION
NOTIFICATION_CHANNEL_ID = 1333930323544899585
VOICE_NOTIFIER_ROLE_ID = 1333932112830664726  # Replace with your actual role ID

# Cooldown tracking
last_join_time = {}

@bot.event
async def on_ready():
    print(f'✅ Bot {bot.user.name} is online!')

@bot.event
async def on_voice_state_update(member, before, after):
    # Only trigger when a user joins a voice channel (not switching or leaving)
    if before.channel is None and after.channel is not None:
        # Check if the user has the specified role
        role = discord.utils.get(member.roles, id=VOICE_NOTIFIER_ROLE_ID)
        if not role:
            return  # User doesn't have the role, ignore

        # Check cooldown (1 minute)
        now = datetime.utcnow()
        if member.id in last_join_time and now - last_join_time[member.id] < timedelta(minutes=1):
            return  # Cooldown active, ignore

        # Update last join time
        last_join_time[member.id] = now

        # Send notification
        channel = bot.get_channel(NOTIFICATION_CHANNEL_ID)
        embed = discord.Embed(
            title="🎤 Voice Channel Activity",
            description=f"{member.mention} joined **{after.channel.name}**!",
            color=0x00ff00  # Green color
        )
        embed.set_thumbnail(url=member.avatar.url)
        embed.add_field(name="Channel", value=after.channel.mention)
        embed.add_field(name="Joined", value=f"<t:{int(now.timestamp())}:R>")

        # Send notification with role mention
        message = await channel.send(f"<@&{VOICE_NOTIFIER_ROLE_ID}>", embed=embed)

        # Add reaction to the notification message
        await message.add_reaction("👋")

bot.run('')  # Replace with your actual token
