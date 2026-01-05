from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "8060008552:AAG4AR4rlL74boMxIFFE6QdvJvClBv2ckYo"
SUPPORT_ID = "@GhazalCandle"

# ---------- START ----------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🛒 خرید VPN", callback_data="buy")],
        [InlineKeyboardButton("💰 قیمت‌ها", callback_data="price")],
        [InlineKeyboardButton("🧑‍💻 پشتیبانی", callback_data="support")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "سلام 👋\n"
        "به ربات فروش VPN خوش اومدی 🤖\n\n"
        "یکی از گزینه‌های زیر رو انتخاب کن 👇",
        reply_markup=reply_markup
    )

# ---------- BUTTON HANDLER ----------
async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "buy":
        await query.edit_message_text(
            "🛒 خرید VPN\n\n"
            "📌 پلن‌ها:\n"
            "• 1 ماهه: 100\n"
            "• 3 ماهه: 250\n"
            "• 6 ماهه: 450\n\n"
            "برای خرید پیام بده 👇\n"
            f"{SUPPORT_ID}"
        )

    elif query.data == "price":
        await query.edit_message_text(
            "💰 لیست قیمت‌ها:\n\n"
            "• 1 ماهه: 100\n"
            "• 3 ماهه: 250\n"
            "• 6 ماهه: 450"
        )

    elif query.data == "support":
        await query.edit_message_text(
            "🧑‍💻 پشتیبانی مستقیم:\n"
            f"{SUPPORT_ID}"
        )

# ---------- APP ----------
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(buttons))

app.run_polling()
