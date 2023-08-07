from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

token = "Your_Bot_Token"
auth_chat = ["Authorized_Chat_Id"]

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text("Welcome!")
    
def handle_response(text: str)->str:
    
    return f"This is a response to your message: {text}!"
    
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):

    chat_id: str = update.message.chat.id
    text:str = update.message.text

    print(f"User ({chat_id}): {text}")

    if str(chat_id) in auth_chat:
        await update.message.reply_text(handle_response(text))
    else:
        await update.message.reply_text("Unauthorized T^T")

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    print(f"Update {update} caused error {context.error}")

if __name__ == "__main__":

    print("Starting bot...")

    app = Application.builder().token(token).build()

    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    app.add_error_handler(error)

    print("Polling...")

    app.run_polling(poll_interval=5)