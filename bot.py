from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8060008552:AAHRxckpO3oUG_9YXIUVSX91Sq2rmjoxHtQ"
SUPPORT_ID = "@GhazalCandle"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "سلام 👋\n"
        "به ربات فروش VPN خوش اومدی 🤖\n\n"
        "از دستورات زیر استفاده کن:\n"
        "/buy خرید سرویس\n"
        "/price قیمت‌ها\n"
        "/support پشتیبانی"
    )

async def buy(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🛒 خرید VPN\n"
        "1 ماهه: 100\n"
        "3 ماهه: 250\n"
        "6 ماهه: 450\n\n"
        "برای خرید پیام بده 👇\n"
        f"{SUPPORT_ID}"
    )

async def price(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💰 قیمت‌ها:\n"
        "1 ماهه: 100\n"
        "3 ماهه: 250\n"
        "6 ماهه: 450"
    )

async def support(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"🧑‍💻 پشتیبانی:\n{SUPPORT_ID}"
    )

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("buy", buy))
app.add_handler(CommandHandler("price", price))
app.add_handler(CommandHandler("support", support))

app.run_polling()
