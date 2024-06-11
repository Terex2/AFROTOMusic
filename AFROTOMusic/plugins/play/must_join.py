from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
from AFROTOMusic import app

@app.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(bot: Client, msg: Message):
    if not "https://t.me/SOURCE_OBITO":  # Not compulsory
        return
    try:
        try:
            await bot.get_chat_member("SOURCE_OBITO", msg.from_user.id)
        except UserNotParticipant:
            if "https://t.me/SOURCE_OBITO".isalpha():
                link = "https://t.me/SOURCE_OBITO"
            else:
                chat_info = await bot.get_chat("VVV5P")
                link = chat_info.invite_link
            try:
                await msg.reply(
                    f"⌯︙عذࢪاَ عزيزي ↫ {msg.from_user.mention} \n⌯︙عـليك الاشـتࢪاك في قنـاة البـوت اولآ\n⌯︙قناة البوت: @SOURCE_OBITO .\nꔹ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ꔹ",
                    disable_web_page_preview=True,
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton("ᯓ سورس ميوزك اوبيتو 𝅘𝅥𝅯", url=link)]
                    ])
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"I m not admin in the MUST_JOIN chat @SOURCE_OBITO !")
      
