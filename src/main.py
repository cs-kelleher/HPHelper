import random

import discord
from discord.ext import commands
import logging
import yaml

from character import Character


logging.basicConfig(level=logging.INFO)
hp = discord.Client()

with open("conf/private_conf.yaml", "r") as config_file:
    try:
        conf = yaml.safe_load(config_file)
    except yaml.YAMLError as exc:
        logging.info(exc)

hp = commands.Bot(command_prefix='!hp ', description="Discord Bot for tracking character HP.")
characters = []


@hp.event
async def on_ready():
    logging.info(f'Logged in as {hp.user.name}')
    logging.info(hp.user.id)
    logging.info('------')


@hp.command()
async def new(ctx, name: str, level: int, hit_points: int):
    """Adds a new character the bot can keep track of."""
    char = Character(name=name, hp=hit_points, level=level)
    characters.append(char)
    await ctx.send(f'New character added!\n{char.print()}')

hp.run(conf['bot_token'])
