import os
from telegram import Update
from telegram.ext import ApplicationBuilder,
CommandHandler, ContextTypes

async def start(update: Update, context;
ContextTypes.DEFAULT_TYPE):
  await update.message.reply_text( "Доброе утро, Танечка! Я твой личный  помощник.")

app =
ApplicationBuilder().token(os.environ["TELEGRAM_TOKEN"]).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
