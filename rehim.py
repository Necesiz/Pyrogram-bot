from telethon import TelegramClient, events, utils 
from telethon.tl.functions.users import GetFullUser 


from Config import Config

api_id = Config.API_ID
api_hash = Config.API_HASH
bot_token = Config.BOT_TOKEN



client = TelegramClient('chatbot_session', api_id, api_hash).start(bot_token=bot_token)



@client.on(events.NewMessage(pattern='/me'))
async def get_user_info(event):
    chat = await event.get_chat()
    chat_id = utils.get_peer_id(chat)

    # Kullanıcı hakkında bilgileri al
    user_id = event.sender_id
    user = await client(GetFullUser(user_id))

    # Kullanıcı adı ve soyadını al
    first_name = user.user.first_name
    last_name = user.user.last_name if user.user.last_name else ""

    # Chat ismini al
    chat_title = chat.title

    # Toplam mesaj sayısını al
    messages = await client.get_messages(chat, limit=0)
    message_count = messages.total

    # Bilgileri gönder
    buttons = [
        [{"text": "Məlumat al", "callback_data": "get_info"}]
    ]
    message = f"Chat adı: {chat_title}\nToplam mesaj sayısı: {message_count}\n\nKullanıcı ID: {user_id}\nAd: {first_name}\nSoyad: {last_name}"
    await event.respond(message, buttons=buttons)

@client.on(events.CallbackQuery())
async def callback_handler(event):
    if event.data == b'get_info':
        await event.edit('Məlumat alındı.')

client.start()
client.run_until_disconnected()
