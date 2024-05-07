import telebot
from telebot import types

token = '5956664037:AAEqcVbbxSVmDqwyF3hMwfHkwTbV3pQmxzk'
bot = telebot.TeleBot(token)
name = ''
problem1 = "В числе A поменяли местами цифры (не обязательно все) и получили число B. Существует ли такое число A, что A - B = 202220222022?"
ans1 = "Число A: 558022468913, а число B: 3558022468991"
problem2 = "Можно ли проделать в деревянном кубе отверстие (исходный куб не должен развалиться), через которое можно протащить такойже куб?"
ans2 = "Можно."


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    keyboard0 = types.InlineKeyboardMarkup()
    keyboard0.add(telebot.types.InlineKeyboardButton(text='Да', callback_data="yes"))
    keyboard0.add(telebot.types.InlineKeyboardButton(text='Нет', callback_data="no"))
    bot.send_message(message.chat.id, text="Привет. Мы знакомы?", reply_markup=keyboard0)

def reg_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, "Привет, " + name + ')')

@bot.message_handler(commands=['do'])
def menu(message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(telebot.types.InlineKeyboardButton(text='Решить задачку', callback_data='task'))
    keyboard.add(telebot.types.InlineKeyboardButton(text='Посмотреть ответы', callback_data='ans'))
    keyboard.add(telebot.types.InlineKeyboardButton(text='Ничего', callback_data='none'))
    bot.send_message(message.chat.id, text="Чего желаем?", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):

    bot.answer_callback_query(callback_query_id=call.id)

    if call.data == "yes":
        bot.send_message(call.message.chat.id, "Отлично!")
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
    elif call.data == "no":
        bot.send_message(call.message.chat.id, "Давай познакомимся! Как я могу тебя называть?")
        bot.register_next_step_handler(call.message, reg_name)
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)

    elif call.data == 'task':
        keyboardT = types.InlineKeyboardMarkup()
        keyboardT.add(telebot.types.InlineKeyboardButton(text='Задача 1', callback_data='task1'))
        keyboardT.add(telebot.types.InlineKeyboardButton(text='Задача 2', callback_data='task2'))
        bot.send_message(call.message.chat.id, text="Выбирай номер)", reply_markup=keyboardT)
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
    elif call.data == 'ans':
        keyboardA = types.InlineKeyboardMarkup()
        keyboardA.add(telebot.types.InlineKeyboardButton(text='Ответ на задачу 1', callback_data='ans1'))
        keyboardA.add(telebot.types.InlineKeyboardButton(text='Ответ на задачу 2', callback_data='ans2'))
        bot.send_message(call.message.chat.id, text="Хочешь посмотреть ответ? Надеюсь, решил(а)?)", reply_markup=keyboardA)
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
    elif call.data == 'none':
        bot.send_message(call.message.chat.id, "Действительно ничего? Хмпф.")
        bot.send_sticker(call.message.chat.id, 'CAACAgIAAxkBAAEGsUVjjcCqvx_Q1bRQHouPKDikyTqJIgAC5hcAAvP2gUnUb8mtTJzF0SsE')
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)

    elif call.data == "task1":
        global problem1
        bot.send_message(call.message.chat.id, problem1)
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
    elif call.data == "task2":
        global problem2
        bot.send_message(call.message.chat.id, problem2)
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)

    elif call.data == "ans1":
        global ans1
        bot.send_message(call.message.chat.id, ans1)
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
    elif call.data == "ans2":
        global ans2
        bot.send_message(call.message.chat.id, ans2)
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        bot.send_photo(call.message.chat.id, "https://problems.ru/show_document.php?id=1583265")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.send_message(message.from_user.id, "Моя твоя не понимать.")
    bot.send_sticker(message.from_user.id, 'CAACAgIAAxkBAAEGsbRjjdUIg7W0_ySeP9xPx_S575VieAACThcAAupwOUlnkUXWDzsgtCsE')

bot.polling()
