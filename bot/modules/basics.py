import asyncio
from bot import CMD
from config import Config
from pyrogram import Client, filters

@Client.on_message(filters.command(CMD.START))
async def start(bot, update):
    msg = await bot.send_message(
        chat_id=update.chat.id,
        text="Ya Hello",
        reply_to_message_id=update.id
    )
    await asyncio.sleep(1)
    await bot.edit_message_text(
        chat_id=update.chat.id,
        message_id=msg.id,
        text="Need Ya Hello Again? 🤨"
    )

@Client.on_message(filters.command(CMD.HELP))
async def help_msg(bot, update):
    await bot.send_message(
        chat_id=update.chat.id,
        text="No Helmp. Everything DIY",
        reply_to_message_id=update.id,
        disable_web_page_preview=True
    )