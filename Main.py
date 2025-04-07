import mysql.connector

conn = mysql.connector.connect(host='localhost', user='root', password='12345678')
cursor=conn.cursor(buffered=True)

cursor.execute("create database if not exists hotel")

from Functions import Booking as F1
from Functions import Room_Info as F2
from Functions import Room_Service as F3
from Functions import Bill as F4
from Functions import Records as F5


def Main():
        while True:
                print("\t\t\t\t\t\t\t\tWelcome To Hotel Paradise")
                print("\t\t\t\tEnter 1 For Booking")
                print("\t\t\t\tEnter 2 For Room Info")
                print("\t\t\t\tEnter 3 For Room Service")
                print("\t\t\t\tEnter 4 For Payment")
                print("\t\t\t\tEnter 5 For Record")
                print("\t\t\t\tEnter 0 To Exit")
                ch=int(input("\n\t\t\t\t->"))
                if ch==1:
                        F1.Main()
                elif ch==2:
                        F2.Main()
                elif ch==3:
                        F3.Main()
                elif ch==4:
                        F4.Main()
                elif ch==5:
                        F5.Main()
                elif ch==0:
                        exit()
                else:
                        print("\t\t\t\t\t\t\t\t!!!!!!Wrong Input Try Again!!!!!!")
                        print()
                        print()
                        print()
                        print()

Main()
