# url = "https://api.telegram.org/bot1242526231:AAF_E6iJo8Gw0GpTjgOI3k2wGlJJZQzWeYI/"
import json
import telebot
import my_bot_res
from telebot import types

bot = telebot.TeleBot("1242526231:AAF_E6iJo8Gw0GpTjgOI3k2wGlJJZQzWeYI")


def check_add(message):
    print(str(message.text).split(' ').__len__() >= 3)
    if str(message.text).split(' ').__len__() >= 3:
        return True
    else:
        bot.send_message(message.chat.id,
                         "incorrect format you need to enter /AddTask [your subject] [your Task description]")
        return False


@bot.message_handler(commands=['start'])
def send_welcome(message):
    print(message)
    bot.reply_to(message, message.from_user.first_name + """ you need some hot 🌶 so call to your local farmer""")


@bot.message_handler(commands=['corona'])
def corona(message):
    print(message)
    bot.send_animation(message.chat.id, open('corona.gif', 'rb'))


@bot.message_handler(commands=['random_vid', 'Random_vid'])
def vid(message):
    try:
        print(message)
        to_send = my_bot_res.random_vid()
        reply_to_step(message, to_send)
    except Exception as e:
        print(e)
        bot.reply_to(message, 'oooops server time out')


@bot.message_handler(commands=['random_gif', 'Random_gif'])
def gif(message):
    try:
        print(message)
        bot.send_animation(message.chat.id, open(my_bot_res.random_gif(), 'rb'))
    except Exception as e:
        print(e)
        bot.reply_to(message, 'oooops server time out')


@bot.message_handler(commands=['Help', 'help'])
def send_list_of_commands(message):
    bot.reply_to(message, """
    /start\n/Help\n/Videos\n/duck\n/corona\n/Random_gif\n/Random_vid
    """)


@bot.message_handler(regexp='🌶')
def pepper_send(message):
    print(message)
    bot.reply_to(message, '{} has use a pepper in the chat\nall hail {}!'
                 .format(message.from_user.first_name, message.from_user.first_name))


@bot.message_handler(commands=['Videos'])
def send_hw(message):
    videos = my_bot_res.list_of("my_videos")
    reply = ""
    for x in videos:
        reply = reply + '\n' + x
    bot.reply_to(message, reply)


# /AddTask [subject] [Task description]
# @bot.message_handler(func=check_add, commands=['AddTask'])
# def send_task(message):
#     data = str(message.text).split(' ', 2)
#     my_bot_res.add_hw(data[1], data[2])
#     bot.reply_to(message, "i have added to %s the task %s" % (data[1], data[2]))


@bot.message_handler(commands=['ivy'])
def ivy(message):
    bot.send_photo(message.chat.id, open('ivy.png', 'rb'))
    bot.send_message(message.chat.id, "or zivivy")
    bot.send_photo(message.chat.id, open('zivivy.png', 'rb'))
    msg = bot.send_message(message.chat.id, "give as the answer now")
    bot.register_next_step_handler(msg, the_ivy_question)


def the_ivy_question(message):
    try:
        answer = message.text
        if answer == 'zivivy':
            bot.send_message(message.chat.id, 'good boy')
        else:
            bot.send_message(message.chat.id, 'bad boy go and think on what you done')
            bot.send_photo(message.chat.id, open('angry_dog.png', 'rb'))
    except Exception as e:
        bot.reply_to(message, 'oooops')


@bot.message_handler(commands=['duck'])
def duck_debug(message):
    print(message.from_user.first_name)
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('yellow')
    itembtn2 = types.KeyboardButton('red')
    itembtn3 = types.KeyboardButton('blue')
    itembtn4 = types.KeyboardButton('white')
    itembtn5 = types.KeyboardButton('the big duck up in the sky')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5)
    bot.send_photo(message.chat.id, open('4ducks.jpg', 'rb'))
    msg = bot.send_message(message.chat.id, "Choose a duck to start debugging:", reply_markup=markup)
    bot.register_next_step_handler(msg, duck2)


def duck2(message):
    duck_id = message.chat.id
    try:
        markup = types.ReplyKeyboardRemove(selective=False)
        bot.send_message(message.chat.id, "you chosen %s" % message.text, reply_markup=markup)
        answer = message.text
        itembtn1 = types.KeyboardButton('Step')
        markup2 = types.ReplyKeyboardMarkup(row_width=1)
        markup2.add(itembtn1)
        if answer == 'yellow' or answer == "red" or answer == 'white' or answer == 'the big duck up in the sky' or answer == 'blue':
            duck = my_bot_res.get_self(duck_id, answer)
            reply = duck.step()
            msg = multiple_reply(message, reply, markup2)
            bot.register_next_step_handler(msg, duck_step)
        else:
            bot.send_message(message.chat.id, 'not writen yet')
    except Exception as e:
        my_bot_res.unregister(duck_id)
        print(e)
        bot.reply_to(message, 'oooops')


def duck_step(message):
    duck_id = message.chat.id
    try:
        markup = types.ReplyKeyboardRemove(selective=False)
        answer = message.text
        if answer == 'Step':
            duck = my_bot_res.get_self(duck_id)
            itembtn1 = types.KeyboardButton('Step')
            markup2 = types.ReplyKeyboardMarkup(row_width=1)
            markup2.add(itembtn1)
            reply = duck.step()
            if reply != 'DONE':
                msg = multiple_reply(message, reply, markup2)
                bot.register_next_step_handler(msg, duck_step)
            else:
                duck.unregister()
                bot.send_message(message.chat.id, "The end", reply_markup=markup)
                bot.send_animation(message.chat.id, open('community_dance.gif', 'rb'))
                print('end')
        else:
            my_bot_res.unregister(duck_id)
            bot.send_message(message.chat.id, "The end only step can be done in debug mod", reply_markup=markup)
            print("end badly")
    except Exception as e:
        print(e)
        my_bot_res.unregister(duck_id)
        bot.reply_to(message, 'oooops')


def reply_to_step(msg, reply, markup=None):
    if reply[0:5] == 'text:':
        return bot.send_message(msg.chat.id, reply[5:], reply_markup=markup)
    elif reply[0:4] == 'img:':
        return bot.send_photo(msg.chat.id, open(reply[4:], 'rb'), reply_markup=markup)
    elif reply[0:4] == 'gif:':
        return bot.send_animation(msg.chat.id, open(reply[4:], 'rb'), reply_markup=markup)
    elif reply[0:4] == 'vid:':
        return bot.send_video(msg.chat.id, open(reply[4:], 'rb'), reply_markup=markup)
    elif reply[0:6] == 'audio:':
        return bot.send_audio(msg.chat.id, open(reply[6:], 'rb'), reply_markup=markup)
    elif reply[0:4] == 'sti:':
        return bot.send_sticker(msg.chat.id, open(reply[4:], 'rb'), reply_markup=markup)
    else:  # return as text if dont find any type
        return bot.send_message(msg.chat.id, reply, reply_markup=markup)


# split on '\n'
# replay to all messages in the reply form duck step
def multiple_reply(msg, m_reply, markup):
    ret = msg
    lines = str(m_reply).split('\n')
    for x in lines:
        ret = reply_to_step(msg, x, markup)
    return ret


bot.polling()
