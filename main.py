import discord
from discord.ext import commands
from keep_alive import keep_alive
keep_alive()

intents = discord.Intents.all()
intents.members = True

prefixes = ["r!", "R!", " <@1133486025025519748>"]

bot = commands.Bot(command_prefix=prefixes, intents=intents)
        
@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    await bot.change_presence(activity=discord.Game(name="discord.gg/rfserver"))

@bot.event
async def on_member_join(member):
    channel_id = 1141032768101437461  # Replace with your channel ID

    embed = discord.Embed(title="Welcome to the Server!",
                          description=f"**English:** {member.mention} Welcome to the server! Send your Roblox nickname to <#1141032768101437461> with mentioning mods and wait for moderators to verify you. Or verify on <#1127501103358025929> channel with Bloxlink! :D If you don't know what to do, go to <#1140027025600561292>!\n\n"
                                      f"**Turkish:** {member.mention} Sunucuya hoş geldin! Roblox adını moderatörleri etiketleyerek <#1141032768101437461> kanalına gönder ve moderatörler tarafından doğrulanmanı bekle. Veya <#1127501103358025929> kanalına girip Bloxlink ile doğrulama yap. :D Nasıl yapacağını bilmiyorsan <#1140027025600561292> kanalına git!",
                          color=0x00ff00)

    channel = bot.get_channel(channel_id)
    await channel.send(embed=embed)

import os

@bot.event
async def on_disconnect():
    print("Bot disconnected. Reconnecting...")

@bot.event
async def on_error(event, *args, **kwargs):
    print(f"Error in {event}: {args[0]}")
    if isinstance(args[0], discord.ConnectionClosed):
        print("Reconnecting...")
        await asyncio.sleep(5)  # Add a delay before attempting to reconnect
        await bot.login(token, bot=True)
        await bot.connect()

token = os.getenv("token")

if token is None:
    print("Error: Token not found in environment variables.")
else:
    bot.run(token)
