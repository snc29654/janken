import tkinter
import random
from tkinter import ttk
from PIL import Image, ImageTk
import time
import threading
import glob
import signal
from tkinter.font import Font 
you_win = 0
janken_counter = 0
janken_counter_old = 0
jan =0
class TestCombobox(ttk.Combobox):
    def __init__(self, var, master=None):
        li = ['グー', 'チョキ', 'パー']     
        super().__init__(master, values=li) 
        self.var = var                      
        self.bind(                          
            '<<ComboboxSelected>>',
            self.show_selected
            )
        
    def show_selected(self, event):
        global janken_counter
        global janken_counter_old
        global you_win
        global jan
        #じゃんけんを実施したらカウントアップ
        janken_counter = janken_counter + 1
        #コンピュータは乱数でじゃんけんを決定します
        jan = random.randint(1,3)
        if jan == 1:
            jan_con='グー'
            if self.get() == 'チョキ':
                self.var.set('あなたはチョキ：あなたの負け')    
                you_win = 2
            elif  self.get() == 'パー':
                self.var.set('あなたはパー：あなたの勝ち')    
                you_win = 1
            else:
                self.var.set('あなたはグー：あいこ')    
                you_win = 0
        elif jan == 2:
            jan_con='チョキ'
            if self.get() == 'パー':
                self.var.set('あなたはパー：あなたの負け')    
                you_win = 2
            elif  self.get() == 'グー':
                self.var.set('あなたはグー：あなたの勝ち')    
                you_win = 1
            else:
                self.var.set('あなたはチョキ：あいこ')    
                you_win = 0
        elif jan == 3:
            jan_con='パー'
            if self.get() == 'グー':
                self.var.set('あなたはグー：あなたの負け')    
                you_win = 2
            elif  self.get() == 'チョキ':
                self.var.set('あなたはチョキ：あなたの勝ち')    
                you_win = 1
            else:
                self.var.set('あなたはパー：あいこ')    
                you_win = 0
        else:
           pass 
def jpg_select():
    global janken_counter
    global janken_counter_old
    global you_win
    global jan


    while(1):
        #じゃんけんを実施したか？
        if janken_counter == janken_counter_old:
            #time.sleep(1) 
            continue
            #じゃんけんしてません
        else:
            pass
        #実施しました
        janken_counter_old = janken_counter


        if jan == 1:
            computer='グー'
            n = 'gu3.jpg'
        elif jan == 2:
            computer='チョキ'
            n = 'choki3.jpg'
        else:
            computer='パー'
            n = 'pa3.jpg'

        lbl = tkinter.Label(text='コンピュータは'+computer,font=48)
        lbl.place(x=30, y=350)

        img2 = Image.open(n)
        img2 = img2.resize((400,300),Image.ANTIALIAS)
        img2 = ImageTk.PhotoImage(img2)
        canvas = tkinter.Canvas(bg = "white", width=400, height=300)
        canvas.place(x=0, y=0)
        item = canvas.create_image(30, 30, image=img2, anchor=tkinter.NW)
        canvas.itemconfig(item,image=img2)

        if c.get() == 'チョキ':
            n='choki3.jpg'
        if c.get() == 'グー':
            n='gu3.jpg'
        if c.get() == 'パー':
            n='pa3.jpg'

        img3 = Image.open(n)
        img3 = img3.resize((300,200),Image.ANTIALIAS)
        img3 = ImageTk.PhotoImage(img3)
        canvas = tkinter.Canvas(bg = "white", width=300, height=200)
        canvas.place(x=600, y=140)
        item = canvas.create_image(30, 30, image=img3, anchor=tkinter.NW)
        #time.sleep(1) 
        canvas.itemconfig(item,image=img3)




if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    root = tkinter.Tk()
    #ウインドウのサイズの初期値    2020.10.21
    root.geometry('1000x400')
    var = tkinter.StringVar(master=root)
    l = tkinter.Label(textvariable=var,font=48)
    l.place(x=700,y=100)
    c = TestCombobox(master=root, var=var)
    c.place(x=700,y=50)
    thread2 = threading.Thread(target=jpg_select)
    thread2.start()
    root.mainloop()