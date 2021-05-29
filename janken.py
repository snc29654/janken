import tkinter
import random
from tkinter import ttk
from PIL import Image, ImageTk
import time
import threading
import glob
import signal
you_win = 0
janken_counter = 0
janken_counter_old = 0
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
        #じゃんけんを実施したらカウントアップ
        janken_counter = janken_counter + 1
        #コンピュータは乱数でじゃんけんを決定します
        jan = random.randint(1,3)
        if jan == 1:
            jan_con='グー'
            if self.get() == 'チョキ':
                self.var.set('敵はグー：あなたの負け')    
                you_win = 2
            elif  self.get() == 'パー':
                self.var.set('敵はグー：あなたの勝ち')    
                you_win = 1
            else:
                self.var.set('敵はグー：あいこ')    
                you_win = 0
        elif jan == 2:
            jan_con='チョキ'
            if self.get() == 'パー':
                self.var.set('敵はチョキ：あなたの負け')    
                you_win = 2
            elif  self.get() == 'グー':
                self.var.set('敵はチョキ：あなたの勝ち')    
                you_win = 1
            else:
                self.var.set('敵はチョキ：あいこ')    
                you_win = 0
        elif jan == 3:
            jan_con='パー'
            if self.get() == 'グー':
                self.var.set('敵はパー：あなたの負け')    
                you_win = 2
            elif  self.get() == 'チョキ':
                self.var.set('敵はパー：あなたの勝ち')    
                you_win = 1
            else:
                self.var.set('敵はパー：あいこ')    
                you_win = 0
        else:
           pass 
def jpg_select():
    global janken_counter
    global janken_counter_old
    global you_win
    while(1):
        じゃんけんを実施したか？
        if janken_counter == janken_counter_old:
            time.sleep(1) 
            continue
            #じゃんけんしてません
        else:
            pass
        #実施しました
        janken_counter_old = janken_counter
        if you_win == 1:
            n = 'sample01.jpg'
        elif you_win == 2:
            n = 'sample02.jpg'
        else:
            n = 'sample03.jpg'
           
        img2 = Image.open(n)
        img2 = img2.resize((400,300),Image.ANTIALIAS)
        img2 = ImageTk.PhotoImage(img2)
        canvas = tkinter.Canvas(bg = "white", width=400, height=300)
        canvas.place(x=0, y=0)
        item = canvas.create_image(30, 30, image=img2, anchor=tkinter.NW)
        time.sleep(1) 
        canvas.itemconfig(item,image=img2)
if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    root = tkinter.Tk()
    #ウインドウのサイズの初期値    2020.10.21
    root.geometry('1000x400')
    var = tkinter.StringVar(master=root)
    l = tkinter.Label(textvariable=var)
    c = TestCombobox(master=root, var=var)
    l.pack()
    c.pack()
    thread2 = threading.Thread(target=jpg_select)
    thread2.start()
    root.mainloop()