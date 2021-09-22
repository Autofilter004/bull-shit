
from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.reply_photo(
            photo="https://telegra.ph/file/9374e3475b69ca28f27e4.jpg", caption=f"<b>➥ Creator : <a href='tg://user?id={OWNER_ID}'>🇩ᴇᴇᴘᴜ</a>\n\n➥ Language : <code>Python3</code>\n\n➥ Library : <a href='https://docs.pyrogram.org/'>Pyrogram asyncio {__version__}</a>\n\n➥ Source Code : <a href='https://github.com'>Click here</a>\n\n➥ Channel : @Xaglerzz\n\n➥ Support : @Deepu_The_Editor</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
