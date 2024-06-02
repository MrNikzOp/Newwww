# ©️ LISA-KOREA | @LISA_FAN_LK | NT_BOT_CHANNEL | LISA-KOREA/YouTube-Video-Download-Bot

# [⚠️ Do not change this repo link ⚠️] :- https://github.com/LISA-KOREA/YouTube-Video-Download-Bot

from pyrogram import Client, filters
import datetime
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ForceReply
from Youtube.config import Config
from Youtube.script import Translation
from Youtube.forcesub import handle_force_subscribe




@Client.on_callback_query(filters.regex("cancel"))
async def cancel(client, callback_query):
    await callback_query.message.delete()

# Start command handler
@Client.on_message(filters.private & filters.command("start"))
async def about(client, message):
    if Config.CHANNEL:
      fsub = await handle_force_subscribe(client, message)
      if fsub == 400:
        return
    await message.reply_text(
        text=Translation.START_TEXT,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton('⛔️ Close', callback_data='cancel')]
        ]
    ))

