from bot import CMD, Config
from pyrogram import Client, filters
from bot.helpers.file_dl import file_dl

@Client.on_message(filters.command(CMD.UPLOAD))
async def upload(bot, update):
  try:
    link = update.text.split(" ", maxsplit=1)[1]
    reply_to_id = update.id
    try:
      rename_name = link.split(" | ")[1]
      link = link.split(" | ")[0]
    except:
      rename_name = None
  except:
    try:
      link = update.reply_to_message
      reply_to_id = update.reply_to_message.id
      try:
        rename_name = update.text.split(" | ", maxsplit=1)[1]
      except:
        rename_name = None
    except:
      return await bot.send_message(
        chat_id=update.chat.id,
        text="Wrong usage boi",
        reply_to_message_id=update.id
        )
  init_msg = await bot.send_message(
    chat_id=update.chat.id,
    text="Downloadimg 😑",
    reply_to_message_id=update.id
    )
  try:
    await file_dl(bot, update, link, init_msg, reply_to_id, upload=True, rename=rename_name)
    await bot.send_message(
      chat_id=update.chat.id,
      text="Success LOL",
      reply_to_message_id=reply_to_id
      )
  except Exception as e:
    await bot.send_message(
      chat_id=update.chat.id,
      text=e,
      reply_to_message_id=reply_to_id
      )
  await bot.delete_messages(
    chat_id=update.chat.id,
    message_ids=init_msg.id
    )
      