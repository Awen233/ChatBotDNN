from tkinter import *
import datetime
import time
from tkinter import ttk
import os
import playsound
import speech_recognition as sr
from gtts import gTTS
import chat as chat
from playsound import playsound

root = Tk()
root.title('chatbot')
#发送按钮事件
def sendmessage():
  #在聊天内容上方加一行 显示发送人及发送时间
  msgcontent = 'Me ' + time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()) + '\n '
  text_msglist.insert(END, msgcontent, 'green')
  user_input = text_msg.get('0.0', END)
  text_msglist.insert(END, user_input)

  text_msg.delete('0.0', END)
  
  response = chat.chatInput(user_input)
  msgcontent = 'chatbot ' + time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()) + '\n '
  text_msglist.insert(END, msgcontent, 'green')
  
  text_msglist.insert(END, response + '\n ')
  text_msg.delete('0.0', END)


'''定义取消发送 消息 函数'''
def cancel():
    text_msg.delete('0.0',END) #取消发送消息，即清空发送消息
 
'''绑定Enter键'''
def msgsendEvent(event):
    if event.keysym == 'Return':
        sendmessage()
        
def getChatBotMessage(input):
    response = chat.chatInput(input)
    return response
    
def getAudio():
    msgcontent = 'Me ' + time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()) + '\n '
    text_msglist.insert(END, msgcontent, 'green')
    text_msg.delete('0.0', END)
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio)
            text_msglist.insert(END, said + '\n ')
            text_msg.delete('0.0', END)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))
         
    response = chat.chatInput(said)
    msgcontent = 'chatbot ' + time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()) + '\n '
    text_msglist.insert(END, msgcontent, 'green')
    text_msglist.insert(END, response + '\n ')
      
    # Language in which you want to convert
    language = 'en'
      
    # Passing the text and language to the engine,
    # here we have marked slow=False. Which tells
    # the module that the converted audio should
    # have a high speed
    myobj = gTTS(text=response, lang=language, slow=False)
    myobj.save("welcome.mp3")
      
    # Playing the converted file
    playsound("welcome.mp3")
    return response



#创建几个frame作为容器
frame_left_top  = Frame(width=380, height=410, bg='white')
frame_left_center = Frame(width=380, height=100, bg='white')
frame_left_bottom = Frame(width=380, height=100)
scrollbar = ttk.Scrollbar(root)
scrollbar.grid(column = 1, row = 0, sticky="NWS")

##创建需要的几个元素
text_msglist = Text(frame_left_top)
text_msg = Text(frame_left_center);
text_msg.bind('<KeyPress-Return>',msgsendEvent)
button_sendmsg = Button(frame_left_bottom, text= 'Send', command=sendmessage)
button_cancel = Button(frame_left_bottom,text = 'Cancel',command = cancel)
button_getAudio = Button(frame_left_bottom,text = 'Speak',command = getAudio)
text_msglist.configure(yscrollcommand=scrollbar.set)
scrollbar.config(command = text_msglist.yview)

#创建一个绿色的tag
text_msglist.tag_config('green', foreground='#008B00')

#使用grid设置各个容器位置
frame_left_top.grid(row=0, column=0, padx=2, pady=5)
frame_left_center.grid(row=1, column=0, padx=2, pady=5)
frame_left_bottom.grid(row=2, column=0)
frame_left_top.grid_propagate(0)
frame_left_center.grid_propagate(0)
frame_left_bottom.grid_propagate(0)

#把元素填充进frame
text_msglist.grid()
text_msg.grid()
button_sendmsg.grid(row = 0, column = 0, sticky=W)
button_cancel.grid(row = 0, column = 1, sticky=W)
button_getAudio.grid(row = 0, column = 2, sticky=W)

print("hello i am here again")
#主事件循环
root.mainloop()


