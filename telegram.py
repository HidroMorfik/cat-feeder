#!/usr/bin/env python3
import os
import asyncio
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.types import InputFile
from video import Camera
from cat import CatDetection
import threading
import time
os.chdir("/home/zesma/Desktop/project/")


#time.sleep(30)
bot = Bot(token='BOT_TOKEN')
dp = Dispatcher(bot)

cam = Camera()
c = CatDetection()

exit_flag = False
chat_id = 'CHAT_ID'




async def on_startup(dp):
    await bot.send_message(chat_id, "Bot Başlatıldı")



@dp.message_handler(commands=['start', 'help'])
async def welcome(message: types.Message):
    print("************help istendi********************")
    global exit_flag
    exit_flag = True
    c.terminate()
    await message.answer("Merhaba ben zesma, kediler için buradayım! Anlık video almak için -> /video. Otomatik algılamayı açmak için -> /auto . Yardım için -> /help")
    
@dp.message_handler(commands=['reboot'])
async def welcome(message: types.Message):
    print("************reboot istendi********************")
    global exit_flag
    exit_flag = True
    c.terminate()
    await message.answer("Raspberry pi reboot atılıyor..")
    await asyncio.sleep(3)
    os.system("sudo reboot")




@dp.message_handler(commands=['video'])
async def video(message: types.Message):
    print("*****************video istendi*************")
    global exit_flag
    exit_flag = True
    c.terminate()
       
    await message.reply("Video yükleniyor..")
    
    cam.video()
    if os.path.exists('video.mp4'):
        video = open("video.mp4", 'rb')
        await bot.send_video(message.chat.id, video)
    print("video yüklendi")


@dp.message_handler(commands=['algila', 'auto'])
async def auto(message: types.Message):
    print("*******************auto istendi****************")
    await message.reply("Otomatik Algılama Başladı")
    
    c._init_()
    if not threading.Thread(target = c.run).is_alive():
        threading.Thread(target = c.run).start()



async def send_image():
    while True:
        if os.path.exists("image_1.png"):
            # Dosya varsa Telegram'a gönder
            with open("image_1.png", "rb") as photo:
                await bot.send_photo(chat_id, InputFile(photo) )

            # Dosyayı sil
            os.remove("image_1.png")
            print("image_1.png dosyası gönderildi ve silindi.")

        # Her 5 saniyede bir kontrol et
        await asyncio.sleep(5)

async def on_error(update, exception):
    # Hata durumunda buraya düşer
    print(f'Hata alındı: {exception}')



if __name__ == '__main__':


    loop = asyncio.get_event_loop()
    loop.create_task(send_image())

    dp.register_errors_handler(on_error)
    dp.middleware.setup(LoggingMiddleware())


    executor.start_polling(dp, on_startup = on_startup, skip_updates=True)   
