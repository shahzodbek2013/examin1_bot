import logging

from aiogram import Bot, Dispatcher, executor, types
from database import *

API_TOKEN = '6514349544:AAH2in3ZQwCj-ARgt2oXiJL7SlYOoJ2c2dg'

logging.basicConfig(level=logging.INFO)


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
create_table()



@dp.message_handler(commands="start")
async def start_bot(message: types.Message):
    await message.answer("salom")


@dp.message_handler(content_types=["audio"])
async def get_music(message: types.Message):
    music_name = message.audio.performer + " " + message.audio.title
    inert_in(music_name, message.audio.file_id)
    

@dp.message_handler(commands=["top"]) 
async def get_all(message: types.Message):
    musics = get_all_musics()
    print(musics)
    music_list = []
    
    for music in musics:
        music_list.append(
            musics[0][1]
        )
    
    for music in music_list:
        await message.answer_audio(music)


if __name__ == '__main__':
    executor.start_polling(dp)