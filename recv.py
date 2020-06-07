from bot import Message, send
from vk_api.longpoll import VkEventType   

recv_prev = False
joke_setup = False

def eq(s1, s2):
    if len(s1) > len(s2):
        if len(s1) != len(s2) + 1 or s1[len(s1)-1] != '*': 
            return False

    for i in range(len(s1)):
        if s1[i] == '*':
            return True
        if s1[i] != s2[i]:
            return False
    return True


def sendif(t, ms_params):
    global recv_prev

    if recv_prev:
        return

    if t == None:
        recv_prev = True
    else:
        for i in t.split('|'):
            if eq(i, recv_msg.text):
                recv_prev = True
                break

    if recv_prev == True:
        for i in ms_params:
            send(recv_user, Message(*i))


def recv(user, msg):
    global recv_user, recv_msg, recv_prev, joke_setup
    recv_user = user
    recv_msg = msg
    recv_prev = False

    if msg.event != VkEventType.MESSAGE_NEW:
        if msg.event == VkEventType.CHAT_EDIT:
            sendif(None, [[None, "photo-192501264_457239032"]])
        return

    sendif("коля гей?|коля шиз?", [["да"]])

    sendif("я ваня|я диван|я литва", [["ЛИТВА??????????????"], [None, "photo-192501264_457239035"]])
    sendif("я даня", [["чмоооoo"], ["чмоооoo"], ["чмоооoo"], ["чмоооoo"]])
    sendif("я коля|я леша|я антон", [[None, "photo-192501264_457239030"]])
    sendif("я *|привет|здравствуйте", [[None, "photo-192501264_457239032"]])

    sendif("го считать", [["добро пожаловать в мою палату", "photo-192501264_457239018"]])
    sendif("заткнись|молчать", [["завали ебало ЧМО"]])
    sendif("ок", [["ок"], ["ок"], ["ок"], ["ок"], ["ок"], ["ок"], ["ок"], ["ок"], ["ок"], ["ок"]])

    if joke_setup:
        sendif("*", [["АХАХАХАХАХА"], ["АХАХАХАХАХА"], ["АХАХАХАХАХА"], ["АХАХАХАХАХА"], ["АХАХАХАХАХА"], ["АХАХАХАХАХА"]])
        joke_setup = False
    if not recv_prev:
        sendif("хочешь шутку?", [["ну"]])
        sendif("что общего *", [["что"]])
        if recv_prev:
            joke_setup = True

    if user[1] == 277022688:
       sendif("*", [["ок"]])

    recv_prev = False
    sendif("1514*|л2ш*", [["психушка"]])
