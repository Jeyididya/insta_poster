from telegram.ext import Updater, CommandHandler
from telegram import Bot, ParseMode
import os

import shutil
TOKEN = "6279915734:AAEuRfgYEXCGMd3e6BMRU0BixiU6pPeq4rs"
CHANNEL =  "@sendMeLogs" #"@oldmercyfiles"
bot=Bot(TOKEN)

# bot.send_message(CHANNEL,"hello")
# logs_.send_message("checking Quote")
def send_message(message):
  bot.send_message(CHANNEL,message)
  