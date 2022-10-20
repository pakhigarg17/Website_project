from tkinter import *
from tkinter import ttk
from tkinter import  messagebox
from PIL import Image,ImageTk
import  db
from Prog_Enquiry_Form import *
from Prog_Show_All_Student import *
from Prog_Registration import Registration
from Prog_Daily_Attendance import *

class Dasboard():
    def __init__(self,master,pic,rec):
        self.master = master
        self.f1=Frame(self.master,bg='orange',highlightbackground="black",highlightthickness=1)
        self.f1.pack(side=LEFT,padx=100,pady=20)
        self.pic = pic        
        self.lblImage=Label(self.f1,image=self.pic)
        self.lblImage.pack()
        # self.lblItem=Label(self.f1,text="Image").pack()
        # print(img_name)
        self.lblImage.bind("<Button-1>",lambda e : self.show_info(rec))
        self.lblImage.bind("<Enter>", lambda e: e.widget.config(fg='white'))
        self.lblImage.bind("<Leave>", lambda e: e.widget.config(fg='black'))

    def show_info(self,rec):
        # messagebox.showinfo('Dashboard',rec[1])
        if int(rec[0]) == 1:
            app=Enquiry()
        elif int(rec[0]) == 2:
            app=Registration()
        elif int(rec[0]) == 3:
            app=StudentRecord()
        elif int(rec[0]) == 4:
            pass        
        elif int(rec[0]) == 5:
            app=Daily_Attendance()
        elif int(rec[0]) == 6:
            pass
        else:
            pass



class Dashboard_Root(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        w, h = self.winfo_screenwidth(), self.winfo_screenheight()
        self.geometry("%dx%d+0+0" % (w-10, h-10))
        self.configure(bg='orange')
        self.resizable(0,0)

        f0=Frame(self,bg='orange')
        f0.pack(side=TOP)
                
        f1=Frame(self,bg='orange')
        f1.pack(side=TOP)
        f2=Frame(self,bg='orange')
        f2.pack(side=TOP)
        f3=Frame(self,bg='orange')
        f3.pack(side=TOP)
        f4=Frame(self,bg='orange')
        f4.pack(side=TOP)

        Label(f0,text='Balbhawan Dashboard',bg='orange',fg='white',font=['impact',45]).pack(pady=10)
        pic=[]
        data=db.get_dashboard()
        # print(data)
        i=0
        for rec in data:
            pic.append(ImageTk.PhotoImage(file=f'.\images\{rec[2]}'))
            if i < 2:
                app=Dasboard(f1,pic[i],data[i])
            elif i < 4:
                app=Dasboard(f2,pic[i],data[i])
            elif i < 6:
                app=Dasboard(f3,pic[i],data[i])
            else:
                app=Dasboard(f4,pic[i],data[i])
            
            i=i+1
# root=Tk()
# app=Dashboard_Root()
# root.mainloop()


