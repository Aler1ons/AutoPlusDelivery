from telethon import TelegramClient, events
import os

api_id = 23355668
api_hash = ea8d634e84ebbb5f21ac93c3d531c533

client = TelegramClient('autoplus_session', api_id, api_hash)

@client.on(events.NewMessage)
async def handler(event):
    sender = await event.get_sender()
    if sender.is_self:
        return

    message_text = event.raw_text.lower()
    if 'доставка' in message_text:
        await event.reply('+')
        me = await client.get_me()
        chat = await event.get_chat()
        chat_name = getattr(chat, 'title', 'Приватний чат')
        await client.send_message(me.id, f"✅ Відповів на 'доставка' в чаті: {chat_name}")

client.start()
print("Бот працює на Railway!")
client.run_until_disconnected()
