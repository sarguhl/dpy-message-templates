import discord

from config.config import Token
from utility.bot import Bot

intents = discord.Intents.all()
# SET PREFIX OF BOT
client = Bot("YOUR PREFIX HERE", intents=intents)

@client.event
async def on_ready():
    client.logger.info(f"Logged in as {client.user.name} ({client.user.id})")
    print(discord.__version__)
        
if __name__ == "__main__":
    client.run(Token.bot())