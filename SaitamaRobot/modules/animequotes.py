#Made By @Madepranav On Telegram & Github Id Superboyfan
import html
import random
import pokemon.modules.animequotesstring as animequotesstring
from pokemon import dispatcher
from telegram import ParseMode, Update
from pokemon.modules.disable import DisableAbleCommandHandler
from telegram.ext import CallbackContext, run_async


@run_async
def animequotes(context: CallbackContext, update: Update):
    update.effective_message.reply_text(random.choice(animequotesstring.ANIMEQUOTES))
   

__help__ = """
 - /animequotes : for random Anime qoutes
"""

ANIMEQUOTES_HANDLER = DisableAbleCommandHandler("animequotes", animequotes)


dispatcher.add_handler(ANIMEQUOTES_HANDLER)

__mod_name__ = "AnimeQuotes"

