
#pyrogram

from pyrogram import Client, filters


from Config import Config

api_id = Config.API_ID
api_hash = Config.API_HASH
bot_token = Config.BOT_TOKEN



rehim = Client(":memory:", api_id, api_hash, bot_token=bot_token)

@rehim.on_message(filters.command(['start']))
def start_command(client, message):
    message.reply_text("Merhaba! Benim adım StartBot. Nasıl yardımcı olabilirim?")
    
#TELETHON SETRİ



rehim.run()

