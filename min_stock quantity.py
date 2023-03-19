# Define a function to check stock levels and send alerts if necessary
import mysql.connector as c

con=c.connect(host="localhost",user="hemanthi",passwd="1.hemanthi.2",database="world")
cur=con.cursor()
def stocklevel():
    cur.execute("foodcode,Name,Quantity,min_stock From stocktb")
    for row in cur.fetchall():
        foodcode,Name,Qauntity,min_stock=row
        if Qauntity<min_stock:
            print("ALERT:Name has fallen below the minimum stock level" ,'min_stock')

stocklevel()
            
