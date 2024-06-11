from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from strings.filters import command
from AFROTOMusic import app
import config

@app.on_message(
    command(["المطور", "السورس", "المصنع"])
)
async def maker(client: Client, message: Message):
    await message.reply_photo(
        photo="https://graph.org/file/e254d61318e928efc7504.jpg",
        caption="• Dev Bot ↦ ميوزك \n ━━━━━━━━━━━━ \n • Dev ↦  @D_3_X . ",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝗠𝗢𝗛𝗔𝗠𝗠𝗘𝗗 •𝖮𝖡𝖨𝖳𝖮", url=f"tg://openmessage?user_id={config.OWNER_ID}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "", url=config.SUPPORT_CHANNEL
                    ),
                ],
            ]
        ),
    )
