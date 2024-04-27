from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Initialize your Pyrogram client
app = Client("MUSIC MASTER")

# Define the /song command handler
@app.on_message(filters.command("song"))
async def song_command(client, message):
    # Create an inline keyboard button that redirects to @songdowningbot
    button = InlineKeyboardButton("Click here to download song", url="https://t.me/songdowningbot")
    keyboard = InlineKeyboardMarkup([[button]])

    # Send a message with the inline keyboard button
    await message.reply_text("Download your song:", reply_markup=keyboard)

# Run the client
app.run()
