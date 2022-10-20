 # from tkinter import Tk
from Prog_Jan_Attendance import *
from tkinter import *
from tkinter import ttk
class dateFrame():
    def __init__(self,master):
        self.master = master
        self.f1=Frame(self.master,highlightbackground="black",highlightthickness=1)
        self.f1.pack(side=LEFT,padx=1,pady=1)
        self.lblR1=Label(self.f1,text='00',width=10)
        self.lblR1.pack()
        self.lblR2=Label(self.f1,text='Present')
        self.lblR2.pack()
        self.lblR3=Label(self.f1,text='')
        self.lblR3.pack()
    def get_attendance(self,attendance):
        if attendance[1]=='Absent'or attendance[1]=='Leave':
            self.lblR1.configure(fg="red")
            self.lblR2.configure(fg="red")
            self.lblR3.configure(fg="red")
        if attendance[2]=='weekoff':
            self.lblR1.configure(fg="grey")
            self.lblR2.configure(fg="grey")
            self.lblR3.configure(fg="grey")
        if attendance[2]=='Holiday':
            self.lblR1.configure(fg="blue")
            self.lblR2.configure(fg="blue")
            self.lblR3.configure(fg="blue")
            
        self.lblR1.configure(text=attendance[0])
        self.lblR2.configure(text=attendance[1])
        self.lblR3.configure(text=attendance[2])

class Attendance(Toplevel):
    def __init__(self,rec):
        Toplevel.__init__(self)
        self.geometry("700x600")
        self.resizable(0,0)
        self.regno=rec[0]
        self.vMonth=StringVar()
        self.vMonth.set('January')
        f0=Frame(self,width=700,height=120)
        f0.pack(fill=X)
        self.months=['January','February','March','April','May','June','July','August','September','October','November','December']    
        pX=5
        pY=5    
        Label(f0,text=f"Student Attendance",font=[30]).place(x=300,y=10)
        
        Label(f0,text=f"Month").place(x=550,y=70)
        ttk.Combobox(f0,values=self.months,textvariable=self.vMonth,width=10).place(x=550,y=90)
        Label(f0,text=f"Roll no : {rec[0]}").place(x=70,y=70)
        Label(f0,text=f"Student Name : {rec[1]}").place(x=70,y=90)
        Label(f0,text=f"Batch Code : CPY-101").place(x=300,y=70)
        Label(f0,text=f"Course Name : {rec[2]}").place(x=300,y=90)
        # ttk.Combobx(f0,values=[""]).grid(row=0,column=0)

        f1=Frame(self)
        f1.pack()
        f2=Frame(self)
        f2.pack()
        f3=Frame(self)
        f3.pack()
        f4=Frame(self)
        f4.pack()
        f5=Frame(self)
        f5.pack()

        # global attendance
        attendance=[]
        for i in range(35):
            if i < 7:
                att=dateFrame(f1)
                attendance.append(att)
            elif i < 14:
                att=dateFrame(f2)
                attendance.append(att)
            elif i < 21:
                    att=dateFrame(f3)
                    attendance.append(att)
            elif i < 28:
                    att=dateFrame(f4)
                    attendance.append(att)
            else:
                att=dateFrame(f5)
                attendance.append(att)

        print("Attendance Start")
        jan_att,weekday,lastday=Jan_Attendance(1,2020)
        i=weekday
        blank=('','','')

        for b in range(weekday):
            attendance[b].get_attendance(blank)

        for b in range(lastday,35):
            attendance[b].get_attendance(blank)

        for day in jan_att:
            attendance[i].get_attendance(day)
            i=i+1 


        f6=Frame(self,height=100,width=700)
        f6.pack()

        Label(f6,text='Total No of Present : ').place(x=70,y=10)   
        Label(f6,text='Total No of Absent : ').place(x=70,y=30)  
        Label(f6,text='Total No of Leave : ').place(x=70,y=50)    
        Label(f6,text='Attendance Percentage : ').place(x=70,y=70)    
# root=Tk()
# app=Attendance()
# app.mainloop()
# root.mainloop()
