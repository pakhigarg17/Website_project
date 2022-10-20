import os
from tkinter import filedialog
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from PIL import Image ,ImageTk
import db
import Prog_Dashboard

def main():
    root=Tk()
    # root.geometry("500x500")
    app=Login(root)
    root.mainloop()


class Login():
    def __init__(self,master):
        self.master = master
        w, h = self.master.winfo_screenwidth(), self.master.winfo_screenheight()
        self.master.geometry("%dx%d+0+0" % (w, h))
        self.master.resizable(0,0)
        self.master.configure(bg='orange')
        self.lbltitle=Label(self.master,text="Welcome to Balbhawan",bg='orange',fg='white',font=("impact", 30)).pack(pady=20)
        #Login Form
        self.frmLoginFrame=Frame(self.master,relief=RIDGE)
        self.frmLoginFrame.configure(highlightbackground="black",highlightthickness=1)
        self.frmLoginFrame.place(x=500,y=100,width=370,height=200)
        
        #Latest Info Form
        # self.frmSecond=Frame(self.master,relief=RIDGE)
        # self.frmSecond.configure(highlightbackground="black",highlightthickness=1)
        # self.frmSecond.place(x=10,y=350,width=w-30,height=380)
        
        Label(self.frmLoginFrame,text="User Name : ").place(x=20,y=30)
        Label(self.frmLoginFrame,text="Password  : ").place(x=20,y=70)
        ttk.Entry(self.frmLoginFrame).place(x=150,y=30,width=180,height=25)
        ttk.Entry(self.frmLoginFrame,show='*').place(x=150,y=70,width=180,height=25)
        ttk.Button(self.frmLoginFrame,text="Login",command=self.login_check,width=10).place(x=240,y=110,width=90)
        lblForget=Label(self.frmLoginFrame,text='Forgot Password')
        lblForget.place(x=237,y=150)
        lblForget.bind("<Button-1>",lambda e : messagebox.showinfo('Password','Contact Admin to change password'))
        lblForget.bind("<Enter>",lambda e : e.widget.config(fg='blue'))
        lblForget.bind("<Leave>",lambda e : e.widget.config(fg='black'))
        
        # self.list_box=Listbox(self.frmSecond).pack()
    
    def login_check(self):
        # self.master.withdraw()
        # app = Registration()
        self.openFrame()
    #----------------------------------------------------------------------
    def hide(self):
        """"""
        self.master.withdraw()
        
    #----------------------------------------------------------------------
    def openFrame(self):
        """"""
        self.hide()
        # subFrame = OtherFrame()
        # app = Registration()
        app = Prog_Dashboard.Dashboard_Root()
        handler = lambda: self.onCloseOtherFrame(app)
        # btn = Button(app.frameBottom, text="Close", command=handler,width=10)
        # btn.place(x=300)
        # app.protocol("WM_DELETE_WINDOW", self._delete_window)
        app.bind("<Destroy>", self._destroy)
        
    #----------------------------------------------------------------------
    def onCloseOtherFrame(self, regFrame):
        """"""
        regFrame.destroy()
        self.show()

    def _destroy(self,event):
        # print(event)
        # print("Registration window destroy by _destroy method")
        self.show()    

    # def _delete_window(self,*args):
    #     print("Registration window destroy by _destroy_window method")
    #     self.show()    
        
    #----------------------------------------------------------------------
    def show(self):
        """"""
        self.master.update()
        self.master.deiconify()

if __name__ == "__main__":
    main()    
