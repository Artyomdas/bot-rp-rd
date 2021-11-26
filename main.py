from discord import FFmpegPCMAudio, Activity, ActivityType
from discord.ext.commands import Bot
import os
import keep_alive
bot = Bot(command_prefix="-", help_command=None)

@bot.event
async def on_ready() -> None:
    print(f"Бот {bot.user} успешно запущен.")
    await bot.change_presence(activity=Activity(name="музыку",  type=ActivityType.listening)) #статус бота (Слушает ... (действие в кавычках))

    voice_channel = bot.get_channel(913859642684235786) #айди голосового канала
    player = await voice_channel.connect()
    player.play(FFmpegPCMAudio("http://s02.fjperezdj.com:8006/live")) #ссылка на радио. Указывать в кавычках.
    
keep_alive.keep_alive()
bot.run(os.environ["OTEzODU3NzgxODg1NDY0NjQ3.YaEmYQ.ZOPUZI5IGaSYrM5GXHe-tk4UbLE"])


# Приятного пользования ;)
# (c) rozovoe utro

# Наш сервер - https://discord.gg/HN4XTp9
# Гайд по боту - https://youtu.be/gRcZqgyp7qQ
# Как найти айди голосового канала - https://www.youtube.com/watch?v=947kXVocXRk
