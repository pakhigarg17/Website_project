import os
from tkinter import filedialog
from tkinter import ttk
from tkinter import *
from PIL import Image ,ImageTk
import db
from tkcalendar import Calendar, DateEntry

class Registration(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        w, h = self.winfo_screenwidth(), self.winfo_screenheight()
        self.geometry("%dx%d+0+0" % (w-10, h-10))
        self.configure(bg='orange')
        self.resizable(0,0)
        self.title("Student Registration Form")
        self.resizable(0,0)
        self.protocol("WM_DELETE_WINDOW",self.onClosingRegistrationForm)

        self.frameTop = Frame(self,bg="orange",bd=1)
        self.frameTop.pack(fill=X)
        
        self.frameMid=Frame(self,bg="orange",bd=1)
        self.frameMid.pack(fill=X)
        
        
        
        
        self.frameCenter=Frame(self.frameMid)
        self.frameCenter.pack()
        self.frameCenter.configure(highlightbackground="black",highlightthickness=1)

        self.frameBottom = Frame(self.frameCenter,bg="white",bd=1,height=45)
        self.frameBottom.pack(side=BOTTOM,fill=X)
        self.frameBottom.configure(highlightbackground="black",highlightthickness=0)

        self.frame1 = Frame(self.frameCenter,height=550,width=350)
        self.frame1.pack(side=LEFT,fill=Y)
        # self.frame1.configure(highlightbackground="black",highlightthickness=1)
        
        self.frame3 = Frame(self.frameCenter,height=550,width=350)
        self.frame3.pack(side=LEFT,fill=Y)
        # self.frame3.configure(highlightbackground="black",highlightthickness=1)
        
        
        self.frame2 = Frame(self.frameCenter,height=550,width=250)
        self.frame2.pack(side=LEFT,fill=Y)
        # self.frame2.configure(highlightbackground="black",highlightthickness=1)
       

        lblTop=Label(self.frameTop,text="Student Registration",font=("impact", 30),bg="orange")
        lblTop.pack(padx=10,pady=10)

#         global tmpimgpath, pic

        self.y1=30
        self.vRegno          = StringVar()
        self.vName           = StringVar()
        self.vDob            = StringVar()
        self.vCourse         = StringVar()
        self.vRegDate        = StringVar()
        self.vQualification  = StringVar()
        self.vContact        = StringVar()
        self.vAddress        = StringVar()


        self.regno=db.get_regno()+1
        self.vRegno.set("HRFC-0000"+str(self.regno))


#         ############################## 

# # Rigth Frame
        self.lblPhotoUpload=LabelFrame(self.frame2,text='Student Photo')
        self.lblPhotoUpload.place(x=20,y=20,width=210,height=520)

        self.pic = ImageTk.PhotoImage(file=".\images\emp10.jpg")
        self.PictureLabel= Label(self.lblPhotoUpload,image=self.pic,height=150,width=150,borderwidth=2, relief="solid")
        self.PictureLabel.place(x=25,y=20)
        self.btnUpload=ttk.Button(self.lblPhotoUpload,text="Upload Image",command=self.uploadPhoto,width=24).place(x=25,y=180)

## Bottom Frame
        self.btnClear=ttk.Button(self.frameBottom,text="Clear",command=self.reset_form,width=10).place(x=300,y=10)
        self.btnSubmit=ttk.Button(self.frameBottom,text="Submit",command=self.uploadData,width=10).place(x=400,y=10)

## Left 
        
        self.lblStudentInfo=LabelFrame(self.frame1,text='Student Info')
        self.lblStudentInfo.place(x=20,y=20,width=320,height=520)

        Label(self.lblStudentInfo,text="Reg No : ").place(x=10,y=20, height=25)
        ttk.Entry(self.lblStudentInfo,width=25,textvariable=self.vRegno,state=DISABLED).place(x=150,y=20,height=25)
        
        Label(self.lblStudentInfo,text="Name : ",width=15, anchor=W).place(x=10,y=70, width=120, height=25)
        ttk.Entry(self.lblStudentInfo,width=25,textvariable=self.vName).place(x=150,y=70, height=25)
        
        Label(self.lblStudentInfo,text="DOB : ",width=15, anchor=W).place(x=10,y=120)
        self.calDob=DateEntry(self.lblStudentInfo, width=25-3, background='darkblue',foreground='white', borderwidth=2)
        self.calDob.place(x=150,y=120, height=25)
        
        Label(self.lblStudentInfo,text="Contact : ",width=15, anchor=W).place(x=10,y=170, height=25)
        ttk.Entry(self.lblStudentInfo,width=25,textvariable = self.vContact).place(x=150,y=170, height=25)
        
        Label(self.lblStudentInfo,text="Residential Address : ",width=15, anchor=W).place(x=10,y=220, height=25)
        ttk.Entry(self.lblStudentInfo,width=25,textvariable=self.vAddress).place(x=150,y=220, height=25)
        
        Label(self.lblStudentInfo,text="Permanent Address : ",width=15, anchor=W).place(x=10,y=270, height=25)
        ttk.Entry(self.lblStudentInfo,width=25,textvariable=self.vQualification).place(x=150,y=270, height=25)
        
        Label(self.lblStudentInfo,text="Course : ",width=15, anchor=W).place(x=10,y=320, height=25)
        ttk.Combobox(self.lblStudentInfo,width=22,values=db.get_course_detail(),textvariable=self.vCourse).place(x=150,y=320, height=25)

        
        Label(self.lblStudentInfo,text="Reg. Date : ",width=15, anchor=W).place(x=10,y=370, height=25)
        self.calReg=DateEntry(self.lblStudentInfo, width=25-3, background='darkblue',foreground='white', borderwidth=2)
        self.calReg.place(x=150,y=370, height=25)
        
        Label(self.lblStudentInfo,text="Gender : ",width=15, anchor=W).place(x=10,y=420, height=25)
        self.vGender = StringVar()
        self.vGender.set('') 

        ttk.Radiobutton(self.lblStudentInfo, text='Male', variable=self.vGender, value='Male').place(x=150,y=420, height=25)
        ttk.Radiobutton(self.lblStudentInfo, text='Female', variable=self.vGender, value='Female').place(x=220,y=420, height=25)

        ##################################

    # Frame3 About Father/Guaridan and Last Qualification
        self.lblF1=LabelFrame(self.frame3,text='About Father/Guardian ')
        self.lblF1.place(x=10,y=20,width=340,height=250)

        self.vFName=StringVar()
        self.vFOccupation=StringVar()
        self.vFOfficeAddress=StringVar()
        self.vFContact=StringVar()

        Label(self.lblF1,text='Name : ').place(x=10,y=20)
        ttk.Entry(self.lblF1,width=25,textvariable=self.vFName).place(x=150,y=20,height=25)
        Label(self.lblF1,text='Occupation : ').place(x=10,y=70)
        ttk.Entry(self.lblF1,width=25,textvariable=self.vFOccupation).place(x=150,y=70,height=25)
        Label(self.lblF1,text='Office Address : ').place(x=10,y=120)
        ttk.Entry(self.lblF1,width=25,textvariable=self.vFOfficeAddress).place(x=150,y=120,height=25)
        Label(self.lblF1,text='Contact : ').place(x=10,y=170)
        ttk.Entry(self.lblF1,width=25,textvariable=self.vFContact).place(x=150,y=170,height=25)
        
        
    # Frame3 About Father/Guaridan and Last Qualification
        self.lblF2=LabelFrame(self.frame3,text='About Last Qualification ')
        self.lblF2.place(x=10,y=290,width=340,height=250)

        self.vInstitute=StringVar()
        self.vExamination=StringVar()
        self.vYearofPassing=StringVar()
        self.vPercentage=StringVar()
        
        Label(self.lblF2,text='Name of the institute : ').place(x=10,y=20)
        ttk.Entry(self.lblF2,width=25,textvariable=self.vInstitute).place(x=150,y=20,height=25)
        Label(self.lblF2,text='Examination : ').place(x=10,y=70)
        ttk.Entry(self.lblF2,width=25,textvariable=self.vExamination).place(x=150,y=70,height=25)
        Label(self.lblF2,text='Year of Passing : ').place(x=10,y=120)
        ttk.Entry(self.lblF2,width=25,textvariable=self.vYearofPassing).place(x=150,y=120,height=25)
        Label(self.lblF2,text='Percentage : ').place(x=10,y=170)
        ttk.Entry(self.lblF2,width=25,textvariable=self.vPercentage).place(x=150,y=170,height=25)
        
    
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
        self.vGender.set('')
        self.vInstitute.set("")
        self.vExamination.set("")
        self.vYearofPassing.set("")
        self.vPercentage.set("")
        self.vFName.set("")
        self.vFOccupation.set("")
        self.vFOfficeAddress.set("")
        self.vFContact.set("")
    

    def uploadPhoto(self):
        tmpimgpath = filedialog.askopenfilename(initialdir=os.getcwd())
        global selectedpicture
        selectedpicture = ImageTk.PhotoImage(file=tmpimgpath)   
        self.PictureLabel.configure(image=selectedpicture)



    def uploadData(self):
        
        record=[
        self.vRegno.get(),
        self.vName.get(),
        self.calDob.get_date(),
        self.vContact.get(),
        self.vAddress.get(),
        self.vQualification.get(),
        self.vCourse.get(),
        self.calReg.get_date(),
        self.vGender.get(),        
        self.vInstitute.get(),
        self.vExamination.get(),
        self.vYearofPassing.get(),
        self.vPercentage.get(),
        self.vFName.get(),
        self.vFOccupation.get(),
        self.vFOfficeAddress.get(),
        self.vFContact.get(),    
        ]
        
        print('Record List : ',record)
        rowcount = db.insert_data(record)
        
        
        
        
        if rowcount > 0:
            self.reset_form()
            # self.destroy()
        else :
            pass    
    
    def submit(self):
        pass
    def onClosingRegistrationForm(self):
        print("Registration Form Closed")    
        self.destroy()
