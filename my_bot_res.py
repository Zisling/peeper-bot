import json
import re
import sqlite3
import glob
import random

list = {"my_videos": (
    'https://www.youtube.com/watch?v=nzeLzlbjszQ', 'https://www.youtube.com/watch?v=1Pf53iFqm4Y',
    'https://www.youtube.com/watch?v=_3aeQKOQd7I')}

story = {
    "yellow": ('text:the yellow duck is smiling at you like a creep 🙂',
               'text:you need to run for your life',
               'text:run the duck is after you',),
    "red": ('text:you go to your shower with your trusted red duck',
            'text:you start singing in the shower and then...',
            'text:a sword cut the duck down',
            'text:you start a fight with 12 different duck ninja',
            'text:and you lose and die while Eevee is watching you\nimg:ivy.png',
            ),
    "blue": ('img:blue1.jpg',
             'img:blue2.jpg',
             'img:blue3.jpg',
             'img:blue4.jpg',
             ),
    "white": ('text:dont blink\nimg:angel1.jpg',
              'text:why did you blink\nsti:angel2.webp',
              'text:run for your life',
              ),
    "the big duck up in the sky": ('img:the_big_duck_in_the_sky.png',)

}


def random_vid():
    # switch to add video from the pc
    # list_vid = glob.glob('random_vid/*.mp4')
    # list_vid.extend(list['my_videos'])
    list_vid = list['my_videos'] # switch
    ret = random.choice(list_vid)
    x = re.match('.+\.mp4', str(ret))
    if x is not None and x.span()[1] == str(ret).__len__():
        return 'vid:' + str(ret)
    else:
        return 'text:' + str(ret)


def random_gif():
    list_gif = glob.glob('*.gif')
    return random.choice(list_gif)


story_chat_id_map = {

}


def get_self(chat_id, st=""):
    if story_chat_id_map.keys().__contains__(chat_id):
        return story_chat_id_map[chat_id]
    else:
        new_duck = my_duck_step(chat_id, story[st])
        new_duck.register()
        return new_duck


def unregister(chat_id):
    if story_chat_id_map.keys().__contains__(chat_id):
        story_chat_id_map.pop(chat_id)
    else:
        print('no chat_id is in')


def list_of(list_name):
    return list[list_name]


def add_hw(subject, task):
    if not list.__contains__(subject):
        list[subject] = (str(task),)
    else:
        list[subject] = list[subject] + (str(task),)


class my_duck_step:
    def __init__(self, chat_id, message=("bug",), step_number=0):
        self.chat_id = chat_id
        self.step_number = step_number
        self.message = message

    def step(self):
        if self.step_number < self.message.__len__():
            msg = self.message[self.step_number]
            self.step_number += 1
            return msg
        else:
            return "DONE"

    def register(self):
        if not story_chat_id_map.keys().__contains__(self.chat_id):
            story_chat_id_map[self.chat_id] = self
        else:
            print("problem at register")

    def unregister(self):
        if story_chat_id_map.keys().__contains__(self.chat_id):
            story_chat_id_map.pop(self.chat_id)
