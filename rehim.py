
#pyrogram

from pyrogram import Client, filters
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from Config import Config

api_id = Config.API_ID
api_hash = Config.API_HASH
bot_token = Config.BOT_TOKEN



rehim = Client(":memory:", api_id, api_hash, bot_token=bot_token)

@rehim.on_message(filters.command(['start']))
def start_command(client, message):
    message.reply_text("Merhaba! Benim adım StartBot. Nasıl yardımcı olabilirim?")
    
    
# Komutları tanımlayın
@rehim.on_message(filters.command(["chatbot"]))
def start(_, message):
    markup = InlineKeyboardMarkup([[InlineKeyboardButton("Aktiv Et", callback_data="activate"),
                                   InlineKeyboardButton("Deaktiv Et", callback_data="deactivate")]])
    message.reply_text("Bot şu an deaktif.", reply_markup=markup)

@rehim.on_callback_query()
def button(_, callback):
    if callback.data == "activate":
        callback.message.reply_text("Bot aktiv edildi.")
        callback.message.edit_reply_markup(reply_markup=None)
    elif callback.data == "deactivate":
        callback.message.reply_text("Bot deaktiv edildi.")
        callback.message.edit_reply_markup(reply_markup=None)

@rehim.on_message(filters.text & filters.command)
def echo(_, message):
    if message.text() == "selam":
        message.reply_text("Aleyküm Selam!")
#TELETHON SETRİ



rehim.run()

