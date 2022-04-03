import discord
import logging
import yaml

logging.basicConfig(level=logging.INFO)
client = discord.Client()

with open("conf/private_conf.yaml", "r") as config_file:
    try:
        conf = yaml.safe_load(config_file)
    except yaml.YAMLError as exc:
        logging.info(exc)


@client.event
async def on_ready():
    logging.info('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$Str'):
        await message.channel.send('Response')
        logging.info("Message received")

client.run(conf['bot_token'])
