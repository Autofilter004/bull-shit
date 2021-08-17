
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from bot import Bot
from config import ADMINS
from helper_func import encode, get_message_id

@Bot.on_message(filters.private & filters.user(ADMINS) & filters.command('batch'))
async def batch(client: Client, message: Message):
    while True:
        try:
            first_message = await client.ask(text = "<b>🤯𝑓𝑜𝑟𝑤𝑎𝑟𝑑 𝑡ℎ𝑒 𝑓𝑖𝑟𝑠𝑡 𝑚𝑒𝑠𝑠𝑎𝑔𝑒 𝑓𝑟𝑜𝑚 ᴅʙ 𝑐ℎ𝑎𝑛𝑛𝑒𝑙 (Wɪᴛʜ Qᴜᴏᴛᴇs).. \n\n ᴏʀ 𝑠𝑒𝑛𝑑 𝑡ℎ𝑒 ᴅʙ 𝑐ℎ𝑎𝑛𝑛𝑒𝑙 𝑝𝑜𝑠𝑡 𝑙𝑖𝑛𝑘🦔 <\b>", chat_id = message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), timeout=60)
        except:
            return
        f_msg_id = await get_message_id(client, first_message)
        if f_msg_id:
            break
        else:
            await first_message.reply("❌ ᗴᖇᖇOᖇ\n\n 𝑡ℎ𝑖𝑠 𝐹𝑜𝑟𝑤𝑎𝑟𝑑𝑒𝑑 𝑝𝑜𝑠𝑡 𝑖𝑠 𝑛𝑜𝑡 𝑓𝑟𝑜𝑚 𝑚𝑦 ᴅʙ 𝑐ℎ𝑎𝑛𝑛𝑒𝑙 Oʀ 𝑡ℎ𝑖𝑠 𝑙𝑖𝑛𝑘 𝑖𝑠 𝑛𝑜𝑡 𝑡𝑎𝑘𝑒𝑛 𝑓𝑟𝑜𝑚 ᴅʙ 𝑐ℎ𝑎𝑛𝑛𝑒𝑙🐿️", quote = True)
            continue

    while True:
        try:
            second_message = await client.ask(text = "<b>🤭𝑓𝑜𝑟𝑤𝑎𝑟𝑑 𝑡ℎ𝑒 𝑓𝑖𝑟𝑠𝑡 𝑚𝑒𝑠𝑠𝑎𝑔𝑒 𝑓𝑟𝑜𝑚 ᴅʙ 𝑐ℎ𝑎𝑛𝑛𝑒𝑙 (Wɪᴛʜ Qᴜᴏᴛᴇs).. \n\n ᴏʀ 𝑠𝑒𝑛𝑑 𝑡ℎ𝑒 ᴅʙ 𝑐ℎ𝑎𝑛𝑛𝑒𝑙 𝑝𝑜𝑠𝑡 𝑙𝑖𝑛𝑘🐿️<\b>", chat_id = message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), timeout=60)
        except:
            return
        s_msg_id = await get_message_id(client, second_message)
        if s_msg_id:
            break
        else:
            await second_message.reply("❌ ᗴᖇᖇOᖇ\n\n 𝑡ℎ𝑖𝑠 𝐹𝑜𝑟𝑤𝑎𝑟𝑑𝑒𝑑 𝑝𝑜𝑠𝑡 𝑖𝑠 𝑛𝑜𝑡 𝑓𝑟𝑜𝑚 𝑚𝑦 ᴅʙ 𝑐ℎ𝑎𝑛𝑛𝑒𝑙 Oʀ 𝑡ℎ𝑖𝑠 𝑙𝑖𝑛𝑘 𝑖𝑠 𝑛𝑜𝑡 𝑡𝑎𝑘𝑒𝑛 𝑓𝑟𝑜𝑚 ᴅʙ 𝑐ℎ𝑎𝑛𝑛𝑒𝑙🦔", quote = True)
            continue


    string = f"get-{f_msg_id * abs(client.db_channel.id)}-{s_msg_id * abs(client.db_channel.id)}"
    base64_string = await encode(string)
    link = f"https://t.me/{client.username}?start={base64_string}"
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("🚀Sʜᴀʀᴇ Uʀʟ🚀", url=f'https://telegram.me/share/url?url={link}')]])
    await second_message.reply_text(f"<b>🤓Hᴇʀᴇ ɪs ʏᴏᴜʀ Lɪɴᴋ👇</b>\n\n{link}", quote=True, reply_markup=reply_markup)


@Bot.on_message(filters.private & filters.user(ADMINS) & filters.command('genlink'))
async def link_generator(client: Client, message: Message):
    while True:
        try:
            channel_message = await client.ask(text = "Forward Message from the DB Channel (with Quotes)..\nor Send the DB Channel Post link", chat_id = message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), timeout=60)
        except:
            return
        msg_id = await get_message_id(client, channel_message)
        if msg_id:
            break
        else:
            await channel_message.reply("❌ ᗴᖇᖇOᖇ\n\n 𝑡ℎ𝑖𝑠 𝐹𝑜𝑟𝑤𝑎𝑟𝑑𝑒𝑑 𝑝𝑜𝑠𝑡 𝑖𝑠 𝑛𝑜𝑡 𝑓𝑟𝑜𝑚 𝑚𝑦 ᴅʙ 𝑐ℎ𝑎𝑛𝑛𝑒𝑙 Oʀ 𝑡ℎ𝑖𝑠 𝑙𝑖𝑛𝑘 𝑖𝑠 𝑛𝑜𝑡 𝑡𝑎𝑘𝑒𝑛 𝑓𝑟𝑜𝑚 ᴅʙ 𝑐ℎ𝑎𝑛𝑛𝑒𝑙🐿️", quote = True)
            continue

    base64_string = await encode(f"get-{msg_id * abs(client.db_channel.id)}")
    link = f"https://t.me/{client.username}?start={base64_string}"
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("🚀Sʜᴀʀᴇ Uʀʟ🚀", url=f'https://telegram.me/share/url?url={link}')]])
    await channel_message.reply_text(f"<b>🤓Hᴇʀᴇ ɪs ʏᴏᴜʀ Lɪɴᴋ👇</b>\n\n{link}", quote=True, reply_markup=reply_markup)
