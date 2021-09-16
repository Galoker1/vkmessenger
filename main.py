
# алгоритм отправки с несколькими аккаунтами с разными ip
# проверка ответа на каждое сообщение
# подогрев аккаунтов
# создание новых пользователей бд
# мессенджер
import time
import vk_api
from config import tokens
import tkinter

session=vk_api.VkApi(token=tokens[0][0])
vk=session.get_api()
def send_message(text,id):
        session.method("messages.send",{
        "user_id":id,
        "message":text+str(get_name(id)),
        "random_id":0
        })
def get_dialogs():
    dia=session.method("messages.getConversations",{"count":20})
    dialogs=dia["items"]
    for dialog in dialogs:
        print(dialog["conversation"]["peer"]["id"])
def get_messages(id):
    his=session.method("messages.getHistory",{"user_id":id})
    messages =his["items"]
    for message in messages:
        print(message["text"])
def get_name(id):
        user=session.method("users.get",{"user_ids":id})
        return user[0]["first_name"]
id=115060294
text_message="Здравствуйте, "
get_dialogs()
#send_message(text_message,id)
