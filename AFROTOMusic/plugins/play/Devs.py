import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AFROTOMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AFROTOMusic import app
from random import  choice, randint

#          
                
@app.on_message(filters.command(["اوبيتو","مطور السورس","السورس"],"")
)
async def yas(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/e254d61318e928efc7504.jpg",
        caption=f"""◉ 𝙽𝙰𝙼𝙴 : ❪[سورس ميوزك اوبيتو](https://t.me/SOURCE_OBITO)❫
◉ 𝚄𝚂𝙴𝚁 : ❪ @D_3_X ❫
◉ 𝙸𝙳      : ❪ `5868423807` ❫
◉ 𝙱𝙸𝙾    : ❪ for me (@D_3_X)  ❫""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "قناة السورس", url=f"https://t.me/SOURCE_OBITO"), 
                 ],[
                   InlineKeyboardButton(
                        "「مطور السورس」", url=f"https://t.me/d_3_x"),
                ],

            ]

        ),

    )
@app.on_message(command(["تخ"]) & filters.group)
async def huhh(client, message):
    to_id = int(ahmed.split("to")[-1].split("in")[0])
    from_id = int(ahmed.split("ahmed")[-1].split("to")[0])
    in_id = int(caption.split("in")[-1])
    to_url = f"tg://openmessage?user_id={to_id}"
    from_url = f"tg://openmessage?user_id={from_id}"
    ahmed = message.text
    await message.reply_animation(
        animation=f"https://graph.org/file/0dcc6d8776f5486169077.mp4",
        caption=f"""↯︙قتل ↫ ⦗ {app.get_chat(to_id).first_name}]({to_url}) ⦘\nالضحيه دا 😢 ↫ ⦗ [{app.get_chat(from_id).first_name}]({from_url}) ⦘\nانا لله وانـا اليـه راجعـون 😢😢""",
    )
    reply_markup=InlineKeyboardMarkup(

       [
           [
               InlineKeyboardButton(
                   "‹ : Obito 𝖳𝖾𝖠𝗆 : ›", url=f"https://t.me/SOURCE_OBITO"),
           ],
       ]
    ),
  
