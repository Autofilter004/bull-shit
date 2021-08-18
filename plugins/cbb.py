#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>➥ Name</b> : <code> File Sharing bot</code>\n\n<b>➥ Editor</b> : <b><i><a href="https://t.me/Deepu_The_Editor">ᴅᴇᴇᴘᴜ</a></i></b>\n\n<b>➥ Language</b> : <code>Python3</code>\n\n<b>➥ Library</b> : <i><a href="https://docs.pyrogram.org">Pyrogram Asyncio 1.13.0 </a></i>\n\n<b>➥ Source Code</b> : <i><a href="https://github.com">Click Me</a></i>",
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
