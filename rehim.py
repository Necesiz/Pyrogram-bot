
#pyrogram

#ss
from Config import Config

api_id = Config.API_ID
api_hash = Config.API_HASH
bot_token = Config.BOT_TOKEN


from telethon import TelegramClient, events

client = TelegramClient('bot_session', api_id, api_hash).start(bot_token=bot_token)

@client.on(events.NewMessage(pattern='/purge'))
async def purge_messages(event):
    if event.is_private:
        await event.respond("Bu komut gruplarda kullanılmalıdır.")
        return

    # Yanıtlanan mesajın bilgilerini al
    replied_msg = await event.get_reply_message()
    if not replied_msg:
        await event.respond("Lütfen bu komutu yanıtlanan bir mesaj üzerinde kullanın.")
        return

    # Yanıtlanan mesajın altındaki tüm mesajları sil
    chat = await event.get_chat()
    messages = await client.get_messages(chat, reply_to=replied_msg.id)
    await client.delete_messages(chat, messages)

    # Kimin tarafından yapıldığını ve kaç saniyede silindiğini kaydet
    admin = await client.get_entity(event.sender_id)
    await event.respond(f"{len(messages)} mesaj {admin.first_name} tarafından {event.date - replied_msg.date} saniyede silindi.")

client.run_until_disconnected()

