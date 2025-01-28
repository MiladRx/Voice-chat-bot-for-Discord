# Voice Channel Notification Bot

This is a **Discord bot** that notifies a designated channel whenever a user joins a voice channel. It also pings a specific role and reacts to the notification message.

## Features
- Sends a notification when a user joins a voice channel.
- Uses an embedded message format.
- Mentions a specific role upon voice join.
- Adds a reaction to the notification message.

## Installation

### 1. Clone the Repository
```bash
git clone <repository-url>
cd <repository-folder>
```

### 2. Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Setup the Environment Variables
Create a `.env` file in the root directory and add your bot token:
```env
DISCORD_TOKEN=your-bot-token-here
```

### 5. Run the Bot
```bash
python bot.py
```

## Configuration
Modify the following variables in `bot.py` to fit your Discord server:
```python
NOTIFICATION_CHANNEL_ID = 1333930323544899585  # Replace with your notification channel ID
VOICE_NOTIFIER_ROLE_ID = 1333932112830664726  # Replace with your role ID
```

## Bot Permissions
Ensure the bot has the following permissions:
- Read Messages
- Send Messages
- Embed Links
- Manage Messages (for reactions)
- View Channels
- Connect & Speak (if needed)

## Contributing
Feel free to contribute by submitting pull requests or reporting issues.



