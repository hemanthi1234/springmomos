import mysql.connector as c

con=c.connect(host="localhost",user="hemanthi",passwd="1.hemanthi.2",database="world")
cursor=con.cursor()
foodcode=int(input("Enter Code:"))
Name=input("Enter Name:")
Description=input("Enter type:")
Price=int(input("Enter the Price"))
Qauntity=int(input("Enter the Qauntity:"))
query="Insert into purchaseorders values({},'{}','{}',{},{})".format(foodcode,Name,Description,Price,Qauntity)
cursor.execute(query)
con.commit()
print("Data Inserted.")


mysql=c.connect(host="localhost",user="hemanthi",passwd="1.hemanthi.2",database="world")
cursor=mysql.cursor()
foodcode=int(input("enter a number"))
Name=input("Enter Name:")
Description=input("Enter type:")
Price=int(input("Enter the Price"))
Qauntity=int(input("Enter the Qauntity:"))
sql="Update purchaseorders set Name=%s,Description=%s,Price=%s,Qauntity=%s where foodcode=%s"
data=(foodcode,Name,Description,Price,Qauntity)
try:
    cursor.execute(sql,data)
    mysql.commit()
    print("Data uploaded")

except:
    print("error")

mysq=c.connect(host="localhost",user="hemanthi",passwd="1.hemanthi.2",database="world")
cursor=mysq.cursor()
foodcode=int(input("enter a number"))
sql="delete from purchaseorders where foodcode=%s"
try:
    cursor.execute(sql,foodcode)
    mysq.commit()
    print("item deleted")
except:
    print("error")


mys=c.connect(host="localhost",user="hemanthi",passwd="1.hemanthi.2",database="world")
cursor=mys.cursor()
print("{},'{}','{}',{},{}".format(foodcode,Name,Description,Price,Qauntity))

try:
    sql="select*from student"
    cursor.execute(sql)
    sdata=cursor.fetchall()
    for s in sdata:
        print("{},'{}','{}',{},{}".format(s[0],s[1],s[2],s[3],s[4]))
except:
    print("error")

    
