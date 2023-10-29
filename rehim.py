from pyrogram import Client, filters


from Config import Config

api_id = Config.API_ID
api_hash = Config.API_HASH
bot_token = Config.BOT_TOKEN






app = Client("my_bot", api_id, api_hash, bot_token=bot_token)

@app.on_message(filters.command("me"))
def get_user_info(_, message):
    chat = message.chat
    user = message.from_user
    chat_info = app.get_chat(chat.id)
    chat_creator = chat_info.creator
    chat_members = chat_info.members_count

    first_name = user.first_name
    user_id = user.id
    message_count = user.messages_count
    message.delete()  # İlk mesajı sil

    response = (
        f"Melumatlar alındı, sizə ötürdüm!\n\n"
        f"Chat İsmi: {chat.title}\n"
        f"Chat ID: {chat.id}\n"
        f"Chat Yaratıcısı: {chat_creator}\n"
        f"Chat Üyeleri: {chat_members}\n"
        f"Mesaj Sayısı: {message_count}\n"
        f"Kullanıcı Adı: {first_name}\n"
        f"Kullanıcı ID'si: {user_id}"
    )
    
    message.reply(response)

app.run()
