# from tkinter import Tk
from tkinter import *
from tkinter import ttk
from tkinter import  messagebox
from tkcalendar import Calendar, DateEntry
import db
class HorizontalScrolledFrame(Frame):
    """A pure Tkinter scrollable frame that actually works!
    * Use the 'interior' attribute to place widgets inside the scrollable frame
    * Construct and pack/place/grid normally
    * This frame only allows vertical scrolling

    """
    def __init__(self, parent, *args, **kw):
        Frame.__init__(self, parent, *args, **kw)            

        # create a canvas object and a vertical scrollbar for scrolling it
        vscrollbar = Scrollbar(self, orient=HORIZONTAL)
        vscrollbar.pack(fill=X, side=BOTTOM, expand=FALSE)
        canvas = Canvas(self, bd=0, highlightthickness=0,
                        xscrollcommand=vscrollbar.set)
        canvas.pack(side=LEFT, fill=BOTH, expand=TRUE)
        vscrollbar.config(command=canvas.xview)

        # reset the view
        canvas.xview_moveto(0)
        canvas.yview_moveto(0)

        # create a frame inside the canvas which will be scrolled with it
        self.interior = interior = Frame(canvas)
        interior_id = canvas.create_window(0, 0, window=interior,
                                           anchor=NW)

        # track changes to the canvas and frame width and sync them,
        # also updating the scrollbar
        def _configure_interior(event):
            # update the scrollbars to match the size of the inner frame
            size = (interior.winfo_reqwidth(), interior.winfo_reqheight())
            canvas.config(scrollregion="0 0 %s %s" % size)
            if interior.winfo_reqwidth() != canvas.winfo_width():
                # update the canvas's width to fit the inner frame
                canvas.config(width=interior.winfo_reqwidth())
        interior.bind('<Configure>', _configure_interior)

        def _configure_canvas(event):
            if interior.winfo_reqwidth() != canvas.winfo_width():
                # update the inner frame's width to fill the canvas
                canvas.itemconfigure(interior_id, width=canvas.winfo_width())
        canvas.bind('<Configure>', _configure_canvas)


class BatchFrame():
    '''
    1. Batch Code 
    2. Batch Start Date 
    3. Batch Time 
    4. Course Code
    5. Faculty
    6. Strength
    7. Status
    8. Progress
    '''
    def __init__(self,master):
        self.master = master
        self.bg='yellow'
        self.faculty='faculty'
        self.batch_code='batch_code'
        self.course_code='course_code'
        self.batch_time='batch_time'
        self.strength='strength'
        self.status='status'
        self.batch_start='batch_start'
        
        self.f1=Frame(self.master,highlightbackground="black",highlightthickness=1)
        self.f1.pack(side=RIGHT,padx=1,pady=1)
        self.lblR5=Label(self.f1,text=self.faculty,bg=self.bg)
        self.lblR5.pack(fill=X)
        self.lblR1=Label(self.f1,text=self.batch_code,width=10,bg=self.bg)
        self.lblR1.pack(fill=X)
        self.lblR2=Label(self.f1,text=self.batch_start,bg=self.bg)
        self.lblR2.pack(fill=X)
        self.lblR3=Label(self.f1,text=self.batch_time,bg=self.bg)
        self.lblR3.pack(fill=X)
        self.lblR4=Label(self.f1,text=self.course_code,width=10,bg=self.bg)
        self.lblR4.pack(fill=X)        
        self.lblR6=Label(self.f1,text=self.strength,bg=self.bg)
        self.lblR6.pack(fill=X)
        self.lblR7=Label(self.f1,text=self.status,bg=self.bg)
        self.lblR7.pack(fill=X)
        self.progress=ttk.Progressbar(self.f1, orient="horizontal", length=100, mode="determinate")
        self.progress.pack()
        self.progress.start()
        self.btnEdit=ttk.Button(self.f1,text='Select',command=self.select_batch).pack(fill=X)
        
    def select_batch(self):
        # messagebox.showinfo('Batch Selected','Thank your for Batch Selection'+self.faculty) 
        rec=[self.faculty,self.batch_code,self.course_code,self.batch_time,self.strength,self.status,self.batch_start]
        app=Batch_Input(rec)
    @classmethod
    def create_new_batch(cls):
        rec=[]
        app=Batch_Input(rec)
        Batch_Input.add_new_batch()
        


    def set_batch(self,rec):
            # print(rec)
            self.bg='yellow'
            
            self.batch_code=rec[0]
            self.course_code=rec[1]
            self.batch_time=rec[3]
            self.faculty=rec[4]
            self.strength=rec[5]
            self.status=rec[6]
            self.batch_start=rec[2]
            
            self.lblR5.configure(text=self.faculty,bg=self.bg)
            self.lblR1.configure(text=self.batch_code,width=10,bg=self.bg)
            self.lblR2.configure(text=self.batch_start,bg=self.bg)
            self.lblR3.configure(text=self.batch_time,bg=self.bg)
            self.lblR4.configure(text=self.course_code,width=10,bg=self.bg)
            
            self.lblR6.configure(text=self.strength,bg=self.bg)
            self.lblR7.configure(text=self.status,bg=self.bg)
            self.progress=ttk.Progressbar(self.f1, orient="horizontal", length=100, mode="determinate")
            

class Batch_Input(Toplevel):
    def __init__(self,rec):
        Toplevel.__init__(self)
        self.resizable(0,0)    
        # StringVar
        self.batchCode=StringVar()        
        self.faculty=StringVar()                
        self.courseCode=StringVar()        
        self.batchTime=StringVar()        
        self.batchDate=StringVar()        
        self.batchStrength=IntVar()
        self.status=StringVar()        
        
        self.lstFaculty=db.get_faculty_info('Python')
        self.lstStatus=['Start','Mid','End']
        self.lstCourse=db.get_course_detail()
        self.lstBatchTime=db.slot_time('Weekday')
        self.f1=Frame(self,bg='green',width=200)
        self.f1.pack(fill=X)
        self.f2=Frame(self)
        self.f2.pack()
        px=5
        py=5
        lblWidth=20
        eWidth=25
        
        self.lblBatchCode = Label(self.f2,text='Batch Code : ',width=lblWidth,anchor=W).grid(row=0,column=0,padx=px,pady=py)
        self.txtBatchCode = ttk.Entry(self.f2,width=eWidth,state=DISABLED,textvariable=self.batchCode).grid(row=0,column=1,padx=px,pady=py)
        
        self.lblCourseName = Label(self.f2,text='Course Name : ',width=lblWidth,anchor=W).grid(row=1,column=0)
        self.txtCourseCode = ttk.Combobox(self.f2,values=self.lstCourse,width=eWidth-3,textvariable=self.courseCode)
        self.txtCourseCode.grid(row=1,column=1,padx=px,pady=py)
        self.txtCourseCode.bind("<<ComboboxSelected>>",self.get_batch_code)

        self.lblStartDate = Label(self.f2,text='Batch Start : ',width=lblWidth,anchor=W).grid(row=2,column=0)
        # self.txtStartDate = ttk.Entry(self.f2,width=eWidth,textvariable=self.batchDate).grid(row=2,column=1,padx=px,pady=py)
        cal = DateEntry(self.f2, width=eWidth-3, background='darkblue',foreground='white', borderwidth=2)
        cal.grid(row=2,column=1,padx=px,pady=py)
        # cal.bind("<<DateEntrySelected>>",printDate)    
    
        self.lblStartTime = Label(self.f2,text='Batch Time : ',width=lblWidth,anchor=W).grid(row=3,column=0)
        self.txtStartTime = ttk.Combobox(self.f2,values=self.lstBatchTime,width=eWidth-3,textvariable=self.batchTime).grid(row=3,column=1,padx=px,pady=py)
        
        self.lblFaculty = Label(self.f2,text='Faculty : ',width=lblWidth,anchor=W).grid(row=4,column=0)
        self.cbFaculty = ttk.Combobox(self.f2,values=self.lstFaculty,width=eWidth-3,textvariable=self.faculty).grid(row=4,column=1,padx=px,pady=py)
        
        self.lblStrength = Label(self.f2,text='Strength : ',width=lblWidth,anchor=W).grid(row=5,column=0)
        self.txtStregth = ttk.Entry(self.f2,width=eWidth,textvariable=self.batchStrength).grid(row=5,column=1,padx=px,pady=py)
        
        self.lblStatus = Label(self.f2,text='Status : ',width=lblWidth,anchor=W).grid(row=6,column=0)
        self.txtStatus = ttk.Combobox(self.f2,values=self.lstStatus,width=eWidth-3,textvariable=self.status).grid(row=6,column=1,padx=px,pady=py)
        
        self.btnClear = ttk.Button(self.f2,text='Clear').grid(row=7,column=1,padx=px,pady=py)
        if len(rec)>0:
            Label(self.f1,text='Update Batch Details',bg='green',fg='white',font=[20]).pack(padx=10,pady=10)
            self.btnUpdate = ttk.Button(self.f2,text='Update',command=self.update_batch_detail).grid(row=7,column=0,padx=px,pady=py)
            self.batchCode.set(rec[1])
            self.faculty.set(rec[0])              
            self.courseCode.set(rec[2])
            self.batchTime.set(rec[3])       
            self.batchDate.set(rec[6])        
            self.batchStrength.set(rec[4])
            self.status.set(rec[5])
        else :
            Label(self.f1,text='Add New Batch Details',bg='green',fg='white',font=[20]).pack(padx=10,pady=10)
            self.btnAdd_Batch = ttk.Button(self.f2,text='Add Batch',command=self.update_batch_detail).grid(row=7,column=0,padx=px,pady=py)
            
    def get_batch_code(self,event):
        db.generate_batch_code(self.courseCode.get())


    def get_data(self):
        args=[]
        args.append(self.batchCode.get())
        args.append(self.courseCode.get())
        args.append(self.batchDate.get())
        args.append(self.batchTime.get())
        args.append(self.faculty.get())
        args.append(self.batchStrength.get())
        args.append(self.status.get())
        return args

    def update_batch_detail(self):
        print('Update Batch Code : ',self.batchCode.get())
        db.update_batch(self.get_data())
        fetch_batch_details()    
    def clear_batch_detail(self):
        pass
    @classmethod
    def add_new_batch(cls):

        fetch_batch_details()    
    




def fetch_batch_details():
    
    for widgets in root.winfo_children():
        # print(widgets.winfo_class())
        if isinstance(widgets, Frame):                        
            widgets.pack_forget()

    batch=[]  # Total No. of Batches :- 11 * 7 + 4 * 7 :- Total : 77 + 28 => 105 
    data = db.get_batch_details()
    i=0    
    for rec in data:        
        batch.append(BatchFrame(root))
        batch[i].set_batch(rec)    
        i=i+1

class NavigationPane():
    def __init__(self):
        pass

root = Tk()
root.geometry("500x300")
leftPanel = ttk.Panedwindow(root,width=100)
leftPanel.pack(side=LEFT,fill=Y)
btnNewBatch=ttk.Button(leftPanel,text="Create New Batch",command=BatchFrame.create_new_batch).pack(side=LEFT)
fetch_batch_details()

root.mainloop()