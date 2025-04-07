import mysql.connector
Cust_Id=[]
R_Bill=[]
r=0

def Main():
    conn = mysql.connector.connect(host='localhost', user='root', password='12345678',  database='hotel')
    cursor=conn.cursor(buffered=True)

    cursor.execute("create table if not exists Resturant( CustomerId varchar(5),ResturantBill varchar(5));")

    query='Select CustomerId from booking'
    q=cursor.execute(query)
    d=cursor.fetchall()
    for row in d:
        Cust_Id.append(row[0])

    def Room_Service():
        global r
        ph=input("\t\t\t\tEnter Your Customer Id: ")
        if ph in Cust_Id:
            print("\t\t\t-------------------------------------------------------------------------")
            print("				 Hotel Paradise")
            print("\t\t\t-------------------------------------------------------------------------")
            print("				 Menu Card")
            print("\t\t\t-------------------------------------------------------------------------")
            print("\n\t\t\t BEVARAGES			  \t 26 Dal Fry................ 140.00")
            print("\t\t\t----------------------------------	 27 Dal Makhani............ 150.00")
            print("\t\t\t 1 Regular Tea............. 20.00	 28 Dal Tadka.............. 150.00")
            print("\t\t\t 2 Masala Tea.............. 25.00")
            print("\t\t\t 3 Coffee.................. 25.00	 ROTI")
            print("\t\t\t 4 Cold Drink.............. 25.00	 ----------------------------------")
            print("\t\t\t 5 Bread Butter............ 30.00	 29 Plain Roti.............. 15.00")
            print("\t\t\t 6 Bread Jam............... 30.00	 30 Butter Roti............. 15.00")
            print("\t\t\t 7 Veg. Sandwich........... 50.00	 31 Tandoori Roti........... 20.00")
            print("\t\t\t 8 Veg. Toast Sandwich..... 50.00	 32 Butter Naan............. 20.00")
            print("\t\t\t 9 Cheese Toast Sandwich... 70.00")
            print("\t\t\t 10 Grilled Sandwich........ 70.00	 RICE")
            print("\t\t\t\t				----------------------------------")
            print("\t\t\t SOUPS					 33 Plain Rice.............. 90.00")
            print("\t\t\t----------------------------------	 34 Jeera Rice.............. 90.00")
            print("\t\t\t 11 Tomato Soup............ 110.00	 35 Veg Pulao.............. 110.00")
            print("\t\t\t 12 Hot & Sour............. 110.00	 36 Peas Pulao............. 110.00")
            print("\t\t\t 13 Veg. Noodle Soup....... 110.00")
            print("\t\t\t 14 Sweet Corn............. 110.00	 SOUTH INDIAN")
            print("\t\t\t 15 Veg. Munchow........... 110.00	 ----------------------------------")
            print("\t							37 Plain Dosa............. 100.00")
            print("\t\t\t MAIN COURSE				 38 Onion Dosa............. 110.00")
            print("\t\t\t----------------------------------	 39 Masala Dosa............ 130.00")
            print("\t\t\t 16 Shahi Paneer........... 110.00	 40 Paneer Dosa............ 130.00")
            print("\t\t\t 17 Kadai Paneer........... 110.00	 41 Rice Idli.............. 130.00")
            print("\t\t\t 18 Handi Paneer........... 120.00	 42 Sambhar Vada........... 140.00")
            print("\t\t\t 19 Palak Paneer........... 120.00")
            print("\t\t\t 20 Chilli Paneer.......... 140.00	 ICE CREAM")
            print("\t\t\t 21 Matar Mushroom......... 140.00	 ----------------------------------")
            print("\t\t\t 22 Mix Veg................ 140.00	 43 Vanilla................. 60.00")
            print("\t\t\t 23 Jeera Aloo............. 140.00	 44 Strawberry.............. 60.00")
            print("\t\t\t 24 Malai Kofta............ 140.00	 45 Pineapple............... 60.00")
            print("\t\t\t 25 Aloo Matar............. 140.00	 46 Butter Scotch........... 60.00")
            print("\t\t\tPress 0 -to end ")
            ch=1
            while(ch!=0):
                
                ch=int(input("\t\t\t\t -> "))
                
                if ch==1 or ch==31 or ch==32:
                    rs=20
                    r=r+rs
                elif ch<=4 and ch>=2:
                    rs=25
                    r=r+rs
                elif ch<=6 and ch>=5:
                    rs=30
                    r=r+rs
                elif ch<=8 and ch>=7:
                    rs=50
                    r=r+rs
                elif ch<=10 and ch>=9:
                    rs=70
                    r=r+rs
                elif (ch<=17 and ch>=11) or ch==35 or ch==36 or ch==38:
                    rs=110
                    r=r+rs
                elif ch<=19 and ch>=18:
                    rs=120
                    r=r+rs
                elif (ch<=26 and ch>=20) or ch==42:
                    rs=140
                    r=r+rs
                elif ch<=28 and ch>=27:
                    rs=150
                    r=r+rs
                elif ch<=30 and ch>=29:
                    rs=15
                    r=r+rs
                elif ch==33 or ch==34:
                    rs=90
                    r=r+rs
                elif ch==37:
                    rs=100
                    r=r+rs
                elif ch<=41 and ch>=39:
                    rs=130
                    r=r+rs
                elif ch<=46 and ch>=43:
                    rs=60
                    r=r+rs
                elif ch==0:
                    pass
                else:
                    print("\t\t\t\tWrong Choice..!!")
            print("\t\t\t\tTotal Bill: ",r)
            R_Bill.append(r)
            query='INSERT INTO Resturant(CustomerId,ResturantBill) Values("'+str(ph)+'","'+str(r)+'");'
            cursor.execute(query)
            conn.commit()
        else:
            print("\t\t\t\tInvalid Customer Id")
        while True:
            n=int(input("\t\t\t\tEnter 0 To Go BACK\n\t\t\t\t->"))
            if n==0:
                break
            else:
                print("\t\t\t\t\t\t\t\t!!!Invalid Input!!!")
                print("\t\t\t\t\t\t\t\t!!!Try Again!!!")

    Room_Service()