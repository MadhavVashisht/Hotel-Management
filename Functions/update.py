import mysql.connector
import Room_Info as info

conn = mysql.connector.connect(host='localhost', user='root', password='',  database='hotel')
cursor=conn.cursor(buffered=True)

def update():
    rn=int(input("Enter your room number: "))
    info.Main()
    nrn=int(input("Enter which type of room do you want: "))
    query=''