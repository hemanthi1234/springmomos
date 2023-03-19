# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 22:14:36 2023

@author: anura
"""
import pymysql as pm 
def show_records():
   conn = pm.connect(host="localhost", user="root", password="1234",database="db")
   curr = conn.cursor()
   curr.execute("use db")
   curr.execute("select * from vendors")
   for i in curr:
       for j in i:
           print(j,end=" ")
       print()    
           
        
   conn.commit()
   conn.close()


def add_records():
    a=input("Enter the vendor ID : ")
    b=input("Enter vendor name : ")
    c=input("Enter shop address : ")
    d=input("Enter contact number: ")
    if a == "" or b == "" or c == "":
      print("Error!", "All fields are required!")
    else:
        conn = pm.connect(host= "localhost", user="root", password="1234", database= "db")
        curr = conn.cursor()
        values=(a,b,c,d)
        qry="INSERT INTO vendors values(%s,%s,%s,%s)"
        curr.execute(qry,values)
        print("A new vendor has been added!")
        conn.commit()
        conn.close()
        show_records()
        


def find_data():
   x=input("Enter the vendor ID : ")
   conn = pm.connect(host="localhost", user="root", password="1234",database="db")
   curr = conn.cursor()
   qry="select * from vendors where vendorID like %s"
   curr.execute(qry,x)
   for i in curr:
       print(i)
   conn.commit()
   conn.close() 
   

def update_record(): #to update information 
    x=input("Enter the ID of vendor whose details have to be updated: ")
    b=input("Enter vendor name : ")
    c=input("Enter new shop address : ")
    d=input("Enter new contact number: ")
    conn = pm.connect(host="localhost", user="root", password="1234", database="db")
    curr = conn.cursor()
    qry="update vendors set Vendorname=%s, Shopaddress=%s, ContactNo=%s where vendorID=%s"
    val=(b,c,d,x)
    curr.execute(qry,val)
    conn.commit()
    print("Vendor details have been updated! ")
    show_records()
    conn.close()
   


def delete_record():
    x=input("Enter the ID of vendor whose details have to be deleted: ")
    conn = pm.connect (host="localhost", user="root", password="1234", database="db")
    curr = conn.cursor() 
    qry="delete from vendors where VendorID=%s"
    curr.execute(qry,x) 
    conn.commit()
    print("The vendor has been removed")
    show_records()
    conn.close()   



print("Welcome to vendor management! ")
print('''Select the option:
         1. Add a new vendor
         2. Search for a vendor
         3. Modify vendor details
         4. Remove a vendor
         5. See all vendors''')
  
       
       
       
       
       
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from turtle import width
import pymysql

win = tk.Tk()
win.geometry("1350x700+0+0")
win.title("Canteen")

title_label = tk.Label(win,text="Uncle Tiwari ki canteen", font=("Stencil", 30,"bold"),border=12,relief=tk.GROOVE,bg="green", foreground="white")
title_label.pack(side=tk.TOP,fill=tk.X)

detail_frame = tk.LabelFrame(win,text="Information",font=("Arial", 25,), bg="light green", border=12,relief=tk.GROOVE)
detail_frame.place(x=20, y=100, width=420,height=530)

data_frame = tk.Frame(win, bd=12, bg="light green",relief=tk.GROOVE)
data_frame.place(x=460, y=100, width=800, height=530)      


x=int(input("Enter the operation you want: "))
         
if x==1:
       add_records()
elif x==2:
       find_data()
elif x==3:
       update_record()  
elif x==4:
       delete_record()
elif x==5:
       show_records()       
else:
       print("Please enter a valid option")  


vid = tk.StringVar()
vendorname = tk.StringVar()
shopad = tk.StringVar()
num = tk.StringVar()
dob = tk.StringVar()

search_by = tk.StringVar()
searchtext = tk.StringVar()

vid = tk.Label(detail_frame, text=" Vendor ID.", font=("Fixedsys", 15), bg="light grey")
vid.grid(row=0, column=0,padx=2,pady=2)

vide = tk.Entry(detail_frame,bd=7,font=("Arial",15),textvariable=vid)
vide.grid(row=0,column=1,padx=2,pady=2)

vendorname = tk.Label(detail_frame, text=" Vendor Name", font=("Fixedsys", 15), bg="light grey")
vendorname.grid(row=1, column=0,padx=2,pady=2)

vendornamee = tk.Entry(detail_frame,bd=7,font=("Arial",15), textvariable=vendorname)
vendornamee.grid(row=1,column=1,padx=2,pady=2)

shopadd = tk.Label(detail_frame, text="Shop address", font=("Fixedsys", 15), bg="light grey")
shopadd.grid(row=2, column=0,padx=2,pady=2)

shopadde= tk.Entry(detail_frame,bd=7,font=("Arial",15),textvariable=shopad)
shopadde.grid(row=2,column=1,padx=2,pady=2)

connum = tk.Label(detail_frame, text="Contact number", font=("Fixedsys", 15), bg="light grey")
connum.grid(row=3, column=0,padx=2,pady=2)

connum= tk.Entry(detail_frame,bd=7,font=("Arial",15),textvariable=num)
connum.grid(row=3,column=1,padx=2,pady=2)



btn_frame = tk.Frame(detail_frame,bg="light grey", bd=10, relief=tk.GROOVE)
btn_frame.place(x=20, y=320, width=360, height=110)

add_btn = tk.Button(btn_frame,text="Add",bd=5,bg="light grey",width=15,font=("arial",13,"bold"), command=add_records)
add_btn.grid(row=0, column=0,padx=2,pady=2)

update_btn = tk.Button(btn_frame,text="Update",bd=5,bg="light grey",width=15, font=("arial",13,"bold"), command=update_record)
update_btn.grid(row=0, column=1,padx=2,pady=2)

update_btn = tk.Button(btn_frame,text="Clear",bd=5,bg="light grey",width=15, font=("arial",13,"bold"), command=update_record)
update_btn.grid(row=1, column=0,padx=2,pady=2)

delete_btn = tk.Button(btn_frame,text="Delete",bd=5,bg="light grey",width=15, font=("arial",13,"bold"), command=delete_record)
delete_btn.grid(row=1, column=1,padx=2,pady=2) 


#searching
search_frame = tk.Frame(data_frame,bg="light grey", bd=10, relief=tk.GROOVE)
search_frame.pack(side=tk.TOP,fill=tk.X)

search_lbl = tk.Label(search_frame,text="Field", bg="light grey", font=("arial", 15))
search_lbl.grid(row=0,column=0,padx=2,pady=2)

search_in = ttk.Combobox(search_frame,font=("arial", 13), state="readonly",textvariable=search_by)
search_in["values"]=("Vendor ID","Vendor name","Shop address","Contact Num")
search_in.grid(row=0, column=1,padx=12,pady=2)

txt_search= tk.Entry(search_frame, width=20, font=("arial",13), bd=5,relief=tk.GROOVE, textvariable=searchtext)
txt_search.grid(row= 0, column= 2, padx=12, pady=2)

search_btn = tk.Button(search_frame, text= "Search", font=("arial",13), bd=9, width=10,bg="light grey", command= find_data)
search_btn.grid(row=0, column=3, padx=12, pady=2)

showall_btn = tk.Button(search_frame, text= "Show All", font=("arial",13), bd=9, width=10,bg="light grey", command=show_records)
showall_btn.grid(row=0, column=4, padx=12, pady=2)
win.mainloop()










