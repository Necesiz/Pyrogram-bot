from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from Config import Config

api_id = Config.API_ID
api_hash = Config.API_HASH
bot_token = Config.BOT_TOKEN



app = TelegramClient('bot_session', api_id, api_hash).start(bot_token=bot_token)
def get_chat_info(chat):
    chat_name = chat.title
    messages_count = chat.total_messages
    return chat_name, messages_count

def get_user_info(user):
    user_id = user.id
    first_name = user.first_name
    last_name = user.last_name
    return user_id, first_name, last_name

@app.on_message(filters.command("me"))
def my_info(_, message):
    chat_name, messages_count = get_chat_info(message.chat)
    user_id, first_name, last_name = get_user_info(message.from_user)

    reply_markup = InlineKeyboardMarkup([
        [InlineKeyboardButton("Məlumat al", callback_data=f"get_info_{user_id}")]
    ])

    message.reply_text(f"Chat adı: {chat_name}\nMesaj sayısı: {messages_count}\n"
                       f"Kullanıcı ID: {user_id}\nAd: {first_name}\nSoyad: {last_name}", 
                       reply_markup=reply_markup)

@app.on_callback_query()
def get_info(_, query):
    user_id = int(query.data.split("_")[2])
    user = app.get_users(user_id)
    _, _, _ = get_user_info(user)
    query.answer(f"Kullanıcı ID: {user_id}\nAd: {user.first_name}\nSoyad: {user.last_name}")

app.run()

#pyrogram

#ss


