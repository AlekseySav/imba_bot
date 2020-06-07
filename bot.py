import requests
import vk_api
from random import randint
from vk_api.longpoll import VkLongPoll, VkEventType                                                                                                                 

from some_stupid_stuff import die

class Message:
    def __init__(self, text, file=None, event=None, id=None):
        self.text = text
        self.file = file
        self.event = event

        if id is not None:
            self.id = id
        else:
            self.id = randint(-1000000, 1000000)


def init(t):
    global longpoll, vk

    print("init... ", end='')
    vk_session = vk_api.VkApi(token=t)

    if not vk_session:
        die("failed")

    longpoll = VkLongPoll(vk_session)
    vk = vk_session.get_api()

    print("ok")
    


def sched(r):
    global recv

    recv = r
    print("sched... ok")

    for event in longpoll.listen():
        if event.to_me or event.type != VkEventType.MESSAGE_NEW:
            chat = event.chat_id if hasattr(event, "chat_id") else None
            user = event.user_id if hasattr(event, "user_id") else None
            text = event.text.lower() if hasattr(event, "text") else None
            recv((chat, user), Message(text, event=event.type))


nr_of = 1

def send(user, msg):
    global nr_of
    print("send... (%d)" % nr_of, end='\t')
    nr_of += 1

    if user[0] is not None:
        vk.messages.send(chat_id=user[0], random_id=msg.id, message=msg.text, attachment=msg.file)
    else:
        vk.messages.send(user_id=user[1], random_id=msg.id, message=msg.text, attachment=msg.file)
