import discord #discord kütüphanesini import ettik
from discord.ext import commands #komutlar için gerekli olan modulu import ettik
import os
import random
from model import get_class
intents = discord.Intents.default() #ayrıcalıklar belirliyoruz
intents.message_content = True #Ayrıcılıkların içindeki mesaj içeriğini erişmek için açıyoruz
IMAGE_DIR = "images"
os.makedirs(IMAGE_DIR,exist_ok=True)
bot = commands.Bot(command_prefix='$', intents=intents) #$ komutu ile aktive olan bot oluşturuyoruz 

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def merhaba(ctx):
    await ctx.send(f'Merhaba!Ben {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
@bot.command(help="Görselinizi yapay zeka ile analiz edin!")
async def check(ctx):
    if ctx.message.attachments:
        for i in ctx.message.attachments:
            file_name=i.filename
            file_path=os.path.join(IMAGE_DIR,file_name)
            await i.save(file_path)
            await ctx.send("Görseliniz başarıyla kayıt edildi"+"!"*random.randint(1,50))
            class_name,score=get_class(file_path)
            await ctx.send(f"""Sonuçlar:
                            Görselinizin sınıfı: {class_name}
                            Doğruluk oranı: {score}""")
    else:
        await ctx.send("Görsel bulunamadı, komutun çalışması için lütfen mesajınıza bir görsel ekleyin...")