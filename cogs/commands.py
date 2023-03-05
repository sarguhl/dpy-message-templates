import datetime

import discord
from discord import app_commands
from discord.ext import commands

from utility.bot import Bot

# Import "Messages" class
from utility.messages import Messages

class Commands(commands.Cog):
    def __init__(self, bot: Bot) -> None:
        self.bot = bot
        self.cached_emojis: dict[int, dict[list, datetime.datetime]] = {}

    # Creating a command which sends a demo-message using the "Messages" class
    @app_commands.command(name="test_error", description="Send a demo error-modal")
    async def test_error(self, interaction: discord.Interaction):
        await interaction.response.send_message(embed=Messages.error("Test Error Description"))

    @app_commands.command(name="test_warning", description="Send a demo warning-modal")
    async def test_warning(self, interaction: discord.Interaction):
        await interaction.response.send_message(embed=Messages.warning("Test Warning Description"))

    @app_commands.command(name="test_info", description="Send a demo information-modal")
    async def test_info(self, interaction: discord.Interaction):
        await interaction.response.send_message(embed=Messages.information("Test Info Description"))

    @app_commands.command(name="test_success", description="Send a demo success-modal")
    async def test_success(self, interaction: discord.Interaction):
        await interaction.response.send_message(embed=Messages.success("Test Success Description"))

async def setup(bot: Bot) -> None:
    await bot.add_cog(Commands(bot))