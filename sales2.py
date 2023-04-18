from tkinter import *
from PIL import Image,ImageTk #pip install pillow
from tkinter import ttk, messagebox
from connect2_1 import get_sql_connection
import os

# unified file pathS
import os
script_dir = os.path.dirname("C://Git/python_prj/")

class sale_class:
    def __init__(self, root):
        self.root = root
        #self.root.overrideredirect(1) #remove top border
        ws = self.root.winfo_screenwidth()
        hs = self.root.winfo_screenheight()
        self.root.geometry("%sx%s+%s+%s" % (ws,hs - 185,0,100))
        self.root.title("Food Market Information Management System")
        self.root.config(bg="lightgrey")
        self.root.focus_force()
        
        self.bill_list=[]
        self.var_invoice=StringVar()
        #title==
        lbl_title=Label(self.root,text="View Customer Bills ",font=("elaris",30),bg="#188576",fg="white",bd=3,relief=RIDGE).pack(side=TOP,fill=X)
      
        lbl_invoice=Label(self.root,text="Invoice No.",font=("elaris",15),bg="lightgrey").place(x=50,y=100)
        txt_invoice=Entry(self.root,textvariable=self.var_invoice,font=("elaris",15),bg="lightyellow").place(x=160,y=100,width=180,height=28)
        btn_search=Button(self.root,text="Search",command=self.search,font=("elaris",15,"bold"),bg="#2196f3",fg="white",cursor="hand2").place(x=360,y=100,width=120,height=28)                                                                                           
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("elaris",15,"bold"),bg="red",fg="white",cursor="hand2").place(x=490,y=100,width=120,height=28)
        
        #===Bill List===
        sales_Frame=Frame(self.root,bd=3,relief=RIDGE)
        sales_Frame.place(x=50,y=140,width=300,height=530)
        
        scrolly=Scrollbar(sales_Frame,orient=VERTICAL)
        self.Sales_List=Listbox(sales_Frame,font=("elaris",15),bg="white",yscrollcommand=scrolly.set)
        scrolly.pack(side=RIGHT,fill=Y)
        scrolly.config(command=self.Sales_List.yview)
        self.Sales_List.pack(fill=BOTH,expand=1)
        self.Sales_List.bind("<ButtonRelease-1>",self.get_data)
        
        #===Bill Area===
        bill_Frame=Frame(self.root,bd=3,relief=RIDGE)
        bill_Frame.place(x=380,y=140,width=450,height=530)
        
        lbl_title2=Label(bill_Frame,text="Customer Bills Area",font=("elaris",20),bg="orange").pack(side=TOP,fill=X)
        
        scrolly2=Scrollbar(bill_Frame,orient=VERTICAL)
        self.bill_area=Text(bill_Frame,bg="lightyellow",yscrollcommand=scrolly2.set)
        scrolly2.pack(side=RIGHT,fill=Y)
        scrolly2.config(command=self.bill_area.yview)
        self.bill_area.pack(fill=BOTH,expand=1)
        
        #==Image==
        self.bill_photo=Image.open(os.path.join(script_dir,"project_ver2_1/picture/cashier2.png"))
        self.bill_photo=ImageTk.PhotoImage(self.bill_photo)
        
        lbl_image=Label(self.root,image=self.bill_photo,bd=0, bg="lightgrey")
        lbl_image.place(x=935,y=130)
        
        self.bill_photo2=Image.open(os.path.join(script_dir,"project_ver2_1/picture/bill1.png"))
        self.bill_photo2=ImageTk.PhotoImage(self.bill_photo2)
        
        lbl_image2=Label(self.root,image=self.bill_photo2,bd=0, bg="lightgrey")
        lbl_image2.place(x=1290,y=90)

        self.show()
        
# function to display bills name
    def show(self):
        del self.bill_list[:]
        self.Sales_List.delete(0,END)
        #print(os.listdir('../IMS')) bill1.txt, category.py
        for i in os.listdir(os.path.join(script_dir,'project_ver2_1/bill')):
            #print(i.split('.'),i.split('.')[-1])
            if i.split('.')[-1]=='txt':
                self.Sales_List.insert(END,i)
                self.bill_list.append(i.split('.')[0])
                
# function to open and display bill
    def get_data(self,ev):
        index_=self.Sales_List.curselection()
        file_name=self.Sales_List.get(index_)
        # print(file_name)
        self.bill_area.delete('1.0',END)
        #fp=open(os.path.join(script_dir,f'project_ver2_1/bill/{file_name}','r'))
        fp = open(os.path.join(script_dir, r'project_ver2_1/bill', f'{file_name}'), 'r')
        for i in fp:
            self.bill_area.insert(END,i)
        fp.close()

# function to search bill by name
    def search(self):
        if self.var_invoice.get()=="":
            messagebox.showerror("Error","Invoice no. should be required",parent=self.root)
        else:
            if self.var_invoice.get() in self.bill_list:
                #fp=open(os.path.join(script_dir,f'project_ver2_1/bill/{self.var_invoice.get()}.txt','r'))
                fp = open(os.path.join(script_dir, r'project_ver2_1/bill', f'{self.var_invoice.get()}'), 'r')
                self.bill_area.delete('1.0',END)
                for i in fp:
                   self.bill_area.insert(END,i)
                fp.close()
            else:
                messagebox.showerror("Error","Invalid Invoice No.",parent=self.root)

    def clear(self):
        self.show()
        self.bill_area.delete('1.0',END)
     


if __name__=="__main__":
    root=Tk()
    obj=sale_class(root)
    connection = get_sql_connection()
    root.mainloop()