import discord
import requests
import json
import os

def get_meme():
  response = requests.get('https://meme-api.com/gimme')
  json_data = json.loads(response.text)
  return json_data['url']

class MyClient(discord.Client):
  async def on_ready(self):
    print('Logged on as {0}!'.format(self.user))

  async def on_message(self, message):
    if message.author == self.user:
      return
    if message.content.startswith('$meme'):
      await message.channel.send(get_meme())

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)

# Get bot token from environment variable or config file
try:
    # Option 1: From environment variable
    token = os.getenv('DISCORD_BOT_TOKEN')
    if not token:
        # Option 2: From config file (create config.py with BOT_TOKEN)
        try:
            from config import BOT_TOKEN
            token = BOT_TOKEN
        except ImportError:
            print("Please set DISCORD_BOT_TOKEN environment variable or create config.py with BOT_TOKEN")
            exit(1)
    
    # client.run(token)  # Uncomment to run the bot
    print("Bot is ready to run. Uncomment the line above to start.")
except Exception as e:
    print(f"Error: {e}")