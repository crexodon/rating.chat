from telegram import InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
import logging
from profile.profile import Profile
from event_base.util import create_event_list

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


def start(bot, update):
    profile = Profile.create(update.message.chat.id)
    event_list = create_event_list(profile['basic']['chat_id'])
    profile['progress']['event_id'] = 'creation_user_name'
    profile['event_list'] = event_list
    Profile.save(profile, update.message.chat.id)

    chat_id = update.message.chat.id
    profile = Profile.load(chat_id)
    event_id = profile['progress']['event_id']
    event_class = profile['event_list']
    event_object = event_class[event_id]['class'](chat_id)

    button_list, text = event_object.create_virtual_keyboard()

    reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=3))
    bot.send_message(chat_id=chat_id, text=text, reply_markup=reply_markup)


def print_profile(bot, update):
    chat_id = update.message.chat.id
    profile = Profile.load(chat_id)

    print(profile)

    event_id = profile['progress']['event_id']
    event_object = profile['event_list'][event_id]['class'](chat_id)

    button_list, text = event_object.create_virtual_keyboard()

    reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=3))
    bot.send_message(chat_id=chat_id, text=text, reply_markup=reply_markup)


def button(bot, update):
    query = update.callback_query
    last_event_data = str(query.data)

    print(last_event_data)
    print(last_event_data.split(";"))
    event_id, decision_id, chat_id = last_event_data.split(";")

    # load profile
    profile = Profile.load(chat_id)

    # react on decision
    previous_event_id = profile['progress']['event_id']
    event_class = profile['event_list']
    event_object = event_class[previous_event_id]['class'](chat_id)
    profile = event_object.react(profile, decision_id)
    profile['progress']['event_id'] = event_id

    # create next event
    event_id = profile['progress']['event_id']
    event_object = event_class[event_id]['class'](chat_id)

    # save progress
    Profile.save(profile, chat_id)

    button_list, text = event_object.create_virtual_keyboard()

    reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=3))
    bot.send_message(chat_id=chat_id, text=text, reply_markup=reply_markup)


def error(bot, update, error_message):
    """Log Errors caused by Updates"""
    logger.warning('Update "%s" caused error "%s"', update, error_message)


def build_menu(buttons,
               n_cols,
               header_buttons=None,
               footer_buttons=None):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, header_buttons)
    if footer_buttons:
        menu.append(footer_buttons)
    return menu


def main():
    updater = Updater(token='541471711:AAFC46JebZN5qQO_znvjz6QRXIaCTcrNp0k')

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('profile', print_profile))

    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    updater.dispatcher.add_error_handler(error)

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
