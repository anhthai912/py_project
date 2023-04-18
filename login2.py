import tkinter as tk 
from tkinter import *
from tkinter import ttk 
from tkinter.ttk import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image,ImageTk
import mysql.connector
from connect2_1 import get_sql_connection
from dashboard2 import IMS
from billing2 import BillClass

# unified file path
import os
script_dir = os.path.dirname("C://Git/python_prj/")

connection = mysql.connector.connect(
            # enter mysql server username
            user='self.root', 
            # enter mysql server password
            password='self.root', 
            host='127.0.0.1', 
            database='prj_ver2')

class login1_class:
    def __init__(self, root):
        self.root = root
        # width and height
        w = 450
        h = 600
        # background color
        bgcolor = "white"

        # CENTER FORM
        self.root.overrideredirect(1) # remove border
        ws = self.root.winfo_screenwidth()
        hs = self.root.winfo_screenheight()
        x = (ws-w)/2
        y = (hs-h)/2
        self.root.geometry("%dx%d+%d+%d" % (w, h, x, y))

# HEADER
        self.headerframe = tk.Frame(self.root, highlightbackgroun='white', highlightcolor='white', 
                            highlightthickness=2, bg='white', width=w, height=70)
        self.titleframe = tk.Frame(self.headerframe, bg='white', padx=1, pady=1)
        self.title_label = tk.Label(self.titleframe, text='Sign In', padx=20, pady=5, bg='white', 
                            fg='#188576', font=('Tahoma',24), width=15)
        self.close_label = tk.Label(self.headerframe, text='x', bg="white", fg="#eb1d0e", cursor="hand2",
                                font=('elaris',15))
        self.close_label.bind("<ButtonRelease-1>", self.close_win)

        self.headerframe.pack()
        self.titleframe.pack()
        self.title_label.pack()
        self.close_label.pack()

        self.titleframe.place(y=26, relx=0.5, anchor=CENTER)
        self.close_label.place(x=410, y=5)

        self.mainframe = tk.Frame(self.root, width=w, height=h)

# Login Page
        self.loginframe = tk.Frame(self.mainframe, width=w, height=h)
        self.login_contentframe = tk.Frame(self.loginframe, padx=30, pady=100, 
                            highlightbackgroun='white', highlightcolor='white', 
                            highlightthickness=2, bg=bgcolor)


        self.user_type_label_rg = tk.Label(self.login_contentframe, text='Login as:', 
                                font=('elaris',14), bg=bgcolor, fg="black")

        self.username_entry = tk.Entry(self.login_contentframe, font=('elaris',16), width=28, bg=bgcolor, fg="black", border=0)
        self.username_entry.insert(0,"Username")
        self.frame1 = tk.Frame(self.login_contentframe, height=2, width=370, bg="black")

        self.username_entry.bind("<FocusIn>", self.on_enter)
        self.username_entry.bind("<FocusOut>", self.on_leave)

        self.password_entry = tk.Entry(self.login_contentframe, font=('elaris',16), width=28, bg=bgcolor, fg="black", border=0)
        self.password_entry.insert(0,"Password")
        self.frame2 = tk.Frame(self.login_contentframe, height=2, width=370, bg="black")

        self.password_entry.bind("<FocusIn>", self.on_enter2)
        self.password_entry.bind("<FocusOut>", self.on_leave2)

        # universal image path for self.open_eye 1,2,3
        image_path_open_eye = os.path.join(script_dir, "project_ver2_1/picture/show1.png")


        self.open_eye = tk.PhotoImage(file = image_path_open_eye)

        self.eye_button = tk.Button(self.login_contentframe, image=self.open_eye, bd=0, bg=bgcolor, activebackground=bgcolor, cursor="hand2", command=self.hide)
        self.eye_button.place(x=345, y=69)

        self.radiosframe3 = tk.Frame(self.login_contentframe)
        self.user_type = StringVar()
        self.user_type.set('Customer')
        self.customer_radiobutton = tk.Radiobutton(self.radiosframe3, text='Customer', font=('elaris',14), 
                                        bg=bgcolor,fg="black", variable=self.user_type, value='Customer')
        self.seller_radiobutton = tk.Radiobutton(self.radiosframe3, text='Seller', font=('elaris',14), 
                                            bg=bgcolor,fg="black", variable=self.user_type, value='Seller')

        self.login_button = tk.Button(self.login_contentframe,text="Login", font=('elaris',16), 
                                bg='#188576',fg='white', padx=25, pady=10, width=25)

        self.go_register_label = tk.Label(self.login_contentframe, 
                            text=">> Don't have an account? Create one" , cursor="hand2",
                            font=('elaris',10), bg=bgcolor, fg='#de4747')

        self.mainframe.pack(fill='both', expand=1)
        self.loginframe.pack(fill='both', expand=1)
        self.login_contentframe.pack(fill='both', expand=1)

        self.username_entry.grid(row=0, column=0, columnspan=3, pady=10)
        self.frame1.grid(row=1, column=0, columnspan=3)

        self.password_entry.grid(row=2, column=0, columnspan=3, pady=10)
        self.frame2.grid(row=3, column=0, columnspan=3)
        self.user_type_label_rg.grid(row=4, column=0, pady=10)
        self.radiosframe3.grid(row=4,column=1)
        self.customer_radiobutton.grid(row=0, column=0)
        self.seller_radiobutton.grid(row=0, column=1)

        self.login_button.grid(row=5, column=0, columnspan=2, pady=40)

        self.go_register_label.grid(row=6, column=0, columnspan=2, pady=20)

        self.go_register_label.bind("<Button-1>", lambda page: self.go_to_register())

        self.login_button['command'] = self.login

# register page
        self.registerframe = tk.Frame(self.mainframe, width=w, height=h)
        self.register_contentframe = tk.Frame(self.registerframe, padx=30, pady=15, 
                                highlightbackgroun='white', highlightcolor='white', 
                                highlightthickness=2, bg=bgcolor)

        self.fullname_label_rg = tk.Label(self.register_contentframe, text='Fullname:', 
                                    font=('elaris',14),fg="black", bg=bgcolor)
        self.username_label_rg = tk.Label(self.register_contentframe, text='Username:', 
                                    font=('elaris',14), fg="black",bg=bgcolor)
        self.password_label_rg = tk.Label(self.register_contentframe, text='Password:', 
                                    font=('elaris',14), fg="black",bg=bgcolor)
        self.confirmpass_label_rg = tk.Label(self.register_contentframe, text='Retype Password:', 
                                        font=('elaris',14),fg="black", bg=bgcolor)
        self.phone_label_rg = tk.Label(self.register_contentframe, text='Phone:', 
                                font=('elaris',14), fg="black",bg=bgcolor)
        self.gender_label_rg = tk.Label(self.register_contentframe, text='Gender:', 
                                font=('elaris',14), fg="black",bg=bgcolor)
        self.address_label_rg = tk.Label(self.register_contentframe, text='Address:', 
                                font=('elaris',14), fg="black",bg=bgcolor)
        self.type_person_label_rg = tk.Label(self.register_contentframe, text='Type:', 
                                font=('elaris',14), fg="black",bg=bgcolor)

        self.fullname_entry_rg = tk.Entry(self.register_contentframe, font=('elaris',16), width=28, bg=bgcolor, fg="black", border=0)
        self.fullname_entry_rg.insert(0,"Fullname")
        self.frame3 = tk.Frame(self.register_contentframe, height=2, width=370, bg="black")

        self.fullname_entry_rg.bind("<FocusIn>", self.on_enter3)
        self.fullname_entry_rg.bind("<FocusOut>", self.on_leave3)

        self.username_entry_rg = tk.Entry(self.register_contentframe, font=('elaris',16), width=28, bg=bgcolor, fg="black", border=0)
        self.username_entry_rg.insert(0,"Username")
        self.frame4 = tk.Frame(self.register_contentframe, height=2, width=370, bg="black")

        self.username_entry_rg.bind("<FocusIn>", self.on_enter4)
        self.username_entry_rg.bind("<FocusOut>", self.on_leave4)


        self.password_entry_rg = tk.Entry(self.register_contentframe, font=('elaris',16), width=28, bg=bgcolor, fg="black", border=0)
        self.password_entry_rg.insert(0,"Password")
        self.frame5 = tk.Frame(self.register_contentframe, height=2, width=370, bg="black")

        self.password_entry_rg.bind("<FocusIn>", self.on_enter5)
        self.password_entry_rg.bind("<FocusOut>", self.on_leave5)

        self.open_eye2 = tk.PhotoImage(file = image_path_open_eye)

        self.eye_button2 = tk.Button(self.register_contentframe, image=self.open_eye2, bd=0, bg=bgcolor, activebackground=bgcolor, cursor="hand2", command=self.hide2)
        self.eye_button2.place(x=345, y=120)


        self.confirmpass_entry_rg = tk.Entry(self.register_contentframe, font=('elaris',16), width=28, bg=bgcolor, fg="black", border=0)
        self.confirmpass_entry_rg.insert(0,"Retype password")
        self.frame6 = tk.Frame(self.register_contentframe, height=2, width=370, bg="black")

        self.confirmpass_entry_rg.bind("<FocusIn>", self.on_enter6)
        self.confirmpass_entry_rg.bind("<FocusOut>", self.on_leave6)

        self.open_eye3 = tk.PhotoImage(file = image_path_open_eye)

        self.eye_button3 = tk.Button(self.register_contentframe, image=self.open_eye3, bd=0, bg=bgcolor, activebackground=bgcolor, cursor="hand2", command=self.hide3)
        self.eye_button3.place(x=345, y=165)


        self.phone_entry_rg = tk.Entry(self.register_contentframe, font=('elaris',16), width=28, bg=bgcolor, fg="black", border=0)
        self.phone_entry_rg.insert(0,"Phone")
        self.frame7 = tk.Frame(self.register_contentframe, height=2, width=370, bg="black")

        self.phone_entry_rg.bind("<FocusIn>", self.on_enter7)
        self.phone_entry_rg.bind("<FocusOut>", self.on_leave7)


        self.address_entry_rg = tk.Entry(self.register_contentframe, font=('elaris',16), width=28, bg=bgcolor, fg="black", border=0)
        self.address_entry_rg.insert(0,"Address")
        self.frame8 = tk.Frame(self.register_contentframe, height=2, width=370, bg="black")

        self.address_entry_rg.bind("<FocusIn>", self.on_enter8)
        self.address_entry_rg.bind("<FocusOut>", self.on_leave8)

        self.radiosframe1 = tk.Frame(self.register_contentframe)
        self.gender = StringVar()
        self.gender.set('Male')
        self.male_radiobutton = tk.Radiobutton(self.radiosframe1, text='Male', font=('elaris',14), 
                                        bg=bgcolor,fg="black", variable=self.gender, value='Male')
        self.female_radiobutton = tk.Radiobutton(self.radiosframe1, text='Female', font=('elaris',14), 
                                            bg=bgcolor,fg="black", variable=self.gender, value='Female')

        self.radiosframe2 = tk.Frame(self.register_contentframe)
        self.person = StringVar()
        self.person.set('Customer')
        self.customer_radiobutton = tk.Radiobutton(self.radiosframe2, text='Customer', font=('elaris',14), 
                                        bg=bgcolor,fg="black", variable=self.person, value='Customer')
        self.seller_radiobutton = tk.Radiobutton(self.radiosframe2, text='Seller', font=('elaris',14), 
                                            bg=bgcolor,fg="black", variable=self.person, value='Seller')

        self.register_button = tk.Button(self.register_contentframe,text="Register", font=('elaris',16)
                                    , bg='#188576',fg='white', padx=25, pady=10, width=25)

        self.go_login_label = tk.Label(self.register_contentframe, 
                                text=">> Already have an account? Sign in" , cursor="hand2", 
                                font=('elaris',10), bg=bgcolor, fg='#de4747')


        self.register_contentframe.pack(fill='both', expand=1)

        self.fullname_entry_rg.grid(row=0, column=0, columnspan=3, pady=10)
        self.frame3.grid(row=1, column=0, columnspan=3)
        self.username_entry_rg.grid(row=2,column=0,columnspan=3,pady=10)
        self.frame4.grid(row=3, column=0, columnspan=3)
        self.password_entry_rg.grid(row=4, column=0, columnspan=3, pady=10)
        self.frame5.grid(row=5, column=0, columnspan=3)
        self.confirmpass_entry_rg.grid(row=6, column=0,columnspan=3, pady=10)
        self.frame6.grid(row=7, column=0, columnspan=3)
        self.phone_entry_rg.grid(row=8,column=0,columnspan=3,pady=10)
        self.frame7.grid(row=9, column=0, columnspan=3)
        self.address_entry_rg.grid(row=10,column=0,columnspan=3,pady=10)
        self.frame8.grid(row=11, column=0, columnspan=3)

        self.gender_label_rg.grid(row=12, column=0, pady=5, sticky='e')
        self.radiosframe1.grid(row=12, column=1)
        self.male_radiobutton.grid(row=0, column=0)
        self.female_radiobutton.grid(row=0, column=1)

        self.type_person_label_rg.grid(row=13, column=0, pady=5, sticky='e')
        self.radiosframe2.grid(row=13, column=1)
        self.customer_radiobutton.grid(row=0, column=0)
        self.seller_radiobutton.grid(row=0, column=1)


        self.register_button.grid(row=14, column=0, columnspan=2, pady=10)

        self.go_login_label.grid(row=15, column=0, columnspan=2, pady=10)

        self.go_login_label.bind("<Button-1>", lambda page: self.go_to_login())

        self.register_button['command'] = self.register

# function to close window
    def close_win(self):
        root.destroy()

# functions to make word disappear when being clicked
    def on_enter(self, sth):
        self.username_entry.delete(0, "end")

    def on_leave(self, sth):
        name = self.username_entry.get()
        if name =="":
            self.username_entry.insert(0,"Username")

    def on_enter2(self, sth):
        self.password_entry.delete(0, "end")

    def on_leave2(self, sth):
        password_ = self.password_entry.get()
        if password_ =="":
            self.password_entry.insert(0,"Password")

    def on_enter3(self, sth):
        self.fullname_entry_rg.delete(0, "end")

    def on_leave3(self, sth):
        fullname = self.fullname_entry_rg.get()
        if fullname =="":
            self.fullname_entry_rg.insert(0,"Fullname")

    def on_enter4(self, sth):
        self.username_entry_rg.delete(0, "end")

    def on_leave4(self, sth):
        username = self.username_entry_rg.get()
        if username =="":
            self.username_entry_rg.insert(0,"Username")

    def on_enter5(self, sth):
        self.password_entry_rg.delete(0, "end")

    def on_leave5(self, sth):
        password_2 = self.password_entry_rg.get()
        if password_2 =="":
            self.password_entry_rg.insert(0,"Password")

    def on_enter6(self, sth):
        self.confirmpass_entry_rg.delete(0, "end")

    def on_leave6(self, sth):
        password_3 = self.confirmpass_entry_rg.get()
        if password_3 =="":
            self.confirmpass_entry_rg.insert(0,"Retype password")

    def on_enter7(self, sth):
        self.phone_entry_rg.delete(0, "end")

    def on_leave7(self, sth):
        phone= self.phone_entry_rg.get()
        if phone =="":
            self.phone_entry_rg.insert(0,"Phone")

    def on_enter8(self, sth):
        self.address_entry_rg.delete(0, "end")

    def on_leave8(self, sth):
        address = self.address_entry_rg.get()
        if address =="":
            self.address_entry_rg.insert(0,"Address")

# create eye icons to show and hide password
    def hide(self):
        # specify the file path relative to the script directory
        image_path = os.path.join(script_dir, "project_ver2_1/picture/hide1.png")
        self.open_eye.config(file=image_path)

        self.password_entry.config(show="*")
        self.eye_button.config(command=self.show)

    def show(self):
        # specify the file path relative to the script directory
        image_path = os.path.join(script_dir, "project_ver2_1/picture/show1.png")
        self.open_eye.config(file=image_path)

        self.password_entry.config(show="")
        self.eye_button.config(command=self.hide)

    def hide2(self):
        # specify the file path relative to the script directory
        image_path = os.path.join(script_dir, "project_ver2_1/picture/hide1.png")
        self.open_eye2.config(file=image_path)

        self.password_entry_rg.config(show="*")
        self.eye_button2.config(command=self.show2)

    def show2(self):
        # specify the file path relative to the script directory
        image_path = os.path.join(script_dir, "project_ver2_1/picture/show1.png")
        self.open_eye2.config(file=image_path)

        self.password_entry_rg.config(show="")
        self.eye_button2.config(command=self.hide2)

    def hide3(self):
        # specify the file path relative to the script directory
        image_path = os.path.join(script_dir, "project_ver2_1/picture/hide1.png")
        self.open_eye3.config(file=image_path)

        self.confirmpass_entry_rg.config(show="*")
        self.eye_button3.config(command=self.show3)

    def show3(self):
        # specify the file path relative to the script directory
        image_path = os.path.join(script_dir, "project_ver2_1/picture/show1.png")
        self.open_eye3.config(file=image_path)
        self.confirmpass_entry_rg.config(show="")
        self.eye_button3.config(command=self.hide3)

# function to display the register frame
    def go_to_register(self):
        self.loginframe.forget()
        self.registerframe.pack(fill="both", expand=1)
        self.title_label['text'] = 'Create Account'
        self.title_label['bg'] = 'white'

# function to make the user login
    def login(self):
        cursor = connection.cursor()
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()
        self.user_type_value = self.user_type.get()
        vals = (username, password, self.user_type_value)
        select_query = "SELECT * FROM `users` WHERE `user_name` = %s and `password` = %s and `type` = %s"
        cursor.execute(select_query, vals)
        user = cursor.fetchone()
        if user is not None:
            if self.user_type_value == "Seller":
                #messagebox.showinfo('Test','Test')
                self.mainformwindow = tk.Toplevel()
                app = IMS(self.mainformwindow)
                self.root.withdraw() # hide the self.root
                self.mainformwindow.protocol("WM_DELETE_WINDOW", self.close_win) # close the app
            else:
                self.mainformwindow = tk.Toplevel()
                app = BillClass(self.mainformwindow)
                self.root.withdraw() # hide the self.root
                self.mainformwindow.protocol("WM_DELETE_WINDOW", self.close_win)
        else:
            messagebox.showwarning('Error','wrong username, password or login perspective')

# function to display the login frame
    def go_to_login(self):
        self.registerframe.forget()
        self.loginframe.pack(fill="both", expand=1)
        self.title_label['text'] = 'Sign In'
        self.title_label['bg'] = 'white'


# function to check if the username already exists
    def check_username(self, username, sth):
        cursor = connection.cursor()
        username = self.username_entry_rg.get().strip()
        vals = (username,)
        select_query = "SELECT * FROM `users` WHERE `user_name` = %s"
        cursor.execute(select_query, vals)
        user = cursor.fetchone()
        if user is not None:
            return True
        else:
            return False

# function to register a new user
    def register(self):
        cursor = connection.cursor()
        full_name = self.fullname_entry_rg.get().strip() # remove white space
        user_name = self.username_entry_rg.get().strip()
        password = self.password_entry_rg.get().strip()
        confirm_password = self.confirmpass_entry_rg.get().strip()
        phone_number = self.phone_entry_rg.get().strip()
        address = self.address_entry_rg.get().strip()
        gdr = self.gender.get()
        type_person = self.person.get()

        if len(full_name) > 0 and  len(user_name) > 0 and len(password) > 0 and len(phone_number) > 0 and len(address)> 0:
            if self.check_username(self,user_name) == False: 
                if password == confirm_password:
                    vals = (full_name, user_name, password, phone_number, gdr, address, type_person)
                    insert_query = "INSERT INTO `users`(`full_name`, `user_name`, `password`, `phone_number`, `gender`, `address`, `type`) VALUES (%s,%s,%s,%s,%s,%s,%s)"
                    cursor.execute(insert_query, vals)
                    connection.commit()
                    messagebox.showinfo('Register','your account has been created successfully')
                    self.go_to_login()
                    
                else:
                    messagebox.showwarning('Password','incorrect password confirmation')
            else:
                messagebox.showwarning('Duplicate Username','This Username Already Exists, try another one')
        else:
            messagebox.showwarning('Empty Fields','make sure to enter all the information')

# main 
if __name__ == "__main__":
    root = Tk()
    obj = login1_class(root)
    connection = get_sql_connection()
    root.mainloop() 