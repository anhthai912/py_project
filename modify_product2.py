from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
from connect2_1 import get_sql_connection

# unified file path
import os
script_dir = os.path.dirname("C://Git/python_prj/")

# connect with sql server
connection = mysql.connector.connect(
            # enter mysql server username
            user='root', 
            # enter mysql server password
            password='root', 
            host='127.0.0.1', 
            database='prj_ver2')
        

class modify_product_class:
    def __init__(self, root):
        self.root = root
        #self.root.overrideredirect(1) #remove top border
        ws = self.root.winfo_screenwidth()
        hs = self.root.winfo_screenheight()
        self.root.geometry("%sx%s+%s+%s" % (ws,hs - 185,0,100))
        self.root.title("Food Market Information Management System")
        self.root.config(bg="lightgrey")
        self.root.focus_force()
        
        #self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()
        self.var_product_id = StringVar()
        self.var_product_name = StringVar()
        self.var_product_type = StringVar()
        self.var_product_price = StringVar()
        self.var_product_unit = StringVar()
        self.var_product_quantity = StringVar()
        self.var_pro_manu = StringVar()
        self.var_pro_exp = StringVar()
        self.var_product_description = StringVar()
        self.var_seller = StringVar()

#=======Search Frame
        search_frame = LabelFrame(self.root, text = "Search Product", font=("elaris", 15,"bold"), bg = "lightgrey", bd = 2, relief = RIDGE)
        search_frame.place(x=470,y=20,width=600,height=70)

#=======option
        csearch = Label(search_frame,text="Product name: ", font=("elaris", 15), bg="lightgrey")
        csearch.place(x=20,y=8,width=170)
        """csearch.current(0)"""

        txt_search = Entry(search_frame, textvariable=self.var_searchtxt, font=("elaris", 15), bg = "white").place(x=190,y=10,width=230,height=25)
        btn_search = Button(search_frame, text = "Search", command=self.search, font=("elaris", 15), bg = "#ed711f", fg = "white", bd =2,cursor = "hand2").place(x=450,y=10,width=100,height=25)

#=======title
        title = Label(self.root, text = "Product Detail", font=("elaris", 20,"bold"), bg = "#188576", fg = "white" )
        title.place(x=0,y=100,relwidth=1, height = 30)

#=======content
        #product id
        lbl_product_id = Label(self.root, text = "Product ID", font=("elaris", 15,"bold"), bg = "lightgrey").place(x=100,y=150)
        txt_product_id = Entry(self.root, textvariable = self.var_product_id, font=("elaris", 15), bg = "lightyellow").place(x=250,y=150,width=200,height=25)
        #MFG
        lbl_pro_manu = Label(self.root, text = "MFG", font=("elaris", 15,"bold"), bg = "lightgrey").place(x=550,y=150)
        txt_pro_manu = Entry(self.root, textvariable = self.var_pro_manu, font=("elaris", 15), bg = "lightyellow").place(x=620,y=150,width=280,height=25)
        #unit id
        lbl_product_unit = Label(self.root, text = "Unit", font=("elaris", 15,"bold"), bg = "lightgrey").place(x=1000,y=150)
        cbb_product_unit = ttk.Combobox(self.root, textvariable=self.var_product_unit, font=("elaris", 13),values=("choose","each","gram","kilogram"), state = "readonly", justify = CENTER)
        cbb_product_unit.place(x=1060,y=150,width=120,height=25)
        cbb_product_unit.current(0)
        #name
        lbl_product_name = Label(self.root, text = "Product name", font=("elaris", 15,"bold"), bg = "lightgrey").place(x=100,y=200)
        txt_product_name = Entry(self.root, textvariable = self.var_product_name, font=("elaris", 15), bg = "lightyellow").place(x=250,y=200,width=200,height=25)
        #EXP
        lbl_pro_exp = Label(self.root, text = "EXP", font=("elaris", 15,"bold"), bg = "lightgrey").place(x=550,y=200)
        txt_pro_exp = Entry(self.root, textvariable = self.var_pro_exp, font=("elaris", 15), bg = "lightyellow").place(x=620,y=200,width=280,height=25)
        #type id
        lbl_product_type = Label(self.root, text = "Type", font=("elaris", 15,"bold"), bg = "lightgrey").place(x=995,y=200)
        cbb_product_type = ttk.Combobox(self.root, textvariable=self.var_product_type, font=("elaris", 13),values=("choose","meat","seafood","dry food","spices","snacks","drinks","fruit","vegetable"), state = "readonly", justify = CENTER)
        cbb_product_type.place(x=1060,y=200,width=120,height=25)
        cbb_product_type.current(0)
        #seller name
        lbl_seller = Label(self.root, text = "Seller username", font=("elaris", 15,"bold"), bg = "lightgrey").place(x=550,y=250)
        txt_seller = Entry(self.root, textvariable = self.var_seller, font=("elaris", 15), bg = "lightyellow").place(x=720,y=250,width=180,height=25)
        #price per unit
        lbl_product_price = Label(self.root, text = "Price per Unit", font=("elaris", 15,"bold"), bg = "lightgrey").place(x=100,y=250)
        txt_product_price = Entry(self.root, textvariable = self.var_product_price, font=("elaris", 15), bg = "lightyellow").place(x=250,y=250,width=200,height=25)
        #quantity
        lbl_product_quantity = Label(self.root, text = "Quantity", font=("elaris", 15,"bold"), bg = "lightgrey").place(x=965,y=250)
        txt_product_quantity = Entry(self.root, textvariable = self.var_product_quantity, font=("elaris", 15), bg = "lightyellow").place(x=1060,y=250,width=120,height=25)
        #description
        lbl_product_description = Label(self.root, text = "Description", font=("elaris", 15,"bold"), bg = "lightgrey").place(x=100,y=320)
        txt_product_description = Entry(self.root, textvariable = self.var_product_description, font=("elaris", 15), bg = "lightyellow").place(x=250,y=300,width=350,height=80)
       
#=======button
        btn_add = Button(self.root, text = "Save", command=self.add, font=("elaris", 15), bg = "blue", fg = "white", bd =2,cursor = "hand2").place(x=650,y=340,width=90,height=25)
        btn_update = Button(self.root, text = "Update", command=self.update, font=("elaris", 15), bg = "green", fg = "white", bd =2,cursor = "hand2").place(x=760,y=340,width=90,height=25)
        btn_delete = Button(self.root, text = "Delete", command=self.delete, font=("elaris", 15), bg = "red", fg = "white", bd =2,cursor = "hand2").place(x=870,y=340,width=90,height=25)
        btn_clear = Button(self.root, text = "Clear", command=self.clear, font=("elaris", 15), bg = "gray", fg = "white", bd =2,cursor = "hand2").place(x=980,y=340,width=90,height=25)

#=======picture
        """self.product_photo1=Image.open(os.path.join(script_dir,"project_ver2_1/picture/seafood2.png"))
        self.product_photo1=ImageTk.PhotoImage(self.product_photo1)
        
        lbl_image1=Label(self.root,image=self.product_photo1,bd=0, bg="lightgrey")
        lbl_image1.place(x=220,y=0)"""

        self.product_photo2=Image.open(os.path.join(script_dir,"project_ver2_1/picture/food1.png"))
        self.product_photo2=ImageTk.PhotoImage(self.product_photo2)
        
        lbl_image2=Label(self.root,image=self.product_photo2,bd=0, bg="lightgrey")
        lbl_image2.place(x=140,y=0)

        """self.product_photo3=Image.open(os.path.join(script_dir,"project_ver2_1/picture/meat1.png"))
        self.product_photo3=ImageTk.PhotoImage(self.product_photo3)
        
        lbl_image3=Label(self.root,image=self.product_photo3,bd=0, bg="lightgrey")
        lbl_image3.place(x=1050,y=3)"""

        self.product_photo4=Image.open(os.path.join(script_dir,"project_ver2_1/picture/diet3.png"))
        self.product_photo4=ImageTk.PhotoImage(self.product_photo4)
        
        lbl_image4=Label(self.root,image=self.product_photo4,bd=0, bg="lightgrey")
        lbl_image4.place(x=1240,y=200)

        self.product_photo5=Image.open(os.path.join(script_dir,"project_ver2_1/picture/octopus5.png"))
        self.product_photo5=ImageTk.PhotoImage(self.product_photo5)
        
        lbl_image5=Label(self.root,image=self.product_photo5,bd=0, bg="lightgrey")
        lbl_image5.place(x=1200,y=3)

#=======table
        pro_frame = Frame(self.root, bd = 3, relief = RIDGE, bg = "white")
        pro_frame.place(x=0,y=420,relwidth=1,height=260)
        
        scrollx = Scrollbar(pro_frame, orient = HORIZONTAL)
        scrolly = Scrollbar(pro_frame, orient = VERTICAL)

        self.product_table = ttk.Treeview(pro_frame, columns=("product_id","product_name","product_type","pro_manu","pro_exp","product_unit","product_price","product_quantity","product_description", "seller"),xscrollcommand = scrollx.set, yscrollcommand = scrolly.set)
        scrollx.pack(side = BOTTOM, fill = X)
        scrolly.pack(side = RIGHT, fill = Y)
        scrollx.config(command = self.product_table.xview)
        scrolly.config(command = self.product_table.yview)
        self.product_table.heading("product_id", text = "ID")
        self.product_table.heading("product_name", text = "Name")
        self.product_table.heading("product_type", text = "Type")
        self.product_table.heading("pro_manu", text = "Manufacturer")
        self.product_table.heading("pro_exp", text = "EXP")
        self.product_table.heading("product_unit", text = "Unit")
        self.product_table.heading("product_price", text = "Price per Unit")
        self.product_table.heading("product_quantity", text = "Quantity")
        self.product_table.heading("product_description", text = "Description")
        self.product_table.heading("seller", text = "Seller")

        self.product_table["show"] = "headings"

        self.product_table.pack(fill = BOTH, expand = 1)
        
        self.product_table.column("product_id", width = 40)
        self.product_table.column("product_name", width = 90)
        self.product_table.column("product_type", width = 90)
        self.product_table.column("pro_manu", width = 90)
        self.product_table.column("pro_exp", width = 90)
        self.product_table.column("product_unit", width = 50)
        self.product_table.column("product_price", width = 50)
        self.product_table.column("product_quantity", width = 50)
        self.product_table.column("product_description", width = 90)
        self.product_table.column("seller", width = 90)

        self.show()
        self.product_table.bind("<ButtonRelease-1>", self.get_data)

# function to add product into the database
    def add(self):
        cursor = connection.cursor()
        try:
            if self.var_product_name.get()=="":
                messagebox.showerror("Error", "Product name must be required", parent = self.root)
            else:
                cursor.execute("SELECT * FROM product WHERE product_name=%s;", (self.var_product_name.get(),))
                row = cursor.fetchone()
                if row != None:
                    messagebox.showerror("Error", "This product name already assigned", parent = self.root)
                else:
                    cursor.execute("INSERT INTO product (product_id,product_name,product_type,pro_manu,pro_exp,product_unit,product_price,product_quantity,product_description,seller) value (%s,%s, %s, %s, %s, %s, %s, %s, %s, %s);", (
                                            self.var_product_id.get(),
                                            self.var_product_name.get(),
                                            self.var_product_type.get(),
                                            self.var_pro_manu.get(),
                                            self.var_pro_exp.get(),
                                            self.var_product_unit.get(),
                                            self.var_product_price.get(),
                                            self.var_product_quantity.get(),                                            
                                            self.var_product_description.get(),
                                            self.var_seller.get()
                    ))
                    connection.commit()
                    messagebox.showinfo("Success", "Product added successfully", parent = self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent = self.root)

# function to display product in the database
    def show(self):
        cursor = connection.cursor()
        try:            
            cursor.execute("SELECT * FROM product")
            rows = cursor.fetchall()
            self.product_table.delete(*self.product_table.get_children())
            for row in rows:
                self.product_table.insert('', END, values=row)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent = self.root)

# function to receive data from product that being clicked
    def get_data(self, ev):
        f=self.product_table.focus()
        content = (self.product_table.item(f))
        row = content['values']
        
        self.var_product_id.set(row[0]),
        self.var_product_name.set(row[1]),
        self.var_product_type.set(row[2]),
        self.var_pro_manu.set(row[3]),
        self.var_pro_exp.set(row[4]),
        self.var_product_unit.set(row[5]),
        self.var_product_price.set(row[6]),
        self.var_product_quantity.set(row[7]),                                            
        self.var_product_description.set(row[8]),
        self.var_seller.set(row[9])

# function to update product info after being changed
    def update(self):
        cursor = connection.cursor()
        try:
            if self.var_product_id.get()=="":
                messagebox.showerror("Error", "Product id must be required", parent = self.root)
            else:
                cursor.execute("SELECT * FROM product WHERE product_id=%s;", (self.var_product_id.get(),))
                row = cursor.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid product id", parent = self.root)
                else:
                    cursor.execute("UPDATE product SET product_name = %s,product_type = %s,pro_manu = %s,pro_exp = %s,product_unit = %s,product_price = %s,product_quantity = %s,product_description = %s,seller = %s where product_id = %s;", (
                                            
                                            self.var_product_name.get(),
                                            self.var_product_type.get(),
                                            self.var_pro_manu.get(),
                                            self.var_pro_exp.get(),
                                            self.var_product_unit.get(),
                                            self.var_product_price.get(),
                                            self.var_product_quantity.get(),                                            
                                            self.var_product_description.get(),
                                            self.var_seller.get(),
                                            self.var_product_id.get()
                    ))
                    connection.commit()
                    messagebox.showinfo("Success", "Product updated successfully", parent = self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent = self.root)

# function to delete product
    def delete(self):    
        cursor = connection.cursor()
        try:
            if self.var_product_id.get()=="":
                messagebox.showerror("Error", "Product id must be required", parent = self.root)
            else:
                cursor.execute("SELECT * FROM product WHERE product_id=%s;", (self.var_product_id.get(),))
                row = cursor.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid product id", parent = self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Do you really want to delete this product?", parent = self.root)
                    if op == True:
                        cursor.execute("DELETE FROM product WHERE product_id =%s;", (self.var_product_id.get(),))
                        #cursor.execute("select max(product_id) from product;")
                        #cursor.execute("alter table product auto_increment = max(product_id)+1;")
                        connection.commit()
                        messagebox.showinfo("Delete", "Product deleted successfully", parent = self.root)
                        
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent = self.root)
        
# function to clear all info in input fields
    def clear(self):
        self.var_product_id.set("")
        self.var_product_name.set("")
        self.var_product_type.set("choose")
        self.var_pro_manu.set("")
        self.var_pro_exp.set("")
        self.var_product_unit.set("choose")
        self.var_product_price.set("")
        self.var_product_quantity.set("")                                           
        self.var_product_description.set("")
        self.var_seller.set("")
        self.var_searchtxt.set("")
        #self.var_searchby.set("Search by")
        self.show()

# function to search product by name
    def search(self):
        cursor = connection.cursor()
        
        try:           
            if self.var_searchtxt.get()=="":
                messagebox.showerror("Error", "Input required", parent = self.root)
            else:            
                #cursor.execute("SELECT * FROM product WHERE %s = %s;",(str(self.var_searchby.get().strip()),self.var_searchtxt.get().strip()))
                cursor.execute("SELECT * FROM product WHERE product_name = %s;",(self.var_searchtxt.get(),))
                rows = cursor.fetchall()
                if len(rows)!=0:
                    self.product_table.delete(*self.product_table.get_children())
                    for row in rows:
                        self.product_table.insert('', END, values=row)
                else:
                    messagebox.showerror("Error", "No record found", parent = self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent = self.root)


if __name__ == "__main__":
    root = Tk()
    obj = modify_product_class(root)
    connection = get_sql_connection()
    root.mainloop()