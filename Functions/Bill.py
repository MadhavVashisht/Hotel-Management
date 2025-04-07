import datetime
import mysql.connector

def Main():
    conn = mysql.connector.connect(host='localhost', user='root', password='12345678',  database='hotel')
    cursor=conn.cursor(buffered=True)

    cursor.execute("create table if not exists Bill( CustomerId varchar(5),RoomNumber varchar(4),Name varchar(50),CheckIn varchar(10),CheckOut varchar(10),Rate varchar(5),Days varchar(3),ResturantBill varchar(5),Bill varchar(10)); ")

    k=input("\t\t\t\tEnter The Customer Id\n\t\t\t\t->")

    Resturant_Bill='0'

    query='Select CustomerId from booking where CustomerId='+k+';'
    q=cursor.execute(query)
    d=cursor.fetchall()
    for row in d:
        Cust_Id=(row[0])


    query='Select RoomNumber from booking where CustomerId='+k+';'
    q=cursor.execute(query)
    d=cursor.fetchall()
    for row in d:
        Room_No=(row[0])

    query='Select Name from booking where CustomerId='+k+';'
    q=cursor.execute(query)
    d=cursor.fetchall()
    for row in d:
        Name=(row[0])

    query='Select CheckIn from booking where CustomerId='+k+';'
    q=cursor.execute(query)
    d=cursor.fetchall()
    for row in d:
        CheckIn=(row[0])

    query='Select CheckOut from booking where CustomerId='+k+';'
    q=cursor.execute(query)
    d=cursor.fetchall()
    for row in d:
        CheckOut=(row[0])

    query='Select Rate from booking where CustomerId='+k+';'
    q=cursor.execute(query)
    d=cursor.fetchall()
    for row in d:
        Price=(row[0])

    query='Select ResturantBill from Resturant where CustomerId='+k+';'
    q=cursor.execute(query)
    d=cursor.fetchall()
    for row in d:
        Resturant_Bill=(row[0])

    checkin=CheckIn
    checkin=checkin.split('/')
    checkin[0]=int(checkin[0])
    checkin[1]=int(checkin[1])
    checkin[2]=int(checkin[2])

    checkout=CheckOut
    checkout=checkout.split('/')
    checkout[0]=int(checkout[0])
    checkout[1]=int(checkout[1])
    checkout[2]=int(checkout[2])

    d1 = datetime.datetime(checkin[2],checkin[1],checkin[0])
    d2 = datetime.datetime(checkout[2],checkout[1],checkout[0])
    d = (d2-d1).days
    Days=str(d)

    k=int(k)
    if Resturant_Bill!=0:
        bill=d*int(Price)+int(Resturant_Bill)
        Bill=str(bill)
    else:
        bill=d*int(Price)
        Bill=str(bill)

    print("\t\t\t\t Payment")
    print("\t\t\t\t --------------------------------")
    print("\t\t\t\t MODE OF PAYMENT")
    print("\t\t\t\t 1- Credit/Debit Card")
    print("\t\t\t\t 2- Paytm/PhonePe")
    print("\t\t\t\t 3- Using UPI")
    print("\t\t\t\t 4- Cash")
    x=int(input("\t\t\t\t-> "))
    print("\n\t\t\t\t Amount: ",Bill)
    print("\n\t\t\t\t Pay For Hotel Paradise")
    print("\t\t\t\t (y/n)")
    ch=str(input("\t\t\t\t->"))

    if ch.lower()=='y':
        print("\t\t\t\t\t\t\t\t	 *** HOTEL Bill ***\n")
        print("\t\t\t-------------------------------------------------------------------------------------------------------------------------")
        print("\t\t\t| CustomerId\t | Name\t\t| Check-In\t| Check-Out\t| Price\t\t| Days\t| Resturant Bill | Total Bill\t|")
        print("\t\t\t-------------------------------------------------------------------------------------------------------------------------")
        print("\t\t\t| ",Cust_Id,"\t\t | ",Name,"\t|",CheckIn,"\t|",CheckOut,"\t|",Price,"\t\t|",Days,"\t|",Resturant_Bill," \t\t |",Bill,"\t|")
        print("\t\t\t-------------------------------------------------------------------------------------------------------------------------")

        query="Insert Into Bill(CustomerID,RoomNumber,Name,CheckIn,CheckOut,Rate,Days,ResturantBill,Bill)\
    Values('"+Cust_Id+"','"+Room_No+"','"+Name+"','"+CheckIn+"','"+CheckOut+"','"+Price+"','"+Days+"','"+Resturant_Bill+"','"+Bill+"');"
        cursor.execute(query)
        conn.commit()

    else:
        print("\t\t\t\t\t\t\t\t!!!Payment Failed!!!")