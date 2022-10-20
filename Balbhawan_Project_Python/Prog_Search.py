import os
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
from tkinter import *
from PIL import Image ,ImageTk
import db

global tmpimgpath, pic

root = Tk()
root.geometry("500x500")
root.title("Student Registration Form")
root.resizable(0,0)

def get_selected_row(event):
    lstBox = event.widget
    values = [lstBox.get(idx) for idx in lstBox.curselection()]
    print(values[0])
   

def show_all():
    list_data.delete(0,END)
    data = db.get_data()
    for row in data:
        list_data.insert(END,row)
        
frame0 = Frame(root,bg="green",bd=1)
frame0.grid(row=0,columnspan=2)
frame0.configure(highlightbackground="black",highlightthickness=1,height="50",width="500")
frame0.grid_propagate(0)

frame5 = LabelFrame(root,text="Student Info")
frame5.place(x=25,y=315)
frame5.configure(highlightbackground="white",highlightthickness=0,height="400",width="450")
frame5.grid_propagate(0)


list_data = Listbox(frame5,width=70)
list_data.pack(side=LEFT)

sb1=Scrollbar(frame5)
sb1.pack(side=RIGHT,fill=Y)
list_data.configure(yscrollcommand=sb1.set)
sb1.configure(command=list_data.yview)

list_data.bind('<<ListboxSelect>>',get_selected_row)

show_all()
root.mainloop()