import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.typing = True
intents.presences = True
intents.members = True

bot = commands.Bot('%', case_insensitive=True, intents=intents)

CHANNEL_ID = channel id

@bot.event
async def on_ready():
    print('Logged in')
    print(f'Username: {bot.user.name}')
    print(f'Bot ID: {bot.user.id}')
    print(f'Invite URL: {discord.utils.oauth_url(bot.user.id)}&permissions=8')
    print("---------------------------------------------")
    print("Created by BlackGemOG")
    
@bot.command()
async def health(ctx, *, text):
    """Anonymous health messages"""
    await ctx.message.delete()
    ts = datetime.datetime.now().timestamp()
    embed = discord.Embed(colour=discord.Colour(0x660000), description=f"{text}")
    embed.set_author(name="Anonymous Mental Health", icon_url="https://cdn.discordapp.com/attachments/790369310081417232/796417112318672947/oie_jpg_1.png")
    embed.set_footer(text="The Affiliate Bot", icon_url="https://cdn.discordapp.com/attachments/790369310081417232/796417112318672947/oie_jpg_1.png")
    channel = bot.get_channel(CHANNEL_ID2)
    msg = await channel.send(embed=embed)
    embed = discord.Embed(colour=discord.Colour(0x008000), description=f"You are in good hands, we love you <3 <#790369309888741399>")
    embed.set_author(name="Anonymous Mental Health", icon_url="https://cdn.discordapp.com/attachments/790369310081417232/796417112318672947/oie_jpg_1.png")
    embed.set_footer(text="The Affiliate Bot", icon_url="https://cdn.discordapp.com/attachments/790369310081417232/796417112318672947/oie_jpg_1.png")
    await ctx.send(embed=embed)
    await ctx.author.send("Hi! This is an automated message from The Affiliate Workshop! We see that you're having a bit of trouble, but it's okay! We are here to help. Keep in mind we will send you this message everytime you do this command, just to check up on you! Stay safe, we all love you <3")
    print(f"{ctx.author} sent a health message: {text}")
    file_object = open('health.txt', 'a')
    file_object.write(f"{ctx.author} sent a health message: {text}\n")
    
bot.run("TOKEN")
