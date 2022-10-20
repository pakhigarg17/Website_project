from tkinter import ttk
from tkinter import *

class Daily_Attendance(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        w, h = self.winfo_screenwidth(), self.winfo_screenheight()
        self.geometry("%dx%d+0+0" % (w, h))
        self.config(bg='orange')
        self.resizable(0,0)

        f_header=Frame(self,bg='orange')
        f_header.pack()
        Label(f_header,text='Daily Attendance Portal',font=['impact',30],bg='orange').pack(pady=20)
        f_top=Frame(self,bg='orange')
        f_top.pack(padx=230,anchor=NW)
        f_bottom=Frame(self).pack()
        
        #Top Frame
        Label(f_top,text='Batch Code : CPY-001',bg='orange',width=20).pack(pady=20,side=LEFT)
        Label(f_top,text='Faculty  : Kartik Khatri',bg='orange',width=20).pack(side=LEFT)
        Label(f_top,text='Month : January',bg='orange',width=20).pack(side=LEFT)
        Label(f_top,text='Date : 28 January 2020',bg='orange',width=20).pack(side=LEFT)
        # Middle Frame
        
        f_mid=Frame(self,height=100,width=1000,highlightbackground="black",highlightthickness=1)
        f_mid.pack()
        
        f_heading=Frame(f_mid,width=900)
        f_heading.pack(padx=1,pady=1)
        lWidth=20
        Label(f_heading,text="Rollno ",width=lWidth,borderwidth=2, relief="groove").pack(side=LEFT)
        Label(f_heading,text="Name ",width=lWidth,borderwidth=2, relief="groove").pack(side=LEFT)
        Label(f_heading,text="Attendance ",width=lWidth,borderwidth=2, relief="groove").pack(side=LEFT)
        Label(f_heading,text="Reason ",width=lWidth,borderwidth=2, relief="groove").pack(side=LEFT)
        Label(f_heading,text="Remarks ",width=lWidth,borderwidth=2, relief="groove").pack(side=LEFT)
        Label(f_heading,text=" ",width=lWidth,borderwidth=2, relief="groove").pack(side=LEFT)
        
        f_data=Frame(f_mid,width=900)
        f_data.pack()
        Label(f_data,text='HRFC-00001',width=lWidth,borderwidth=2, relief="groove").pack(side=LEFT)
        Label(f_data,text='Abhishek Tiwari',width=lWidth,borderwidth=2, relief="groove").pack(side=LEFT)
        ttk.Combobox(f_data,values=['Present','Absent','Leave'],width=lWidth).pack(side=LEFT,padx=1)
        ttk.Entry(f_data,text='Reason',width=lWidth+3).pack(side=LEFT,padx=1)
        ttk.Entry(f_data,text='Remarks',width=lWidth+3).pack(side=LEFT,padx=1)
        ttk.Button(f_data,text='Submit',width=lWidth+2).pack(side=LEFT,padx=1)
        #Bottom Frame



# root=Tk()
# root.geometry('1000x700')
# app=Daily_Attendance(root)
# # app.mainloop()
# root.mainloop()