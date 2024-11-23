import discord
from discord.ext import commands
from model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='#', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def list(ctx, count_heh = 5):
    await ctx.send("Ilmuwan terkenal : 1. Albert Einstein 2. Isaac Newton 3. Marie Curie 4. Julius Robert Oppenheimer 5. Ibnu Sina 6. Nikola Tesla 7. Galileo Galilei 8. B.J.Habibie")

@bot.command()
async def info(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f"./{attachment.filename}")
            await ctx.send(get_class(model_path="./keras_model.h5", labels_path="labels.txt", image_path=f"./{attachment.filename}"))
    else:
        await ctx.send("You forgot to upload the image :(")

bot.run("TOKEN")
