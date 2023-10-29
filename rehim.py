from telethon import TelegramClient, events, utils

from Config import Config

api_id = Config.API_ID
api_hash = Config.API_HASH
bot_token = Config.BOT_TOKEN



client = TelegramClient('chatbot_session', api_id, api_hash).start(bot_token=bot_token)




@client.on(events.NewMessage(pattern='/me'))
async def get_user_info(event):
    chat = await event.get_chat()
    chat_name = utils.get_display_name(chat)
    chat_id = utils.get_peer_id(chat)

    user = await event.get_sender()
    user_id = user.id
    user_first_name = user.first_name
    user_last_name = user.last_name if user.last_name else ""

    messages = await client.get_messages(chat_id, limit=0)
    message_count = len(messages)

    info_message = (f"Chat Adı: {chat_name}\n"
                    f"Toplam Mesaj Sayısı: {message_count}\n"
                    f"Kullanıcı ID: {user_id}\n"
                    f"Ad: {user_first_name}\n"
                    f"Soyad: {user_last_name}")

    buttons = [
        [{"text": "Məlumat al", "callback_data": "get_info"}]
    ]

    await event.reply(info_message, buttons=buttons)

@client.on(events.CallbackQuery(pattern="get_info"))
async def send_user_info(event):
    user = await event.get_sender()
    user_id = user.id
    user_first_name = user.first_name
    user_last_name = user.last_name if user.last_name else ""

    info_message = (f"Kullanıcı ID: {user_id}\n"
                    f"Ad: {user_first_name}\n"
                    f"Soyad: {user_last_name}")

    await event.edit(info_message)

client.start()
client.run_until_disconnected()
