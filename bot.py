#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""A Telegram bot for Synology NAS"""

import logging
import json
import os
from synolopy import NasApi
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

# Texts “consts”
TEXTS = {
    'start': '一次給我一個連結，我將為您創建下載任務',
    'error_not_owner': '對不起我只效忠於我的主人，你可以在 https://github.com/idealhack/synologynasbot 建立一個自己的bot。sorry, I only take orders from my master, get your own bot at https://github.com/idealhack/synologynasbot',
    'error_link': '請傳給我有效的連結 (magnet or http)',
    'error_syno': 'an error occurred, please make sure it’s a valid link and try again',
    'created': '成功新增下載任務',
    'magnet_prefix': 'magnet:?xt=urn:btih:',
    'http_prefix': 'http',
	 'nowmissionstart':'now mission start' ,
}


# Handlers
def start(bot, update):
    """Send a message when the command /start is issued."""
    update.message.reply_text(TEXTS['start'])

def nowmission(bot, update):
	update.message.reply_text(TEXTS['nowmissionstart'])
	s = json.dumps(nas.downloadstation.task.request('list'))
	json_array = json.load(s)
	for item in json_array:
		replytxt = item['title'] + "\n" + item['status']
		update.message.reply_text(nas.downloadstation.task.request('list'))
	update.message.reply_text("end \n ll")


def text(bot, update):
    """Handle the user message."""

    # only accept messages from the owner
    if update.message.from_user.username != os.getenv("SYNOLOGY_NAS_BOT_OWNER"):
        update.message.reply_text(TEXTS['error_not_owner'])
        return

    t = update.message.text
    logger.info('got message "%s"', t)

    # if it’s not a link, tell the user
    if not t.startswith(TEXTS['magnet_prefix']) and not t.startswith(TEXTS['http_prefix']):
        update.message.reply_text(TEXTS['error_link'])
        return

    # if it’s a valid link, download it
    try:
        nas.downloadstation.task.request('create', uri=t)
        update.message.reply_text(TEXTS['created'])
    except:
        update.message.reply_text(TEXTS['error_syno'])


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('update "%s" caused error "%s"', update, error)


def main():
    """Start the bot."""

    # Init Synology API
    global nas
    nas = NasApi(os.getenv("SYNOLOGY_NAS_BOT_URL")
               , os.getenv("SYNOLOGY_NAS_BOT_ACCOUNT")
               , os.getenv("SYNOLOGY_NAS_BOT_PASSWORD"))

    # Create the EventHandler
    updater = Updater(os.getenv("SYNOLOGY_NAS_BOT_TOKEN"))
    dp = updater.dispatcher

    # On different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("NowMission", nowmission))
    dp.add_handler(MessageHandler(Filters.text, text))

    # Log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
