import eel
from config import alltokens
import vk_api
from datetime import datetime

tokens=alltokens

def get_name(token,id):
        session=vk_api.VkApi(token=token)
        vk=session.get_api()
        user=session.method("users.get",{"user_ids":id})

        return  user[0]["first_name"] + " " + user[0]["last_name"]

@eel.expose
def get_namenm(n,id):
        id=int(id)
        session=vk_api.VkApi(token=tokens[n][0])
        vk=session.get_api()
        user=session.method("users.get",{"user_ids":id})

        return  user[0]["first_name"] + " " + user[0]["last_name"]

@eel.expose
def get_messages(n,id):
    session=vk_api.VkApi(token=tokens[n][0])
    vk=session.get_api()
    his=session.method("messages.getHistory",{"user_id":id,"count":20})
    messages=[]
    for mes in his["items"]:
        ltime=mes["date"]+10800
        time=datetime.utcfromtimestamp(ltime).strftime('%d-%m %H:%M')
        name=get_name(tokens[n][0],mes["from_id"]).split(" ")[0]
        messages.append([mes["from_id"],name+": "+mes["text"]+"["+time+"]"])
    return messages

@eel.expose
def send_message(n,text,id):
        id=int(id)
        session=vk_api.VkApi(token=tokens[n][0])
        vk=session.get_api()
        session.method("messages.send",{
        "user_id":id,
        "message":str(text),
        "random_id":0
        })


@eel.expose
def chat(i):
    session=vk_api.VkApi(token=tokens[i][0])
    vk=session.get_api()
    dlgs=[]

    dia=session.method("messages.getConversations",{"count":20})
    dialogs=dia["items"]
    i=0
    for dialog in dialogs:
        id_dlg=dialog["conversation"]["peer"]["id"]
        """if dialog["last_message"]["read_state"]==0:
            last_mess=dialog["last_message"]["text"][0:20]
        else:"""
        last_mess=dialog["last_message"]["text"][0:20]
        if id_dlg>0:
            dlgs.append([get_name(tokens[i][0],id_dlg),id_dlg,tokens[i][0],last_mess])
    #print(dialog["last_message"])

    return dlgs


@eel.expose
def get_all_accounts():


    usrs=[]
    i=0
    for token in tokens:
        session=vk_api.VkApi(token=token)
        vk=session.get_api()
        session=vk_api.VkApi(token=token[0])
        vk=session.get_api()
        id=token[1]
        l_token=token[0]
        user=session.method("users.get",{"user_ids":id})
        name = user[0]["first_name"] + " " + user[0]["last_name"]
        usrs.append(name)

    return usrs

def get_settings():
    for widget in frame2.winfo_children():
        widget.destroy()
    for widget in frame3.winfo_children():
            widget.destroy()
    btn_usr=Button(frame2,text="settings",width=20,pady=20,bg="#dafffd",font=40,)
    btn_usr.pack()
def delete():
    for widget in frame2.winfo_children():
        widget.destroy()
    for widget in frame3.winfo_children():
        widget.destroy()
eel.init("")
eel.start("window.html",size=(1060,600))
