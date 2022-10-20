import os
from tkinter import filedialog
from tkinter import ttk
from tkinter import *
from tkcalendar import DateEntry
from PIL import Image ,ImageTk
import db

class Registration():
    def __init__(self,master):
        self.master = master
        self.frame0 = Frame(self.master,bg="green",bd=1)
        self.frame0.grid(row=0,columnspan=2)
        self.frame0.configure(highlightbackground="black",highlightthickness=1,height="50",width="500")
        self.frame0.grid_propagate(0)
        # self.geometry("500x500")
        # self.title("Student Registration Form")
        # self.resizable(0,0)
        # self.protocol("WM_DELETE_WINDOW",self.onClosingRegistrationForm)
    
        self.frame1 = Frame(self.master)
        self.frame1.grid(row=1,column=0)
        self.frame1.configure(highlightbackground="white",highlightthickness=0,height="260",width="300")
        self.frame1.grid_propagate(0)

        self.frame2 = Frame(self.master)
        self.frame2.grid(row=1,column=1)
        self.frame2.configure(highlightbackground="black",highlightthickness=0,height="260",width="200")
        self.frame2.grid_propagate(0)

        self.frameBottom2 = Frame(self.master,bd=1)
        self.frameBottom2.grid(row=2,columnspan=2)
        self.frameBottom2.configure(highlightbackground="black",highlightthickness=0,height="160",width="500")
        self.frameBottom2.grid_propagate(0)
        
        self.frameBottom = Frame(self.master,bg="white",bd=1)
        self.frameBottom.grid(row=3,columnspan=2)
        self.frameBottom.configure(highlightbackground="black",highlightthickness=0,height="30",width="500")
        self.frameBottom.grid_propagate(0)


        lblTop=Label(self.frame0,text="Faculty Registration Form",font=("Helvetica", 17),bg="green",width=40).place(x=0,y=10)

#         global tmpimgpath, pic

        self.y1=15
        self.vRegno          = StringVar()
        self.vName           = StringVar()
        self.vDob            = StringVar()
        self.vCourse         = StringVar()
        self.vRegDate        = StringVar()
        self.vQualification  = StringVar()
        self.vContact        = StringVar()
        self.vAddress        = StringVar()


        self.regno=db.get_regno()+1
        self.vRegno.set("HRFC-000"+str(self.regno))


#         ############################## 

# # Rigth Frame
        self.pic = ImageTk.PhotoImage(file=".\images\emp10.jpg")
        self.PictureLabel= Label(self.frame2,image=self.pic,height=150,width=150,highlightbackground="black",highlightthickness=2)
        self.PictureLabel.place(x=25,y=10)
        self.btnUpload=Button(self.frame2,text="Upload Image",command=self.uploadPhoto).place(x=50,y=200)

## Bottom Frame
        self.btnClear=Button(self.frameBottom,text="Clear",command=self.reset_form,width=10).place(x=150)
        self.btnSubmit=Button(self.frameBottom,text="Submit",command=self.uploadData,width=10).place(x=250)

#        
## Left Frame
        lblRegno = Label(self.frame1,text="Reg No : ",width=15, anchor=W).place(x=10,y=0+self.y1)
        txtRegno = Entry(self.frame1,width=25,textvariable=self.vRegno,state=DISABLED).place(x=150,y=0+self.y1)

        self.lblName = Label(self.frame1,text="Name : ",width=15, anchor=W).place(x=10,y=25+self.y1)
        self.txtName = Entry(self.frame1,width=25,textvariable=self.vName).place(x=150,y=25+self.y1)
        self.lblDob = Label(self.frame1,text="DOB : ",width=15, anchor=W).place(x=10,y=50+self.y1)
        # self.txtDob = Entry(self.frame1,width=25,textvariable=self.vDob).place(x=150,y=50+self.y1)
        cal = DateEntry(self.frame1, width=22, background='darkblue',foreground='white', borderwidth=2)
        cal.place(x=150,y=50+self.y1)
        self.lblContact = Label(self.frame1,text="Contact : ",width=15, anchor=W).place(x=10,y=75+self.y1)
        self.txtContact = Entry(self.frame1,width=25,textvariable = self.vContact).place(x=150,y=75+self.y1)

        self.lblAddress = Label(self.frame1,text="Address : ",width=15, anchor=W).place(x=10,y=100+self.y1)
        self.txtAddress = Entry(self.frame1,width=25,textvariable=self.vAddress).place(x=150,y=100+self.y1)
        self.lblQualification = Label(self.frame1,text="Qualification : ",width=15, anchor=W).place(x=10,y=125+self.y1)
        self.txtQualification = Entry(self.frame1,width=25,textvariable=self.vQualification).place(x=150,y=125+self.y1)
        # self.lblCourse = Label(self.frame1,text="Course : ",width=15, anchor=W).place(x=10,y=150+self.y1)
        # txtCourse = Entry(self.frame1,width=25).place(x=150,y=150+self.y1)
        # self.cbCourse = ttk.Combobox(self.frame1,width=21,values=["Basic","Tally","Core Java","Python"],textvariable=self.vCourse).place(x=150,y=150 + self.y1)

        self.lblRegDate = Label(self.frame1,text="Reg. Date : ",width=15, anchor=W).place(x=10,y=175+self.y1)
        self.txtRegDate = Entry(self.frame1,width=25,textvariable=self.vRegDate).place(x=150,y=175+self.y1)


        self.lblGender = Label(self.frame1,text="Gender : ",width=15, anchor=W).place(x=10,y=200+self.y1)
        self.vGender = IntVar() 
        Radiobutton(self.frame1, text='Male', variable=self.vGender, value=1).place(x=150,y=200+self.y1)
        Radiobutton(self.frame1, text='Female', variable=self.vGender, value=2).place(x=220,y=200+self.y1)
        # Course Details 
        self.lblCourse = Label(self.frame1,text="Course : ",width=15, anchor=W).place(x=10,y=225+self.y1)

        coursePaneWindow1=ttk.Panedwindow(self.frameBottom2)
        coursePaneWindow1.place(x=10,y=0+self.y1)
        coursePaneWindow2=ttk.Panedwindow(self.frameBottom2)
        coursePaneWindow2.place(x=150,y=0+self.y1)
        coursePaneWindow3=ttk.Panedwindow(self.frameBottom2)
        coursePaneWindow3.place(x=300,y=0+self.y1)
        self.lstCourses=db.get_course_detail()
        i=0
        self.lstCVar=[]
        for c_name in self.lstCourses:
            # print(c_name)
            self.lstCVar.append(IntVar())
            if i < 6:
                # self.lstCourses.append(ttk.Checkbutton(coursePaneWindow1,text=c_name,width=20,variable=self.lstCVar[i]).pack(padx=5))
                ttk.Checkbutton(coursePaneWindow1,text=c_name,width=20,variable=self.lstCVar[i]).pack(padx=5)
            elif i < 12:
                # self.lstCourses.append(ttk.Checkbutton(coursePaneWindow2,text=c_name,width=20,variable=self.lstCVar[i]).pack(padx=5))
                ttk.Checkbutton(coursePaneWindow2,text=c_name,width=20,variable=self.lstCVar[i]).pack(padx=5)
            elif i < 18:
                # self.lstCourses.append(ttk.Checkbutton(coursePaneWindow3,text=c_name,width=20,variable=self.lstCVar[i]).pack(padx=5))
                ttk.Checkbutton(coursePaneWindow3,text=c_name,width=20,variable=self.lstCVar[i]).pack(padx=5)
            i=i+1

        ##################################

    def reset_photo(self):
        global pic
        pic = ImageTk.PhotoImage(file=".\images\emp10.jpg")
        self.PictureLabel.configure(image=pic)

    def reset_form(self):
        regno=db.get_regno()+1
        self.vRegno.set("HRFC-000"+str(regno))
        self.vName.set("")
        self.vDob.set("")
        self.vCourse.set("")
        self.vRegDate.set("")
        self.vQualification.set("")
        self.vContact.set("")
        self.vAddress.set("")
        self.reset_photo()


    def uploadPhoto(self):
        tmpimgpath = filedialog.askopenfilename(initialdir=os.getcwd())
        global selectedpicture
        selectedpicture = ImageTk.PhotoImage(file=tmpimgpath)   
        self.PictureLabel.configure(image=selectedpicture)



    def uploadData(self):
        i=0
        courses=[]
        for w in self.lstCVar:
            if w.get():
                courses.append(self.lstCourses[i])
            i=i+1    
        courses=','.join(courses)    
        print('Course Seleted : ',courses)
        
        # rowcount = db.insert_data(self.vName.get(),self.vDob.get(),self.vContact.get(),self.vAddress.get(),self.vQualification.get(),self.vCourse.get(),self.vRegDate.get(),self.vGender.get())
        # if rowcount > 0:
        #     self.reset_form()
        #     self.destroy()
        # else :
        #     pass    
    
    def submit(self):
        pass
    def onClosingRegistrationForm(self):
        print("Registration Form Closed")    
        self.destroy()

root=Tk()
root.geometry("500x600")
root.resizable(0,0)
app = Registration(root)
root.mainloop()