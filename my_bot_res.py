import json
import re
import sqlite3
import glob
import random

list = {"my_videos": (
    'https://www.youtube.com/watch?v=nzeLzlbjszQ', 'https://www.youtube.com/watch?v=1Pf53iFqm4Y',
    'https://www.youtube.com/watch?v=_3aeQKOQd7I')}

story = {
    "yellow": (
        'text:the yellow duck is smiling at you like a creep 🙂\ntext:dont move\nimg:yellow\\1.jpg',
        'she cant see us if we dont move\nimg:yellow\\2.jpg',
        'img:yellow\\3.jpg',
        'img:yellow\\4.jpg',
        'img:yellow\\4.jpg\nimg:yellow\\6.jpg\ntext:i think she see as run',
        'text:haaaaaaaaaaa\nimg:yellow\\7.jpg',),
    "red": ('text:This is the legend of the red rubber duck ,the most red duck in the house\nimg:red\\1.png',
            'text:one day you take the red rubber duck for a walk\nimg:red\\2.png',
            'text:and then form no where a sword is throw at you\nimg:red\\3.png',
            'text:you fall to the ground and start bleeding as 4 rubber duck ninja jump at you\nimg:red\\4.png',
            'text:you think for you self this is how i go, but the you look up as you red rubber duck stop them'
            '\nimg:red\\5.png',
            'img:red\\6.png\nimg:red\\7.png',
            'text:then before you say to your red rubber duck tanks\n'
            'text:he start to speak and say: weak human and push down the sword\n'
            'img:red\\8.png',
            ),
    "blue": ('img:blue\\1.png',
             'img:blue\\2.png',
             'img:blue\\3.png',
             'img:blue\\4.png',
             'img:blue\\5.png',
             'img:blue\\6.png',
             'img:blue\\7.png',
             ),
    "white": ('text:dont blink\nimg:angel1.jpg',
              'text:why did you blink\nsti:angel2.webp',
              'text:run for your life',
              ),
    "the big duck up in the sky": ('img:the_big_duck_in_the_sky.png',)
}


class Users:
    def __init__(self):
        self.users = ()

    def add_user(self, user_id, chat_id):
        self.users = self.users.__add__(((user_id, chat_id),))

    def __contains__(self, item):
        return self.users.__contains__(item)


def random_vid():
    # switch to add video from the pc
    # list_vid = glob.glob('random_vid/*.mp4')
    # list_vid.extend(list['my_videos'])
    list_vid = list['my_videos']  # switch
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
