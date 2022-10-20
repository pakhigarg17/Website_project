from tkinter import *
from tkinter import ttk
from tkinter import  messagebox
from tkcalendar import Calendar, DateEntry

from PIL import Image,ImageTk
import db

class Fee_Record:
    def __init__(self,master):
        self.master=master
        self.master.geometry('400x400')
        self.f_top=Frame(self.master)
        self.f_top.pack()
        self.f_mid=Frame(self.master,height=300,width=300)
        self.f_mid.pack()

        Label(self.f_top,text='Fee Deposit ',font=[20]).pack(padx=15,pady=15)
        Label(self.f_mid,text='Roll no  : ').place(x=10,y=0)
        Label(self.f_mid,text='Name     : ').place(x=10,y=30)
        Label(self.f_mid,text='Course   : ').place(x=10,y=60)
        Label(self.f_mid,text='Fee Amt  : ').place(x=10,y=90)
        Label(self.f_mid,text='Due Date : ').place(x=10,y=120)
        Label(self.f_mid,text='Late Fee : ').place(x=10,y=150)
        Label(self.f_mid,text='Amount   : ').place(x=10,y=180)
        Label(self.f_mid,text='Installment  : ').place(x=10,y=210)

        ttk.Entry(self.f_mid).place(x=100,y=0)
        ttk.Entry(self.f_mid).place(x=100,y=30)
        ttk.Entry(self.f_mid).place(x=100,y=60)
        ttk.Entry(self.f_mid).place(x=100,y=90)
        ttk.Entry(self.f_mid).place(x=100,y=120)
        ttk.Entry(self.f_mid).place(x=100,y=150)
        ttk.Entry(self.f_mid).place(x=100,y=180)
        ttk.Entry(self.f_mid).place(x=100,y=210)




root=Tk()
app=Fee_Record(root)
root.mainloop()        