from tkinter import *
from tkinter import ttk
from tkinter import  messagebox
from tkcalendar import Calendar, DateEntry
from PIL import Image,ImageTk
import db
import Attendance
# import Prog_Fee_Form
class StudentRecord(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        w, h = self.winfo_screenwidth(), self.winfo_screenheight()
        self.geometry("%dx%d+0+0" % (w, h))
        self.resizable(0,0)
        # self.f_Record=Frame(self)
        # self.f_Record.pack()
        
        # for r in lst:
        #     Label(self.f_Record,text=r,width=lWidth,borderwidth=2, relief="groove").pack(side=LEFT)
        # self.btnSelect = ttk.Button(self.f_Record,width=lWidth+1,text='Select',command=lambda : self.select_record(lst)).pack()

        # self
        self.rollno=""
        self.vRollno=StringVar()
        self.vName = StringVar()
        self.vCourse = StringVar()
        self.vFaculty=StringVar()
        
        self.f_header=Frame(self,highlightbackground="black",highlightthickness=1)
        self.f_header.pack(fill=X,padx=1,pady=1)

        self.f_footer=Frame(self,bg='blue',height=20)
        self.f_footer.pack(side=BOTTOM,padx=1,pady=1,fill=X)

        self.f_left=Frame(self,width=300,bg='orange',highlightbackground="black",highlightthickness=1)
        self.f_left.pack(side=LEFT,fill=Y,padx=1,pady=1)

        self.f_center=Frame(self)
        self.f_center.pack(side=LEFT,padx=5,pady=2,fill=Y)

        self.f_right=Frame(self,bg='orange',width=300,highlightbackground="black",highlightthickness=1)
        self.f_right.pack(side=LEFT,fill=Y,padx=1,pady=1)

        Label(self.f_header,text='All Student Information',font=['',15,'bold']).pack(padx=5,pady=5)
        Label(self.f_footer,text='All Student Information',font=['',15,'bold']).pack(padx=5,pady=5)


        #Heading
        lWidth=12
        f_heading=Frame(self.f_center)
        f_heading.pack()

        Label(f_heading,text='Roll No',width=lWidth,borderwidth=2, relief="groove").pack(side=LEFT)
        Label(f_heading,text='Name',width=lWidth,borderwidth=2, relief="groove").pack(side=LEFT)
        Label(f_heading,text='Course',width=lWidth,borderwidth=2, relief="groove").pack(side=LEFT)
        Label(f_heading,text='Batch Code',width=lWidth,borderwidth=2, relief="groove").pack(side=LEFT)
        Label(f_heading,text='Batch Time',width=lWidth,borderwidth=2, relief="groove").pack(side=LEFT)
        Label(f_heading,text='Faculty',width=lWidth,borderwidth=2, relief="groove").pack(side=LEFT)
        Label(f_heading,text='Batch Start',width=lWidth,borderwidth=2, relief="groove").pack(side=LEFT)
        Label(f_heading,text='Attendance',width=lWidth,borderwidth=2, relief="groove").pack(side=LEFT)
        Label(f_heading,text='Progress',width=lWidth,borderwidth=2, relief="groove").pack(side=LEFT)
        Label(f_heading,text='Remarks',width=lWidth,borderwidth=2, relief="groove").pack(side=LEFT)

        self.show_all()
        #Search Tab
        y1=10
        Label(self.f_left,text="Search Student Record",width=28).pack(padx=10,pady=10)
        Label(self.f_left,text='Rollno  : ',bg='orange').place(x=10,y=25+y1)
        ttk.Entry(self.f_left,width=30,textvariable=self.vRollno).place(x=10,y=50+y1)
        Label(self.f_left,text='Student Name : ',bg='orange').place(x=10,y=75+y1)
        ttk.Entry(self.f_left,width=30,textvariable=self.vName).place(x=10,y=100+y1)

        Label(self.f_left,text='Course Code  : ',bg='orange').place(x=10,y=125+y1)
        ttk.Combobox(self.f_left,width=27,values=db.get_course_detail(),textvariable=self.vCourse).place(x=10,y=150+y1)        
        Label(self.f_left,text='Batch Code : ',bg='orange').place(x=10,y=175+y1)
        ttk.Entry(self.f_left,width=30).place(x=10,y=200+y1)

        Label(self.f_left,text='Batch Time  : ',bg='orange').place(x=10,y=225+y1)
        ttk.Combobox(self.f_left,width=27,values=db.slot_time('Weekday')).place(x=10,y=250+y1)
        Label(self.f_left,text='Faculty Name : ',bg='orange').place(x=10,y=275+y1)
        ttk.Combobox(self.f_left,width=27,values=db.get_faculty_info()).place(x=10,y=300+y1)
        ttk.Button(self.f_left,text='Search',command=self.Search_Student_Record).place(x=120,y=350+y1)
        ttk.Button(self.f_left,text='Show All',command=self.show_all).place(x=20,y=350+y1)
    
    def Search_Student_Record(self):
        sql=""
        if len(self.vRollno.get()) > 0 :
            sql=f"Select regno,name,course,dob,contact,address,qualification,regdate,gender from student_info where regno='{self.vRollno.get()}'"
        elif len(self.vName.get()) > 0:    
            sql=f"Select regno,name,course,dob,contact,address,qualification,regdate,gender from student_info where name='{self.vName.get()}'"
        elif len(self.vCourse.get()) > 0:
            sql=f"Select regno,name,course,dob,contact,address,qualification,regdate,gender from student_info where course='{self.vCourse.get()}'"
        
        self.show_all(sql)
    
 
    def callback(event):
        print("clicked at", event.x, event.y)

    def Show_Attendance(self,rec):
        print('Show Attendance')
        rollno='HRFC-00001'
        # for w in self.f_center.winfo_children():
        #     w.destroy()
        app=Attendance.Attendance(rec)
        app.mainloop()



    def show_all(self,sql=""):
        i=0    
        for w in self.f_center.winfo_children():
            print(w)
            if i > 0:
                w.destroy()
            i=i+1    
        print('Show all start')
        if sql == "":
            sql="Select regno,name,course,dob,contact,address,qualification,regdate,gender from student_info"
        # print(sql)
        student_list=db.get_data(sql)
        i=-1
        for rec in student_list:
            i=i+1
            self.f_Record=Frame(self.f_center)
            self.f_Record.pack()
            for r in rec: 
                Label(self.f_Record,text=r,width=12,borderwidth=2, relief="groove").pack(side=LEFT)
        
            app=Show_all_Student(self.f_Record,rec,self.select_record)            
        Label(self.f_left,text=f'Total No. Records : {len(student_list)}',bg='orange').place(x=10,y=400)
        self.select_record(student_list[0])
        print('Show all end')
        
    def clear_f_right_frame(self):
        for w in self.f_right.winfo_children():
            w.destroy()
    
    def select_record(self,rec):
        print("Record : ",rec)
        #Student Info
        self.rollno=rec[0]
        self.clear_f_right_frame()
        Label(self.f_right,text="Student Info",width=40).pack(padx=10,pady=10)
        self.pic = ImageTk.PhotoImage(file=f'.\images\{rec[0]}.jpg')
        Label(self.f_right,image=self.pic).pack()
        Label(self.f_right,text=rec[0],width=10,bg='orange').pack(padx=10,pady=5)
        Label(self.f_right,text=rec[1],width=20,bg='orange').pack(padx=10,pady=5)
        Label(self.f_right,text=rec[2],width=10,bg='orange').pack(padx=10,pady=5)
        Label(self.f_right,text=rec[3],width=20,bg='orange').pack(padx=10,pady=5)

        lblAttendance=Label(self.f_right,text='Attendance %',width=20,bg='orange')
        lblAttendance.pack(padx=10,pady=5)
        lblAttendance.bind("<Button-1>",lambda e : self.Show_Attendance(rec))
        lblAttendance.bind("<Enter>", lambda e: e.widget.config(fg='white'))
        lblAttendance.bind("<Leave>", lambda e: e.widget.config(fg='black'))

        lblResult=Label(self.f_right,text='Result',width=20,bg='orange')
        lblResult.pack(padx=10,pady=5)
        lblResult.bind("<Button-1>", self.callback)
        lblResult.bind("<Enter>", lambda e: e.widget.config(fg='white'))
        lblResult.bind("<Leave>", lambda e: e.widget.config(fg='black'))

        lblFee=Label(self.f_right,text='Fee Info',width=20,bg='orange')
        lblFee.pack(padx=10,pady=5)
        lblFee.bind("<Button-1>", self.callback)
        lblFee.bind("<Enter>", lambda e: e.widget.config(fg='white'))
        lblFee.bind("<Leave>", lambda e: e.widget.config(fg='black'))

        lblFee=Label(self.f_right,text='Update Student Info',width=20,bg='orange')
        lblFee.pack(padx=10,pady=5)
        lblFee.bind("<Button-1>", self.callback)
        lblFee.bind("<Enter>", lambda e: e.widget.config(fg='white'))
        lblFee.bind("<Leave>", lambda e: e.widget.config(fg='black'))

    
class Show_all_Student():
    def __init__(self,master,rec,func):
        self=master
        self.btnSelect = ttk.Button(self,width=12+1,text='Select',command=lambda : func(rec)).pack()



# root=Tk()
# # self.geometry('1366x700')
# # self.attributes('-fullscreen', True)
# # w, h = self.winfo_screenwidth(), self.winfo_screenheight()
# # self.geometry("%dx%d+0+0" % (w, h))
# # self.resizable(0,0)
# app=StudentRecord()
# root.mainloop()