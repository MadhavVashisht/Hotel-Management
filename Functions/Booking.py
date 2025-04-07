from datetime import date
import datetime
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
room=0
R1=R2=R3=R4=R5=R6=0

R=''

Today=date.today()
D1=Today.strftime("%d/%m/%Y")

conn = mysql.connector.connect(host='localhost', user='root', password='12345678',  database='hotel')
cursor=conn.cursor(buffered=True)

cursor.execute("create table if not exists Booking( CustomerId varchar(5),RoomNumber varchar(4),Name varchar(50),PhoneNumber varchar(10),Address varchar(50),CheckIn varchar(10),CheckOut varchar(10),RoomType varchar(50),Rate varchar(5));")

def Main():    
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

    print(i4)
    Booking(i)
    
def date(c):

    global i

    if c[2]>=2022 and c[2]<=2024:

        if c[1]!=0 and c[1]<=12:

            if c[1]==2 and c[0]!=0 and c[0]<=31:

                if c[2]%4==0 and c[0]<=29:
                    pass

                elif c[0]<29:
                    pass

                else:
                    print("Invalid date")
                    Name.pop(i)
                    Phone.pop(i)
                    Address.pop(i)
                    CheckIn.pop(i)
                    CheckOut.pop(i)
                    Booking(i)

            elif c[1]<=7 and c[1]%2!=0 and c[0]<=31:
                pass

            elif c[1]<=7 and c[1]%2==0 and c[0]<=30 and c[1]!=2:
                pass

            elif c[1]>=8 and c[1]%2==0 and c[0]<=31:
                pass

            elif c[1]>=8 and c[1]%2!=0 and c[0]<=30:
                pass

            else:
                print("Invalid date")
                Name.pop(i)
                Phone.pop(i)
                Address.pop(i)
                CheckIn.pop(i)
                CheckOut.pop(i)
                Booking(i)

        else:
            print("Invalid date")
            Name.pop(i)
            Phone.pop(i)
            Address.pop(i)
            CheckIn.pop(i)
            CheckOut.pop(i)
            Booking(i)
    else:
        print("Invalid date")
        Name.pop(i)
        Phone.pop(i)
        Address.pop(i)
        CheckIn.pop(i)
        CheckOut.pop(i)
        Booking(i)

def Booking(i):

    global R1,R2,R3,R4,R5,R6,cursor,D1,room,R

    print("\t\t\t\t\t\t\t\tRoom Booking")
    name=input("\t\t\t\tEnter Your Name: ")
    phone=input("\t\t\t\tEnter Your Number: ")
    address=input("\t\t\t\tEnter Your Address: ")
    if name!="" and phone!="" and address!="":
        Name.append(name)
        Phone.append(phone)
        Address.append(address)
    else:
        print("\t\t\t\t!!..Name, Phone no. & Address cannot be empty..!!")
        Booking(i)


    checkin=input("\t\t\t\tEnter Enter The Date Of Check-In In 'dd/mm/yyyy' Format: ")
    x=checkin
    if x<D1:
        print("\t\t\t\t\t\t\t\t!!!Invalid date!!!")
        print("\t\t\t\t\t\t\t\t!!!Try Again!!!")
        Name.pop(i)
        Phone.pop(i)
        Address.pop(i)
        Booking(i)
    
    CheckIn.append(checkin)
    m=checkin
    checkin=checkin.split('/')
    checkin[0]=int(checkin[0])
    checkin[1]=int(checkin[1])
    checkin[2]=int(checkin[2])
    date(checkin)

    checkout=input("\t\t\t\tEnter Enter The Date Of Check-Out In 'dd/mm/yyyy' Format: ")
    CheckOut.append(checkout)
    checkout=checkout.split('/')
    checkout[0]=int(checkout[0])
    checkout[1]=int(checkout[1])
    checkout[2]=int(checkout[2])

    if checkout[1]<checkin[1] and checkout[2]<checkin[2]:
        print("\t\t\t\tErr..!!\tCheck-Out date must fall after Check-In")
        Name.pop(i)
        Phone.pop(i)
        Address.pop(i)
        CheckIn.pop(i)
        CheckOut.pop(i)
        Booking(i)

    elif checkout[1]==checkin[1] and checkout[2]>=checkin[2] and checkout[0]<=checkin[0]:
        print("\t\t\t\tErr..!!\tCheck-Out date must fall after Check-In")
        Name.pop(i)
        Phone.pop(i)
        Address.pop(i)
        CheckIn.pop(i)
        CheckOut.pop(i)
        Booking(i)

    else:
        pass

    date(checkout)
    d1 = datetime.datetime(checkin[2],checkin[1],checkin[0])
    d2 = datetime.datetime(checkout[2],checkout[1],checkout[0])
    d = (d2-d1).days
    Days.append(d)

    while True:


        print("\t\t\t\t\t\t\t\t----SELECT ROOM TYPE----")
        print("\t\t\t\t1. Standard Non-AC")
        print("\t\t\t\t2. Standard AC")
        print("\t\t\t\t3. 2-Bed Non-AC")
        print("\t\t\t\t4. 2-Bed AC")
        print("\t\t\t\t5. 3-Bed Non-AC")
        print("\t\t\t\t6. 3-Bed AC")
        print(("\t\t\t\tPress 0 for Room Prices"))
        ch=int(input("\t\t\t\t->"))

        if ch==0:
            print("\t\t\t\t1. Standard Non-AC - Rs. 3500")
            print("\t\t\t\t2. Standard AC - Rs. 4000")
            print("\t\t\t\t3. 2-Bed Non-AC - Rs. 4500")
            print("\t\t\t\t4. 2-Bed AC - Rs. 5000")
            print("\t\t\t\t5. 3-Bed Non-AC - Rs. 5500")
            print("\t\t\t\t6. 3-Bed AC - Rs. 6000")
            ch=int(input("\t\t\t\t->"))
            break

        elif ch==1:
            if i!=0:
                query='Select CheckIn from Booking where RoomType='+ "'Standard Non-Ac'"+' order by CheckIn desc;'
                q=cursor.execute(query)
                a=cursor.fetchall()

                query='Select CheckOut from Booking where RoomType='+ "'Standard Non-Ac'"+' order by CheckOut asc;'
                q=cursor.execute(query)
                b=cursor.fetchall()
                
                query='Select RoomNumber from Booking where RoomType='+ "'Standard Non-Ac'"+' order by RoomNumber Desc;'
                q=cursor.execute(query)
                r=cursor.fetchall()
                for row in r:
                    R=int(row[0])
                
                if R!='':
                    Room.append('Standard Non-AC')
                    print("\t\t\t\tRoom Type- Standard Non-AC")
                    Price.append('3500')
                    print("\t\t\t\tPrice- 3500")
                    room=R+1
                    if room>=110 :
                        if m>=a[0] and m<=b[0]:
                            print("\t\t\t\tErr..!!\tRoom Not Available for This Date")
                            Name.pop(i)
                            Phone.pop(i)
                            Address.pop(i)
                            CheckIn.pop(i)
                            CheckOut.pop(i)
                            Booking(i)
                            print("\t\t\t\tErr..!!\tTry Again With Another Room or Date")
                        else:
                            break
                    else:
                        break
                else:
                    Room.append('Standard Non-AC')
                    print("\t\t\t\tRoom Type- Standard Non-AC")
                    Price.append('3500')
                    print("\t\t\t\tPrice- 3500")
                    room=101
            else:
                Room.append('Standard Non-AC')
                print("\t\t\t\tRoom Type- Standard Non-AC")
                Price.append('3500')
                print("\t\t\t\tPrice- 3500")
                room=101+i
        
        elif ch==2:
            if i!=0:
                query='Select CheckIn from Booking where RoomType='+ "'Standard Ac'"+' order by CheckIn desc;'
                q=cursor.execute(query)
                a=cursor.fetchall()

                query='Select CheckOut from Booking where RoomType='+ "'Standard Ac'"+' order by CheckOut asc;'
                q=cursor.execute(query)
                b=cursor.fetchall()

                query='Select RoomNumber from Booking where RoomType='+ "'Standard Ac'"+' order by RoomNumber Desc;'
                q=cursor.execute(query)
                r=cursor.fetchall()
                for row in r:
                    R=int(row[0])
                
                if R!='':
                    Room.append('Standard AC')
                    print("\t\t\t\tRoom Type- Standard AC")
                    Price.append('4000')
                    print("\t\t\t\tPrice- 4000")
                    room=R+1
                    if room>=210 :
                        if m>=a[0] and m<=b[0]:
                            print("\t\t\t\tErr..!!\tRoom Not Available for This Date")
                            Name.pop(i)
                            Phone.pop(i)
                            Address.pop(i)
                            CheckIn.pop(i)
                            CheckOut.pop(i)
                            Booking(i)
                            print("\t\t\t\tErr..!!\tTry Again With Another Room or Date")
                        else:
                            break
                    else:
                        break
                else:
                    Room.append('Standard AC')
                    print("\t\t\t\tRoom Type- Standard AC")
                    Price.append('4000')
                    print("\t\t\t\tPrice- 4000")
                    room=201
                    break
            else:
                Room.append('Standard AC')
                print("\t\t\t\tRoom Type- Standard AC")
                Price.append('4000')
                print("\t\t\t\tPrice- 4000")
                room=201+i
                break

        elif ch==3:
            if i!=0:
                query='Select CheckIn from Booking where RoomType='+ "'2-Bed Non-Ac'"+' order by CheckIn desc;'
                q=cursor.execute(query)
                a=cursor.fetchall()

                query='Select CheckOut from Booking where RoomType='+ "'2-Bed Non-Ac'"+' order by CheckOut asc;'
                q=cursor.execute(query)
                b=cursor.fetchall()

                query='Select RoomNumber from Booking where RoomType='+ "'2-Bed Non-Ac'"+' order by RoomNumber Desc;'
                q=cursor.execute(query)
                r=cursor.fetchall()
                for row in r:
                    R=int(row[0])
                
                if R!='':
                    Room.append('2-Bed Non-AC')
                    print("\t\t\t\tRoom Type- 2-Bed Non-AC")
                    Price.append('4500')
                    print("\t\t\t\tPrice- 4500")
                    room=R+1
                    if room>=310:
                        if m>=a[0] and m<=b[0]:
                            print("\t\t\t\tErr..!!\tRoom Not Available for This Date")
                            Name.pop(i)
                            Phone.pop(i)
                            Address.pop(i)
                            CheckIn.pop(i)
                            CheckOut.pop(i)
                            Booking(i)
                            print("\t\t\t\tErr..!!\tTry Again With Another Room or Date")
                        else:
                            break
                    else:
                        break
                else:    
                    Room.append('2-Bed Non-AC')
                    print("\t\t\t\tRoom Type- 2-Bed Non-AC")
                    Price.append('4500')
                    print("\t\t\t\tPrice- 4500")
                    room=301
                    break
            else:
                Room.append('2-Bed Non-AC')
                print("\t\t\t\tRoom Type- 2-Bed Non-AC")
                Price.append('4500')
                print("\t\t\t\tPrice- 4500")
                room=301+i
                break

        elif ch==4:
            if i!=0:
                query='Select CheckIn from Booking where RoomType='+ "'2-Bed Ac'"+' order by CheckIn desc;'
                q=cursor.execute(query)
                a=cursor.fetchall()

                query='Select CheckOut from Booking where RoomType='+ "'2-Bed Ac'"+' order by CheckOut asc;'
                q=cursor.execute(query)
                b=cursor.fetchall()
                
                query='Select RoomNumber from Booking where RoomType='+ "'2-Bed Ac'"+' order by RoomNumber Desc;'
                q=cursor.execute(query)
                r=cursor.fetchall()
                conn.commit()
                for row in r:
                    R=int(row[0])

                if R!='':
                    Room.append('2-Bed AC')
                    print("\t\t\t\tRoom Type- 2-Bed AC")
                    Price.append('5000')
                    print("\t\t\t\tPrice- 5000")
                    room=R+1
                    if room>=410 :
                        if m>=a[0] and m<=b[0]:
                            print("\t\t\t\tErr..!!\tRoom Not Available for This Date")
                            Name.pop(i)
                            Phone.pop(i)
                            Address.pop(i)
                            CheckIn.pop(i)
                            CheckOut.pop(i)
                            Booking(i)
                            print("\t\t\t\tErr..!!\tTry Again With Another Room or Date")
                        else:
                            break
                    else:
                        break
                else:
                    Room.append('2-Bed AC')
                    print("\t\t\t\tRoom Type- 2-Bed AC")
                    Price.append('5000')
                    print("\t\t\t\tPrice- 5000")
                    room=401
                    break
            else:
                Room.append('2-Bed AC')
                print("\t\t\t\tRoom Type- 2-Bed AC")
                Price.append('5000')
                print("\t\t\t\tPrice- 5000")
                room=401+i
                break

        elif ch==5:
            if i!=0:
                query='Select CheckIn from Booking where RoomType='+ "'3-Bed Non-Ac'"+' order by CheckIn desc;'
                q=cursor.execute(query)
                a=cursor.fetchall()

                query='Select CheckOut from Booking where RoomType='+ "'3-Bed Non-Ac'"+' order by CheckOut asc;'
                q=cursor.execute(query)
                b=cursor.fetchall()
                
                query='Select RoomNumber from Booking where RoomType='+ "'3-Bed Non-Ac'"+' order by RoomNumber desc;'
                q=cursor.execute(query)
                r=cursor.fetchall()
                for row in r:
                    R=int(row[0])

                if R!='':
                    Room.append('3-Bed Non-AC')
                    print("\t\t\t\tRoom Type- 3-Bed Non-AC")
                    Price.append('5500')
                    print("\t\t\t\tPrice- 5500")
                    room=R+1
                    if room>=510 :
                        if m>=a[0] and m<=b[0]:
                            print("\t\t\t\tErr..!!\tRoom Not Available for This Date")
                            Name.pop(i)
                            Phone.pop(i)
                            Address.pop(i)
                            CheckIn.pop(i)
                            CheckOut.pop(i)
                            Booking(i)
                            print("\t\t\t\tErr..!!\tTry Again With Another Room or Date")
                        else:
                            break
                    else:
                        break
                else:
                    Room.append('3-Bed Non-AC')
                    print("\t\t\t\tRoom Type- 3-Bed Non-AC")
                    Price.append('5500')
                    print("\t\t\t\tPrice- 5500")
                    room=501
            else:
                Room.append('3-Bed Non-AC')
                print("\t\t\t\tRoom Type- 3-Bed Non-AC")
                Price.append('5500')
                print("\t\t\t\tPrice- 5500")
                room=501+i

        elif ch==6:
            if i!=0:
                query='Select CheckIn from Booking where RoomType='+ "'3-Bed Ac'"+' order by CheckIn desc;'
                q=cursor.execute(query)
                a=cursor.fetchall()

                query='Select CheckOut from Booking where RoomType='+ "'3-Bed Ac'"+' order by CheckOut asc;'
                q=cursor.execute(query)
                b=cursor.fetchall()
                
                query='Select RoomNumber from Booking where RoomType='+ "'3-Bed Ac'"+' order by RoomNumber desc;'
                q=cursor.execute(query)
                r=cursor.fetchall()
                for row in r:
                    R=int(row[0])
                
                if R!='':
                    Room.append('3-Bed AC')
                    print("\t\t\t\tRoom Type- 3-Bed AC")
                    Price.append('6000')
                    print("\t\t\t\tPrice- 6000")
                    room=R+1
                    if room>=610 :
                        if m>=a[0] and m<=b[0]:
                            print("\t\t\t\tErr..!!\tRoom Not Available for This Date")
                            Name.pop(i)
                            Phone.pop(i)
                            Address.pop(i)
                            CheckIn.pop(i)
                            CheckOut.pop(i)
                            Booking(i)
                            print("\t\t\t\tErr..!!\tTry Again With Another Room or Date")
                        else:
                            break
                    else:
                        break
                else:
                    Room.append('3-Bed AC')
                    print("\t\t\t\tRoom Type- 3-Bed AC")
                    Price.append('6000')
                    print("\t\t\t\tPrice- 6000")
                    room=601
                    break
            else:
                Room.append('3-Bed AC')
                print("\t\t\t\tRoom Type- 3-Bed AC")
                Price.append('6000')
                print("\t\t\t\tPrice- 6000")
                room=601+i
                break

        else:
            print("\t\t\t\tWrong choice..!!")

    Room_num=str(room)
    Cust=i+1
    Cust_id=str(Cust)

    print("")
    print("\t\t\t\t\t\t\t\t***ROOM BOOKED SUCCESSFULLY***")
    print("\t\t\t\tRoom No. - ",Room_num)
    print("\t\t\t\tCustomer Id - ",Cust_id)
    Room_No.append(Room_num)
    Cust_Id.append(Cust_id)
    query='INSERT INTO booking (CustomerId,RoomNumber,Name,PhoneNumber,Address,CheckIn,CheckOut,RoomType,Rate) VALUES\
("'+Cust_Id[i]+'","'+Room_No[i]+'","'+Name[i]+'","'+Phone[i]+'","'+Address[i]+'","'+CheckIn[i]+'","'+CheckOut[i]+'","'+Room[i]+'","'+Price[i]+'");'
    cursor.execute(query)
    conn.commit()
    while True:
        n=int(input("\t\t\t\t0-BACK\n\t\t\t\t->"))
        if n==0:
            break
        else:
            print("\t\t\t\t\t\t\t\t!!!Invalid Input!!!")
            print("\t\t\t\t\t\t\t\t!!!Try Again!!!")