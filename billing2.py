from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import mysql.connector
from connect2_1 import get_sql_connection
import time
import os
import tempfile

# unified file path
import os
script_dir = os.path.dirname("C:/Git/python_prj/")

# connect with sql server
# connection = mysql.connector.connect(
#             # enter mysql server username
#             user='root', 
#             # enter mysql server password
#             password='root', 
#             host='127.0.0.1', 
#             database='prj_ver2')
sql_user = 'root'
sql_pass = 'root'
        
class BillClass:
    def __init__(self,root):
        self.root=root
        ws = self.root.winfo_screenwidth()
        hs = self.root.winfo_screenheight()
        self.root.geometry("%sx%s+%s+%s" % (ws - 10,hs - 35,0,0))
        self.root.title("Food Market Information Management System")
        self.root.config(bg="white")
        self.cart_list = []
        self.chk_print = 0
        #===TITLE===
        title = Label(self.root, text="Food Market Information Management System", font=("elaris", 40, "bold"), bg="#188576", fg="white").place(x=0, y=0, relwidth=1, height=70)        
        #===BTN_LOGOUT===
       # btn_logout=Button(self.root,text="Logout",font=("time new roman",15,"bold"),bg="yellow",cursor="hand2").place(x=1150,y=10,height=50,width=150)

        #===PRODUCT_FRAME===
        self.var_search = StringVar()

        ProductFrame1=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        ProductFrame1.place(x=6,y=222,width=490,height=562)
        
        pTitle=Label(ProductFrame1,text="Choose Your Products",font=("elaris",20,"bold"),bg="#ed711f",fg="white").pack(side=TOP,fill=X)
        
        ProductFrame2=Frame(ProductFrame1,bd=2,relief=RIDGE,bg="lightgrey")
        ProductFrame2.place(x=2,y=42,width=478,height=90)
               
        lbl_search=Label(ProductFrame2,text="Product Name",font=("elaris",15,"bold"),bg="lightgrey").place(x=25,y=25)
        txt_search=Entry(ProductFrame2,textvariable=self.var_search,font=("elaris",15),bg="white").place(x=168,y=27,width=150,height=22)
        btn_search=Button(ProductFrame2,text="Search", command= self.search,font=("elaris",15),bg="#4f87b3",fg="white",cursor="hand2").place(x=340,y=10,width=100,height=25)
        btn_show_all=Button(ProductFrame2,text="Show All", command=self.show, font=("elaris",15),bg="#c44999",fg="white",cursor="hand2").place(x=340,y=45,width=100,height=25)
        
# create table to show product
        ProductFrame3=Frame(ProductFrame1,bd=3,relief=RIDGE)
        ProductFrame3.place(x=2,y=132,width=478,height=419)
        
        scrolly=Scrollbar(ProductFrame3,orient=VERTICAL)
        scrollx=Scrollbar(ProductFrame3,orient=HORIZONTAL)
        
        self.product_Table=ttk.Treeview(ProductFrame3,columns=("product_id","product_name","product_type","pro_manu","pro_exp","product_unit","product_price","product_quantity","product_description","seller"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set) 
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.product_Table.xview)
        scrolly.config(command=self.product_Table.yview)
        
        self.product_Table.heading("product_id",text="ID")
        self.product_Table.heading("product_name",text="Name")
        self.product_Table.heading("product_type",text="Type")
        self.product_Table.heading("pro_manu",text="Date of manu")
        self.product_Table.heading("pro_exp",text="Date of exp")
        self.product_Table.heading("product_unit",text="Unit")
        self.product_Table.heading("product_price",text="Price per unit")
        self.product_Table.heading("product_quantity",text="Quantity")
        self.product_Table.heading("product_description",text="Description")
        self.product_Table.heading("seller",text="Seller")
        self.product_Table["show"]="headings"
        self.product_Table.column("product_id",width=40)
        self.product_Table.column("product_name",width=100)
        self.product_Table.column("product_type",width=100)
        self.product_Table.column("pro_manu",width=100)
        self.product_Table.column("pro_exp",width=100)
        self.product_Table.column("product_unit",width=100)
        self.product_Table.column("product_price",width=100)
        self.product_Table.column("product_quantity",width=100)
        self.product_Table.column("product_description",width=100)
        self.product_Table.column("seller",width=100)
        self.product_Table.pack(fill=BOTH,expand=1)
        self.product_Table.bind("<ButtonRelease-1>",self.get_data)
        
        #lbl_note=Label(ProductFrame1,text="Note: 'Enter 0 Quantity to remove product from the Cart'",font=("elaris",12),anchor='w',bg="white",fg="red").pack(side=BOTTOM,fill=X)
       
       #===CUSTOMERFRAME===
        self.var_cname=StringVar()
        self.var_contact=StringVar()
        CustomerFrame=Frame(self.root,bd=4,relief=RIDGE,bg="lightgrey")
        CustomerFrame.place(x=497,y=222,width=610,height=70)
        
        cTitle=Label(CustomerFrame,text="Your Information",font=("elaris",15,"bold"),bg="#ed711f", fg="white").pack(side=TOP,fill=X)
        lbl_name=Label(CustomerFrame,text="Name",font=("elaris",15),bg="lightgrey").place(x=10,y=35)
        txt_name=Entry(CustomerFrame,textvariable=self.var_cname,font=("elaris",13),bg="white").place(x=80,y=35,width=180)
        
        lbl_contact=Label(CustomerFrame,text="Contact No.",font=("elaris",15),bg="lightgrey").place(x=310,y=35)
        txt_contact=Entry(CustomerFrame,textvariable=self.var_contact,font=("elaris",13),bg="white").place(x=430,y=35,width=140)
       
        #===CART FRAME===
        Cal_Cart_Frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        Cal_Cart_Frame.place(x=497,y=292,width=610,height=360)
        
        cart_Frame=Frame(Cal_Cart_Frame,bd=3,relief=RIDGE)
        cart_Frame.place(x=1,y=2,width=605,height=355)
        self.cartTitle=Label(cart_Frame,text="Your Cart \t\t\t Total Product: [0]",font=("elaris",15, "bold"),bg="#ed711f", fg="white")
        self.cartTitle.pack(side=TOP,fill=X)

# create table to show products in cart
        scrolly=Scrollbar(cart_Frame,orient=VERTICAL)
        scrollx=Scrollbar(cart_Frame,orient=HORIZONTAL)
        
        self.CartTable=ttk.Treeview(cart_Frame,columns=("product_id","product_name","product_type","product_unit","product_price","product_quantity","seller"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set) 
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.CartTable.xview)
        scrolly.config(command=self.CartTable.yview)
        
        self.CartTable.heading("product_id",text="ID")
        self.CartTable.heading("product_name",text="Name")
        self.CartTable.heading("product_type",text="Type")
        self.CartTable.heading("product_unit",text="Unit")
        self.CartTable.heading("product_price",text="Price")
        self.CartTable.heading("product_quantity",text="Quantity")
        self.CartTable.heading("seller",text="Seller")
        self.CartTable["show"]="headings"
        self.CartTable.column("product_id",width=90)
        self.CartTable.column("product_name",width=100)
        self.CartTable.column("product_type",width=100)
        self.CartTable.column("product_unit",width=100)
        self.CartTable.column("product_price",width=100)
        self.CartTable.column("product_quantity",width=100)
        self.CartTable.column("seller",width=100)
        self.CartTable.pack(fill=BOTH,expand=1)
        self.CartTable.bind("<ButtonRelease-1>",self.get_data2)
        
        #===ADD CART WIDGETS FRAME===
        self.var_product_id=StringVar()
        self.var_pname=StringVar()
        self.var_product_type = StringVar()
        self.var_product_unit = StringVar()
        self.var_qty=StringVar()
        self.var_price=StringVar()
        self.var_seller = StringVar()
        self.var_stock=StringVar()
        
        Add_CartWidgetsFrame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        Add_CartWidgetsFrame.place(x=497,y=652,width=610,height=130)
        
        lbl_p_name=Label(Add_CartWidgetsFrame,text="Product Name",font=("elaris",15),bg="white").place(x=5,y=5)
        txt_p_name=Entry(Add_CartWidgetsFrame,textvariable=self.var_pname,font=("elaris",15),bg="lightyellow",state='readonly').place(x=5,y=35,width=190,height=22)
        
        lbl_p_price=Label(Add_CartWidgetsFrame,text="Price",font=("elaris",15),bg="white").place(x=240,y=5)
        txt_p_price=Entry(Add_CartWidgetsFrame,textvariable=self.var_price,font=("elaris",15),bg="lightyellow",state='readonly').place(x=240,y=35,width=150,height=22)

        lbl_p_qty=Label(Add_CartWidgetsFrame,text="Quantity",font=("elaris",15),bg="white").place(x=430,y=5)
        txt_p_qty=Entry(Add_CartWidgetsFrame,textvariable=self.var_qty,font=("elaris",15),bg="lightyellow").place(x=430,y=35,width=120,height=22)
        
        self.lbl_inStock=Label(Add_CartWidgetsFrame,text="In Stock",font=("elaris",15),bg="white")
        self.lbl_inStock.place(x=5,y=80)
        
        btn_clear_cart=Button(Add_CartWidgetsFrame,text="Clear", command=self.clear, font=("elaris",15,"bold"),bg="#c44999", fg="white",cursor="hand2").place(x=320,y=80,width=120,height=30)
        btn_add_cart=Button(Add_CartWidgetsFrame,text="Add", command=self.add_to_cart,font=("elaris",15,"bold"),bg="#4f87b3", fg="white",cursor="hand2").place(x=460,y=80,width=120,height=30)
        btn_delete_cart=Button(Add_CartWidgetsFrame,text="Delete", command=self.delete_cart, font=("elaris",15,"bold"),bg="#d13715", fg="white",cursor="hand2").place(x=180,y=80,width=120,height=30)

        #========billing area=============================

        bill_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        bill_frame.place(x=1110, y=222, width=410, height=495)

        BTitle=Label(bill_frame,text="Your Bill",font=("elaris",20,"bold"),bg="#ed711f",fg="white").pack(side=TOP,fill=X)
        scrolly = Scrollbar(bill_frame, orient=VERTICAL)
        scrolly.pack(side=RIGHT, fill=Y)

        self.txt_bill_area = Text(bill_frame, yscrollcommand=scrolly.set)
        self.txt_bill_area.pack(fill=BOTH, expand=1)
        scrolly.config(command=self.txt_bill_area.yview)

        #============Billing button========================
        bill_button_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        bill_button_frame.place(x=1110, y=717, width=410, height=65)

        btn_print = Button(bill_button_frame, text="Print", command=self.print_bill, cursor="hand2", font=("elaris", 15, "bold"), bg="#c44999", fg="white")
        btn_print.place(x=1,y=5,width=120,height=50)

        btn_clear = Button(bill_button_frame, text="Clear", command=self.clear_bill, cursor="hand2", font=("elaris", 15, "bold"), bg="#d13715", fg="white")
        btn_clear.place(x=124,y=5,width=120,height=50)

        btn_generate = Button(bill_button_frame, text="Save bill", command=self.generate_bill, cursor="hand2", font=("elaris", 15, "bold"), bg="#4f87b3", fg="white")
        btn_generate.place(x=246,y=5,width=160,height=50)

        #picture
        self.pic_1=Image.open(os.path.join(script_dir,"project_ver2_1/picture/pic_2_2.jpg"))
        self.pic_1=ImageTk.PhotoImage(self.pic_1)        
        lbl_image=Label(self.root,image=self.pic_1,bd=0)
        lbl_image.place(x=600, y=73)

        self.pic_2=Image.open(os.path.join(script_dir,"project_ver2_1/picture/pic3_2.png"))        
        self.pic_2=ImageTk.PhotoImage(self.pic_2)        
        lbl_image2=Label(self.root,image=self.pic_2,bd=0, bg="white")
        lbl_image2.place(x=40, y=73)

        self.pic_3=Image.open(os.path.join(script_dir,"project_ver2_1/picture/pic4_1.png"))        
        self.pic_3=ImageTk.PhotoImage(self.pic_3)        
        lbl_image3=Label(self.root,image=self.pic_3,bd=0, bg="white")
        lbl_image3.place(x=400, y=73)

        self.pic_4=Image.open(os.path.join(script_dir,"project_ver2_1/picture/pic7_1.png"))        
        self.pic_4=ImageTk.PhotoImage(self.pic_4)        
        lbl_image4=Label(self.root,image=self.pic_4,bd=0, bg="white")
        lbl_image4.place(x=200, y=73)

        self.pic_5=Image.open(os.path.join(script_dir,"project_ver2_1/picture/pic5_1.png"))        
        self.pic_5=ImageTk.PhotoImage(self.pic_5)        
        lbl_image5=Label(self.root,image=self.pic_5,bd=0, bg="white")
        lbl_image5.place(x=1070, y=73)

        self.pic_6=Image.open(os.path.join(script_dir,"project_ver2_1/picture/pic6_1.png"))        
        self.pic_6=ImageTk.PhotoImage(self.pic_6)        
        lbl_image6=Label(self.root,image=self.pic_6,bd=0, bg="white")
        lbl_image6.place(x=1300, y=73)

        #=================footer==================================
        label_footer = Label(self.root, text = "Food Market Information Management System | Developed by Group 31\nFor any technical issue please contact: 098xxxxxx36 ", font = ("elaris", 15), bg = "#188576", fg="white").pack(side=BOTTOM, fill = X)

        self.show()
        #self.bill_top()

#==============functions===================================

# function to show product detail
    def show(self):
        connection = mysql.connector.connect(user= sql_user, password=sql_pass, host='127.0.0.1', database='prj_ver2')
        cursor = connection.cursor()
        try:            
            cursor.execute("SELECT * FROM product")
            rows = cursor.fetchall()
            self.product_Table.delete(*self.product_Table.get_children())
            for row in rows:
                self.product_Table.insert('', END, values=row)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent = self.root)

# function to search product by name
    def search(self):
        connection = mysql.connector.connect(user=sql_user, password=sql_user, host='127.0.0.1', database='prj_ver2')
        cursor = connection.cursor()        
        try:
            if self.var_search.get()=="":
                messagebox.showerror("Error", "Input required", parent = self.root)
            else:            
                #cursor.execute("select * from product where %s = %s;",(str(self.var_searchby.get().strip()),self.var_searchtxt.get().strip()))
                cursor.execute("SELECT * FROM product WHERE product_name = %s;",(self.var_search.get(),))
                rows = cursor.fetchall()
                if len(rows)!=0:
                    self.product_Table.delete(*self.product_Table.get_children())
                    for row in rows:
                        self.product_Table.insert('', END, values=row)
                else:
                    messagebox.showerror("Error", "No record found", parent = self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent = self.root)

# functions to display product that being clicked
    def get_data(self, ev):
        f=self.product_Table.focus()
        content = (self.product_Table.item(f))
        row = content['values']

        self.var_product_id.set(row[0])
        self.var_pname.set(row[1])
        self.var_product_type.set(row[2])
        self.var_product_unit.set(row[5])
        self.var_price.set(row[6])
        self.lbl_inStock.config(text=f"In Stock [{str(row[7])}]")
        self.var_stock.set(row[7])    
        self.var_seller.set(row[9])

    def get_data2(self, ev):
        f=self.CartTable.focus()
        content = (self.CartTable.item(f))
        row = content['values']

        self.var_product_id.set(row[0])
        self.var_pname.set(row[1])
        self.var_product_type.set(row[2])
        self.var_price.set(row[4])

# function to add products into cart
    def add_to_cart(self):
        if self.var_product_id.get()=="":
            messagebox.showerror("Error", "Please choose the product you want to buy")
        elif self.var_qty.get()=="":
            messagebox.showerror("Error", "Please enter quantity of the product you want to buy")
        elif int(self.var_qty.get())>int(self.var_stock.get()):
            messagebox.showerror("Error", f"The product has only {str(self.var_stock.get())} stocks left")
        else:
            price_cal = float(int(self.var_qty.get()) * float(self.var_price.get()))
            cart_data = [self.var_product_id.get(), self.var_pname.get(), self.var_product_type.get(), self.var_product_unit.get(), price_cal, self.var_qty.get(), self.var_seller.get()]
            
            #update cart
            option = "no"
            index_ = 0
            for row in self.cart_list:
                if self.var_product_id.get() == row[0]:
                    option = "yes"
                    break
                index_+=1
            if option == "yes":
                op = messagebox.askyesno("Confirm", "Product already in the cart\nDo you want to update the quantity?", parent =self.root)
                if op == True:
                    if self.var_qty.get()=="0":
                        self.cart_list.pop(index_)
                    else:
                        self.cart_list[index_][4] = price_cal
                        self.cart_list[index_][5] = self.var_qty.get()
            else:
                self.cart_list.append(cart_data)
            self.show_cart()
            self.cartTitle.config(text=f"Your Cart \t\t\t Total Product: [{str(len(self.cart_list))}]")
            self.clear()
    
# function to delete product in cart
    def delete_cart(self):
        option = "no"
        index_ = 0
        for row in self.cart_list:
            if self.var_product_id.get() == row[0]:
                option = "yes"
                break
            index_ +=1
        if option == "yes":
            op = messagebox.askyesno("Confirm", "Do you really want to delete this product?", parent =self.root)
            if op == True:
                self.cart_list.pop(index_)
        self.show_cart()
        self.cartTitle.config(text=f"Your Cart \t\t\t Total Product: [{str(len(self.cart_list))}]")
        self.clear()

# function to display product in cart
    def show_cart(self):
        try:            
            self.CartTable.delete(*self.CartTable.get_children())
            for row in self.cart_list:
                self.CartTable.insert('', END, values=row)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent = self.root)

# function to clear all information in input fields
    def clear(self):
        self.var_product_id.set('')
        self.var_pname.set('')
        self.var_product_type.set('')
        self.var_product_unit.set('')
        self.var_price.set('')
        self.lbl_inStock.config(text=f"In Stock [{str(0)}]")
        self.var_qty.set('')    
        self.var_seller.set('')

        self.show()

    def clear_bill(self):
        del self.cart_list[:]
        self.var_cname.set("")
        self.var_contact.set("")
        self.var_search.set("")
        self.txt_bill_area.delete("1.0",END)
        self.cartTitle.config(text="Your Cart \t\t\t Total Product: [0]")
        self.clear()
        self.show()
        self.show_cart()
        self.chk_print = 0

# function to display customer bill
    def generate_bill(self):
        if self.var_cname.get()=="" or self.var_contact.get()=="":
            messagebox.showerror("Error", "Make sure to enter your name and your contact number", parent = self.root)
        elif len(self.cart_list)<=0:
            messagebox.showerror("Error", "Your cart are empty", parent = self.root)
        else:
            #Bill top
            self.bill_top()
            #Bill middle
            self.bill_middle()
            #Bill bottom
            self.bill_bottom()
            
            fp = open(os.path.join(script_dir, r'project_ver2_1/bill', f'{str(self.invoice)}.txt'), 'w')
            fp.write(self.txt_bill_area.get('1.0',END))
            fp.close()
            messagebox.showinfo("Saved", "Bill has been generated", parent = self.root)
            self.chk_print = 1

# functions to create bill's contents
    def bill_top(self):
        self.invoice = int(time.strftime("%d%m%y")) + int(time.strftime("%H%M%S"))
        bill_top_temp = f'''
\t      Group 31 - Food Market
  18 Hoang Quoc Viet str, Cau Giay dist, Hanoi
{str("."*48)}
    \t\t       BILL

Customer Name: {self.var_cname.get()}
Contact Number: {self.var_contact.get()}
Date: {str(time.strftime("%d,%m,%Y"))}  {str(time.strftime("%H%M%S"))} 
Bill No. {str(self.invoice)}
        
Product\t\tPrice/unit\t\tQty\t Total
        
        '''
        self.txt_bill_area.delete("1.0", END)
        self.txt_bill_area.insert("1.0", bill_top_temp)


    def bill_bottom(self):
        self.invoice = int(time.strftime("%d%m%y")) + int(time.strftime("%H%M%S"))
        bill_bottom_temp = f'''

\t   (Price already include tax)

{str("."*48)}
Reference Number                {str(self.invoice)}
{str("."*48)}
   Tax Invoice will be issued within same day
{str("."*48)}
\t  THANK YOU AND SEE YOU AGAIN
        
        '''
        self.txt_bill_area.insert(END, bill_bottom_temp)


    def bill_middle(self):
        connection = mysql.connector.connect(user=sql_user, password=sql_pass, host='127.0.0.1', database='prj_ver2')
        cursor = connection.cursor()        
        try:
            for row in self.cart_list:
                product_id = row[0]
                name = row[1]
                qty = row[5]
                
                price = row[4]
                price_per_unit = str(float(row[4])/int(row[5]))
                self.txt_bill_area.insert(END,"\n "+name+"\t\t "+price_per_unit+"\t\t "+qty+"\t "+str(price))
                quantity = int(self.var_stock.get()) - int(qty)
                cursor.execute("UPDATE product SET product_quantity = %s WHERE product_id = %s;",(quantity, product_id))
                connection.commit()
            connection.close()
            self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent = self.root)

# function to save bill into device
    def print_bill(self):
        if self.chk_print == 1:
            messagebox.showinfo("Print","Printing, please wait", parent = self.root)
            new_file = tempfile.mktemp('.txt')
            open(new_file,'w').write(self.txt_bill_area.get('1.0',END))
            os.startfile(new_file,'print')
        else:
            messagebox.showerror("Error", "Bill was not saved", parent = self.root)

if __name__=="__main__":
    root=Tk()
    obj=BillClass(root)
    connection = get_sql_connection()
    root.mainloop()

        
        
        