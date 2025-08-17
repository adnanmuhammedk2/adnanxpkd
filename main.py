import asyncio
import logging
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import API_ID, API_HASH, BOT_TOKEN, AUTH_CHANNEL, WEB_APP_URL
from forcesubscribe import is_subscribed

# Enable logging
logging.basicConfig(level=logging.INFO)

# Bot Client
app = Client(
    "my_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.command("start"))
async def start_command(client, message):
    if AUTH_CHANNEL:
        try:
            btn = await is_subscribed(client, message, AUTH_CHANNEL)
            if btn:
                username = (await client.get_me()).username
                if len(message.command) > 1:
                    btn.append([InlineKeyboardButton("♻️ Try Again ♻️", 
                              url=f"https://t.me/{username}?start={message.command[1]}")])
                else:
                    btn.append([InlineKeyboardButton("♻️ Try Again ♻️", 
                              url=f"https://t.me/{username}?start=true")])
                
                await message.reply_text(
                    f"<b>👋 Hello {message.from_user.mention},\n\n"
                    f"Please join the channel then click on try again button. 😇</b>",
                    reply_markup=InlineKeyboardMarkup(btn)
                )
                return
        except Exception as e:
            print(e)
    
    # Main start message
    await message.reply_text(
        f"<b>🎉 Welcome {message.from_user.mention}!\n\n"
        f"I'm your file sharing bot. Send me any file and I'll give you a shareable link!</b>"
    )

# Keep alive function
async def ping_server():
    import aiohttp
    sleep_time = 40
    while True:
        await asyncio.sleep(sleep_time)
        try:
            async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=10)) as session:
                async with session.get(WEB_APP_URL) as resp:
                    logging.info(f"Pinged server with response: {resp.status}")
        except Exception as e:
            logging.warning(f"Couldn't connect to server: {e}")

async def main():
    # Start keep-alive task
    asyncio.create_task(ping_server())
    
    # Start the bot
    await app.start()
    print("Bot is running...")
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
