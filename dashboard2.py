from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk,messagebox
from modify_product2 import modify_product_class
from sales2 import sale_class
#from for_exp import login1_class

# unified file path
import os
script_dir = os.path.dirname("C://Git/python_prj/")

class IMS:
    def __init__(self, root):
        self.root = root
        
        ws = self.root.winfo_screenwidth()
        hs = self.root.winfo_screenheight()
        self.root.geometry("%sx%s+%s+%s" % (ws - 10,hs - 35,0,0))
        self.root.title("Food Market Information Management System")
        self.root.config(bg="white")

#title
        title = Label(self.root, text="Food Market Information Management System", bd=2,font=("elaris", 40, "bold"), bg="#188576", fg="white").place(x=0, y=0, relwidth=1, height=70)

#main
        self.photo_bg=Image.open(os.path.join(script_dir,"project_ver2_1/picture/bg1_2.png"))
        self.photo_bg=ImageTk.PhotoImage(self.photo_bg)
        lbl_image_bg=Label(self.root,image=self.photo_bg,bd=0, bg="white")
        lbl_image_bg.place(x=8, y=70)
        
        main_frame = Frame(self.root, bd=2, bg="white")
        main_frame.place(x=310, y=270, width=900, height=310)

        modify_button = Button(main_frame, text="Modify Products", cursor="hand2",font=('elaris',20), bg="#d13715", fg="white",command= self.modify_product)
        modify_button.place(x=50, y=5)
        
        bill_button = Button(main_frame, text="View Customer Bill", cursor="hand2",font=('elaris',20), bg="#d13715", fg="white",command= self.sale)
        bill_button.place(x= 570, y=5)

        self.photo1=Image.open(os.path.join(script_dir,"project_ver2_1/picture/a2.jpg"))
        self.photo1=ImageTk.PhotoImage(self.photo1)
        lbl_image1=Label(main_frame,image=self.photo1,bd=0, bg="white")
        lbl_image1.place(x=35,y=65)

        self.photo2=Image.open(os.path.join(script_dir,"project_ver2_1/picture/b.png"))
        self.photo2=ImageTk.PhotoImage(self.photo2)      
        lbl_image2=Label(main_frame,image=self.photo2,bd=0, bg="white")
        lbl_image2.place(x=560,y=65)

        """log_out_button = Button(self.root, text="Sign out", cursor="hand2", font=('elaris',20), bg="#d13715", fg="white",command= self.sign_out)
        log_out_button.place(x=1100, y=5)"""
        """button_modify_product = Button(self.root, text = ">> Modify",command=self.modify_product, font = ("elaris", 20, "bold"), bg="#242323", bd=0, cursor="hand2", fg="#de108b").pack(side = TOP, fill = X)
        button_bill = Button(self.root, text = ">> Bill", command=self.sale, font = ("elaris", 20, "bold"), bg="#242323", bd=0, cursor="hand2", fg="#de108b").pack(side = TOP, fill = X)


        self.photo4=Image.open(os.path.join(script_dir,"project_ver2_1/picture/bg_login_image1.jpg"))
        self.photo4=ImageTk.PhotoImage(self.photo4)
        
        lbl_image5=Label(self.root,image=self.photo4,bd=0, bg="#242323")
        lbl_image5.place(x=0,y=70)"""

#footer
        label_footer = Label(self.root, text = "Food Market Information Management System | Developed by Group 31\nFor any technical issue please contact: 098xxxxxx36 ", font = ("elaris", 15), bg="#188576", fg="white").pack(side=BOTTOM, fill = X)

    def sign_out(self):
        op = messagebox.askyesno("Confirm", "Do you want to sign out?", parent = self.root)
        if op == True:
            root.destroy()
            # login1_class.go_to_login()
            # self.new_win = Toplevel(self.root)
            # self.new_obj = login1_class(self.new_win)

# function to pop up modify_product's screen
    def modify_product(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = modify_product_class(self.new_win)

# function to pop up view_bill's screen
    def sale(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = sale_class(self.new_win)

    def exit_(self):
        root.destroy()

if __name__ == "__main__":
    root = Tk()
    obj = IMS(root)
    root.mainloop()