import discord
from discord.ext import commands
from datetime import datetime

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

# CONFIGURATION
NOTIFICATION_CHANNEL_ID = 1333930323544899585
VOICE_NOTIFIER_ROLE_ID = 1333932112830664726  # Replace with your actual role ID

@bot.event
async def on_ready():
    print(f'✅ Bot {bot.user.name} is online!')

@bot.event
async def on_voice_state_update(member, before, after):
    # Only trigger for voice channel joins
    if before.channel is None and after.channel is not None:
        channel = bot.get_channel(NOTIFICATION_CHANNEL_ID)
        
        # Create embed
        embed = discord.Embed(
            title="🎤 Voice Channel Activity",
            description=f"{member.mention} joined **{after.channel.name}**!",
            color=0x00ff00  # Green color
        )
        embed.set_thumbnail(url=member.avatar.url)
        embed.add_field(name="Channel", value=after.channel.mention)
        embed.add_field(name="Joined", value=f"<t:{int(datetime.now().timestamp())}:R>")
        
        # Send notification with role ping
        await channel.send(
            f"<@&{VOICE_NOTIFIER_ROLE_ID}>",  # Role mention
            embed=embed
        )
        
        # Add reaction to the notification message
        message = await channel.fetch_message(channel.last_message_id)
        await message.add_reaction("👋")

bot.run('MTMzMzkyODgxNDkyMDYwMTY2MA.GgydT9.sJI1H7l-c4Yy651BBjF0LyJo0KQUQH6-2WmKVo')  # Replace with your actual token