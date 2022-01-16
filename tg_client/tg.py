import logging
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from config import Config

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Привет {user.mention_markdown_v2()}\!',
        reply_markup=ForceReply(selective=True),
    )


def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text(
        'Это бот, который оповещает о скидках на баскетбольные кроссовки с популярных онлайн магазинов'
    )

def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    update.message.reply_text(update.message.text)
    print(update.message.chat_id)

def send_parse_info(shoes_db):
    updater = Updater(Config.TG_TOKEN)
    updater.bot.send_photo(
        Config.TG_CHAT_ID,
        photo=open(shoes_db.img_path, 'rb'),
        caption=f'<strong>{shoes_db.platform.name.upper()}</strong>\n'
                f'<strong>{shoes_db.name}</strong>\n'
                f'<strong>Скидка</strong>: -{shoes_db.discount_percent}%\n'
                f'<strong>Цена</strong>:{shoes_db.price}\n'
                f'<strong>Размер</strong>: 11 US',
        parse_mode="HTML"
    )

def send_error_info(platform):
    updater = Updater(Config.TG_TOKEN)
    updater.bot.send_message(Config.TG_CHAT_ID, f"Error {platform}")

def main() -> None:
    updater = Updater(Config.TG_TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    # dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
