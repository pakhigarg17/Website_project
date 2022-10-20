from tkinter import *
from tkinter import ttk
import  db

class Enquiry(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        # self.master = master
        # self.master.geometry("1000x700")
        w, h = self.winfo_screenwidth(), self.winfo_screenheight()
        self.geometry("%dx%d+0+0" % (w-10, h-10))
        self.configure(bg='orange')
        self.resizable(0,0)
        f_header=Frame(self,height=60,bg='orange')
        f_header.pack(fill=X)
        Label(f_header,text='Course Enquiry',font=['impact',30],fg='white',bg='orange').place(x=600,y=10)
        self.f_left=Frame(self,width=235,height=700,bg='orange')
        self.f_left.pack(side=LEFT,fill=Y)

        self.f_center1=Frame(self,highlightbackground="black",highlightthickness=1,bg='orange')
        self.f_center1.pack(side=LEFT)


        #Vertical Scrollbar
        # --- create canvas with scrollbar ---
        self.canvas = Canvas(self.f_center1,height=650,width=1100)
        self.canvas.pack(side=LEFT, anchor=N)

        self.scrollbar = ttk.Scrollbar(self.f_center1, command=self.canvas.yview)
        self.scrollbar.pack(side=RIGHT, fill='y')

        self.canvas.configure(yscrollcommand = self.scrollbar.set)

        # update scrollregion after starting 'mainloop'
        # when all widgets are in canvas
        
        self.canvas.bind('<Configure>', self.on_configure)

        self.f_center=Frame(self.canvas)
        self.f_center.pack(side=LEFT,fill=Y)
        # self.f_center.pack()
        self.canvas.create_window((0,0), window=self.f_center)
        self.f_center.bind("<Configure>",lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")
    )
)
        #Search Tab
        self.vFaculty=StringVar()
        self.vBatchTime=StringVar()
        self.vCourse=StringVar()
        self.vBatchCount=StringVar()
        self.vBatchCount.set('Total No. of Batches : 0')
        y1=10
        
        Label(self.f_left,text='Course Code  : ',bg='orange').place(x=10,y=10+y1)
        ttk.Combobox(self.f_left,width=27,values=db.get_course_detail(),textvariable=self.vCourse).place(x=10,y=40+y1)        
        
        Label(self.f_left,text='Batch Time  : ',bg='orange').place(x=10,y=70+y1)
        ttk.Combobox(self.f_left,width=27,values=db.slot_time('Weekday'),textvariable=self.vBatchTime).place(x=10,y=100+y1)
        
        Label(self.f_left,text='Faculty Name : ',bg='orange').place(x=10,y=130+y1)
        ttk.Combobox(self.f_left,width=27,values=db.get_faculty_info(),textvariable=self.vFaculty).place(x=10,y=160+y1)
        
        ttk.Button(self.f_left,text='Search',command=self.Search).place(x=120,y=350+y1)
        ttk.Button(self.f_left,text='Show All',command=self.show_all).place(x=20,y=350+y1)
        ttk.Button(self.f_left,text='Batch Info',command=self.update_batch_info).place(x=20,y=400+y1)
        ttk.Button(self.f_left,text='Clear',command=self.clear).place(x=120,y=400+y1)
        
        Label(self.f_left,text='Total No. of Batches : ',textvariable=self.vBatchCount,bg='orange').place(x=10,y=230+y1)
        
    def clear(self):
        self.vCourse.set('')
        self.vFaculty.set('')
        self.vBatchTime.set('')    
        self.vBatchCount.set('Total No. of Batches : 0')
    
    
    def on_configure(self,event):
            # update scrollregion after starting 'mainloop'
            # when all widgets are in canvas
            self.canvas.configure(scrollregion=self.canvas.bbox('all'))

    def Search(self,flag=''):

        for w in self.f_center.winfo_children():
            print(w)
            if isinstance(w,Frame):
                w.destroy()
        
        # self.f_batch1=Frame(self.f_center,highlightbackground="black",highlightthickness=1,height=100,width=100)
        # self.f_batch1.pack(side=TOP,padx=5,pady=5)
        # self.f_batch2=Frame(self.f_center,highlightbackground="black",highlightthickness=1,height=100,width=100)
        # self.f_batch2.pack(side=TOP,padx=5,pady=5)
        # self.f_batch3=Frame(self.f_center,highlightbackground="black",highlightthickness=1,height=100,width=100)
        # self.f_batch3.pack(side=TOP,padx=5,pady=5)
        # self.f_batch4=Frame(self.f_center,highlightbackground="black",highlightthickness=1,height=100,width=100)
        # self.f_batch4.pack(side=TOP,padx=5,pady=5)
        # self.f_batch5=Frame(self.f_center,highlightbackground="black",highlightthickness=1,height=100,width=100)
        # self.f_batch5.pack(side=TOP,padx=5,pady=5)
        # self.f_batch6=Frame(self.f_center,highlightbackground="black",highlightthickness=1,height=100,width=100)
        # self.f_batch6.pack(side=TOP,padx=5,pady=5)
        
        self.f_batch1=Frame(self.f_center)
        self.f_batch1.pack(side=TOP,padx=5,pady=5)
        self.f_batch2=Frame(self.f_center)
        self.f_batch2.pack(side=TOP,padx=5,pady=5)
        self.f_batch3=Frame(self.f_center)
        self.f_batch3.pack(side=TOP,padx=5,pady=5)
        self.f_batch4=Frame(self.f_center)
        self.f_batch4.pack(side=TOP,padx=5,pady=5)
        self.f_batch5=Frame(self.f_center)
        self.f_batch5.pack(side=TOP,padx=5,pady=5)
        self.f_batch6=Frame(self.f_center)
        self.f_batch6.pack(side=TOP,padx=5,pady=5)
        self.f_batch7=Frame(self.f_center)
        self.f_batch7.pack(side=TOP,padx=5,pady=5)
        self.f_batch8=Frame(self.f_center)
        self.f_batch8.pack(side=TOP,padx=5,pady=5)
        self.f_batch9=Frame(self.f_center)
        self.f_batch9.pack(side=TOP,padx=5,pady=5)
        self.f_batch10=Frame(self.f_center)
        self.f_batch10.pack(side=TOP,padx=5,pady=5)
        self.f_batch11=Frame(self.f_center)
        self.f_batch11.pack(side=TOP,padx=5,pady=5)
        
        if flag=='1':
            data=db.get_batch_info()
        else :        
            data=db.get_batch_info(self.vCourse.get(),self.vBatchTime.get(),self.vFaculty.get())
        # print(data)
        bCount=len(data)
        bCount='Total No. of Batches : ' + str(bCount)
        self.vBatchCount.set(bCount)
        i=0
        for rec in data:
            if i < 7:
                app=Batch(self.f_batch1,rec)
            elif i< 14:
                app=Batch(self.f_batch2,rec)
            elif i< 21:
                app=Batch(self.f_batch3,rec)
            elif i< 28:
                app=Batch(self.f_batch4,rec)
            elif i< 35:
                app=Batch(self.f_batch5,rec)
            elif i< 42:
                app=Batch(self.f_batch6,rec)
            elif i< 49:
                app=Batch(self.f_batch7,rec)
            elif i< 56:
                app=Batch(self.f_batch8,rec)
            elif i< 63:
                app=Batch(self.f_batch9,rec)
            elif i< 70:
                app=Batch(self.f_batch10,rec)
            else:
                app=Batch(self.f_batch11,rec)
            i=i+1    
        # print(self.scrollbar.get())
        # self.scrollbar.set('0.12','0.19')    
    def show_all(self):
        self.clear()
        self.Search('1')

    def update_batch_info(self):
        app=Update_Batch_Info()
        app.mainloop()

        
class Batch():
    def __init__(self,master,rec=''):
        self.master = master
        self.f1=Frame(self.master,highlightbackground="black",highlightthickness=1)
        self.f1.pack(side=LEFT,padx=15,pady=10)
        w=16
        # Label(self.f1,text='Faculty',width=w).pack(padx=2,pady=2)
        # Label(self.f1,text='Course Code',width=w).pack(padx=2,pady=2)
        # Label(self.f1,text='Batch Time',width=w).pack(padx=2,pady=2)
        # Label(self.f1,text='Strength',width=w).pack(padx=2,pady=2)
        # Label(self.f1,text='Status',width=w).pack(padx=2,pady=2)
        # Label(self.f1,text='Progress',width=w).pack(padx=2,pady=2)
        
        Label(self.f1,text=rec[1],width=w).pack(padx=2,pady=2)
        Label(self.f1,text=rec[2],width=w).pack(padx=2,pady=2)
        Label(self.f1,text=rec[3],width=w).pack(padx=2,pady=2)
        Label(self.f1,text=rec[4],width=w).pack(padx=2,pady=2)
        Label(self.f1,text=rec[6],width=w).pack(padx=2,pady=2)
        
        lblProgress=Label(self.f1,text='Progress',width=w)
        lblProgress.pack(fill=X)

        if int(rec[7]):
            # print('Active Batch : ',rec[7])
            lblProgress.config(bg='orange')
            lblProgress.bind("<Button-1>",lambda e : self.update_batch_info(rec))
            lblProgress.bind("<Enter>", lambda e: e.widget.config(fg='red'))
            lblProgress.bind("<Leave>", lambda e: e.widget.config(fg='black'))

        print(rec)

        
    def update_batch_info(self,rec):
        app=Update_Batch_Info(rec)
        app.mainloop()

class Update_Batch_Info(Toplevel):
    def __init__(self,rec=''):
        Toplevel.__init__(self)
        Label(self,text='Update Batch Info',font=[20]).pack()
        
        self.faculty_list=db.get_faculty_info()
        self.course_list=db.get_course_detail()
        self.batch_time=db.slot_time()
        self.status=['Start','Mid','End']
        
        self.vStrength=IntVar()
        self.vFaculty=StringVar()
        self.vCourse = StringVar()
        self.vProgress=StringVar()
        self.vStatus=StringVar()
        self.vBatchTime=StringVar()
        self.checkActive=StringVar()
       
    
        self.f1=Frame(self,height=400,width=400)
        self.f1.pack()
        Label(self.f1,text='Faculty Name :').place(x=10,y=10)
        self.cbFaculty=ttk.Combobox(self.f1,values=self.faculty_list,textvariable=self.vFaculty)
        self.cbFaculty.place(x=150,y=10)
        Label(self.f1,text='Course Code :').place(x=10,y=50)
        ttk.Combobox(self.f1,values=self.course_list,textvariable=self.vCourse).place(x=150,y=50)
        Label(self.f1,text='Batch Time :').place(x=10,y=100)
        self.cbBatchTime=ttk.Combobox(self.f1,values=self.batch_time,textvariable=self.vBatchTime)
        self.cbBatchTime.place(x=150,y=100)
        Label(self.f1,text='Strength :').place(x=10,y=150)
        ttk.Entry(self.f1,textvariable=self.vStrength).place(x=150,y=150)
        Label(self.f1,text='Status :').place(x=10,y=200)
        ttk.Combobox(self.f1,values=self.status,textvariable=self.vStatus).place(x=150,y=200)
        self.ActiveBatch=IntVar() 
        ttk.Checkbutton(self.f1, text ='Active', takefocus = 0,variable=self.ActiveBatch).place(x = 10, y = 250)         
        
        if len(rec)>0:
            print(rec)
            self.vStrength.set(rec[4])
            self.vFaculty.set(rec[1])
            self.vCourse.set(rec[3])
            # self.vProgress.set(rec[5])
            self.vStatus.set(rec[6])
            self.vBatchTime.set(rec[2])
            self.cbBatchTime.configure(state=DISABLED)
            self.cbFaculty.configure(state=DISABLED)
            self.ActiveBatch.set(rec[7])
        ttk.Button(self.f1,text='Update',width=15,command=self.update_info).place(x=150,y=300)


    def update_info(self):
        course=self.vCourse.get()
        faculty=self.vFaculty.get()
        batch_time=self.vBatchTime.get()
        strength=self.vStrength.get()
        status=self.vStatus.get()
        active=self.ActiveBatch.get()
        
        db.update_batch_info_data(faculty,batch_time,course,strength,status,active)
        # print('Check Button Status : ',self.ActiveBatch.get())

# root=Tk()
# # Button(root,text='Enquiry Form')
# app=Enquiry(root)
# # app.mainloop()
# root.mainloop()
