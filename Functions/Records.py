import mysql.connector
Name=[]
Phone=[]
Address=[]
CheckIn=[]
CheckOut=[]
Days=[]
Room=[]
Price=[]
Room_No=[]
Cust_Id=[]
conn = mysql.connector.connect(host='localhost', user='root', password='12345678',  database='hotel')
cursor=conn.cursor(buffered=True)

def Main():

    while True:
        print("\t\t\t\t\t\t\t\tWelcome To Records Menu")
        print("\t\t\t\tEnter 1 For Booking Record Of Specific Date")
        print("\t\t\t\tEnter 2 For Record Of Specific Customer")
        print("\t\t\t\tEnter 3 For Bookings Record")
        print("\t\t\t\tEnter 4 For Customer Record")
        print("\t\t\t\tEnter 0 To Go Back")
        ch=int(input("\n\t\t\t\t->"))
        if ch==1:
            query='select CustomerId from booking order by CustomerId desc ;'
            q=cursor.execute(query)
            d=cursor.fetchall()

            if d==[]:
                i=0
            else:
                ele=d[0]
                i=int(ele[0])

            query='Select CustomerId from booking'
            q=cursor.execute(query)
            d=cursor.fetchall()
            for row in d:
                Cust_Id.append(row[0])
            
            query='Select RoomNumber from booking'
            q=cursor.execute(query)
            d=cursor.fetchall()
            for row in d:
                Room_No.append(row[0])

            query='Select Name from booking'
            q=cursor.execute(query)
            d=cursor.fetchall()
            for row in d:
                Name.append(row[0])

            query='Select PhoneNumber from booking'
            q=cursor.execute(query)
            d=cursor.fetchall()
            for row in d:
                Phone.append(row[0])

            query='Select Address from booking'
            q=cursor.execute(query)
            d=cursor.fetchall()
            for row in d:
                Address.append(row[0])

            query='Select CheckIn from booking'
            q=cursor.execute(query)
            d=cursor.fetchall()
            for row in d:
                CheckIn.append(row[0])

            query='Select CheckOut from booking'
            q=cursor.execute(query)
            d=cursor.fetchall()
            for row in d:
                CheckOut.append(row[0])

            query='Select RoomType from booking'
            q=cursor.execute(query)
            d=cursor.fetchall()
            for row in d:
                Room.append(row[0])

            query='Select Rate from booking'
            q=cursor.execute(query)
            d=cursor.fetchall()
            for row in d:
                Price.append(row[0])
        
            if Phone!=[]:
                i=int(Cust_Id[0])
                print("\t\t\t\t\t\t\t\t	 *** HOTEL RECORD ***\n")
                print("\t\t-----------------------------------------------------------------------------------------------------------------------------------------")
                print("\t\t| Name        \t | Phone No. \t| Address	 \t| Check-In \t| Check-Out	 \t| Room Type	 \t| Price	 \t|")
                print("\t\t-----------------------------------------------------------------------------------------------------------------------------------------")
                for n in range(0,i):
                    print("\t\t|",Name[n],"\t |",Phone[n],"\t|",Address[n],"\t\t|",CheckIn[n],"\t|",CheckOut[n],"\t\t|",Room[n],"\t\t|",Price[n],"\t\t|")
                print("\t\t-----------------------------------------------------------------------------------------------------------------------------------------")

            else:
                print("No Records Found")
        elif ch==3:  
            query='select CustomerId from booking order by CustomerId desc ;'
            q=cursor.execute(query)
            d=cursor.fetchall()

            if d==[]:
                i=0
            else:
                ele=d[0]
                i=int(ele[0])

            query='Select CustomerId from booking'
            q=cursor.execute(query)
            d=cursor.fetchall()
            for row in d:
                Cust_Id.append(row[0])
            
            query='Select RoomNumber from booking'
            q=cursor.execute(query)
            d=cursor.fetchall()
            for row in d:
                Room_No.append(row[0])

            query='Select Name from booking'
            q=cursor.execute(query)
            d=cursor.fetchall()
            for row in d:
                Name.append(row[0])

            query='Select PhoneNumber from booking'
            q=cursor.execute(query)
            d=cursor.fetchall()
            for row in d:
                Phone.append(row[0])

            query='Select Address from booking'
            q=cursor.execute(query)
            d=cursor.fetchall()
            for row in d:
                Address.append(row[0])

            query='Select CheckIn from booking'
            q=cursor.execute(query)
            d=cursor.fetchall()
            for row in d:
                CheckIn.append(row[0])

            query='Select CheckOut from booking'
            q=cursor.execute(query)
            d=cursor.fetchall()
            for row in d:
                CheckOut.append(row[0])

            query='Select RoomType from booking'
            q=cursor.execute(query)
            d=cursor.fetchall()
            for row in d:
                Room.append(row[0])

            query='Select Rate from booking'
            q=cursor.execute(query)
            d=cursor.fetchall()
            for row in d:
                Price.append(row[0])
        
            if Phone!=[]:
                i=int(Cust_Id[0])
                print("\t\t\t\t\t\t\t\t	 *** HOTEL RECORD ***\n")
                print("\t\t-----------------------------------------------------------------------------------------------------------------------------------------")
                print("\t\t| Name        \t | Phone No. \t| Address	 \t| Check-In \t| Check-Out	 \t| Room Type	 \t| Price	 \t|")
                print("\t\t-----------------------------------------------------------------------------------------------------------------------------------------")
                for n in range(0,i):
                    print("\t\t|",Name[n],"\t |",Phone[n],"\t|",Address[n],"\t\t|",CheckIn[n],"\t|",CheckOut[n],"\t\t|",Room[n],"\t\t|",Price[n],"\t\t|")
                print("\t\t-----------------------------------------------------------------------------------------------------------------------------------------")

            else:
                print("No Records Found")
        elif ch==0:
            break
        else:
            print("\t\t\t\t\t\t\t\t!!!Invalid Input!!!")
            print("\t\t\t\t\t\t\t\t!!!Try Again!!!")

    while True:
        ch=int(input("\t\t\t\t0-BACK\n\t\t\t\t ->"))
        if ch==0:
            break
        else:
            print("\t\t\t\t\t\t\t\t!!!Invalid Input!!!")
            print("\t\t\t\t\t\t\t\t!!!Try Again!!!")