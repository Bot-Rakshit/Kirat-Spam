import discord
from discord.ext import commands
from fuzzywuzzy import fuzz

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', help_command=None, intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')


@bot.event
async def on_message(message):

    if message.author == bot.user:
        return

    keywords = ["kirat bhaiya", "kirat sir", "harkirat"]
    variations = ["kirat baia", "kirat bhaaiyaaa"]

    message_content = message.content.lower()
    for keyword in keywords:
        if keyword in message_content or any(
                fuzz.partial_ratio(keyword, message_content) > 80 for keyword in variations):
            scolding_message = f"Hey {message.author.mention}, STOP CALLING KIRAT BE INDEPEDENT!"
            await message.author.send(scolding_message)
            break

    await bot.process_commands(message)


bot.run(TOKEN)
