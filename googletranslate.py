from ctypes.wintypes import WORD
import tkinter as tk
from tkinter import *
from tkinter import BOTTOM, Frame, Label, ttk
from cv2 import EMD
from googletrans import Translator,LANGUAGES
from matplotlib.pyplot import text
from calendar import timegm


def change(text="type",src="English",dest="Hindi"):
    text1=text
    src1=src
    dest1=dest
    trans=Translator()
    trans1=trans.translate(text,src=src1,dest=dest1)
    return trans1



def data():
    s=comb_sor.get()
    d=comb_des.get()
    masg=src_text.get(1.0,END)
    textget=change(text=masg , src=s,dest=d)
    des_text.delete(1.0,END)
    des_text.insert(END,textget)




root=tk.Tk()

root.title("GOOGLE TRANSLATOR")
root.geometry("500x700")
root.config(bg='blue')

lab_txt=Label(root,text="Translator",font=("Times New Roman",20,"bold"),bg='red')
lab_txt.place(x=100,y=40,height=50,width=300)

frame=Frame(root).pack(side=BOTTOM)

lab_txt=Label(root,text="Source Text",font=("Times New Roman",20,"bold"),fg="black",bg="blue")
lab_txt.place(x=100,y=100,height=20,width=300)


src_text= Text(frame,font=("Times New Roman",20,"bold"),wrap=WORD)
src_text.place(x=10,y=130,height=150,width=480)

list_text=list(LANGUAGES.values())

comb_sor = ttk.Combobox(frame,value=list_text)
comb_sor.place(x=10,y=300,height=40,width=150)
comb_sor.set("english")

button_change= Button(frame,text="Translate",relief=RAISED,command=data)
button_change.place(x=170,y=300,height=40,width=150)

comb_des = ttk.Combobox(frame,value=list_text)
comb_des.place(x=330,y=300,height=40,width=150)
comb_des.set("english")

lab_txt=Label(root,text="Destination Text",font=("Times New Roman",20,"bold"),fg="black",bg="blue")
lab_txt.place(x=100,y=360,height=20,width=300)

des_text= Text(frame,font=("Times New Roman",20,"bold"),wrap=WORD)
des_text.place(x=10,y=400,height=150,width=480)


root.mainloop()


#shalini