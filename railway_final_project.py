import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="password", database="railways")
mycursor = mydb.cursor()


# mycursor.execute("Show tables")
# for db in mycursor:
#   print(db)
def showall():
    mycursor.execute("select * from passengers")
    myresult = mycursor.fetchall()
    for rows in myresult:
        print(rows)
        print("\n")


def search():
    id = input("Enter id ")
    sql = "select pid,pname,page,ticket_no,DATE_FORMAT(doj,'%d-%m-%y') as DOJ from passengers where pid = %s"
    id = (id,)
    # print(id)
    mycursor.execute(sql, id)
    result = mycursor.fetchone()
    print(result)


def insert():
    sql = "insert into passengers(PNAME,PAGE,TNO,TNAME,DOJ,TICKET_NO,COACH,SEATS) values (%s,%s,%s,%s,%s,%s,%s,%s)"
    print("enter name : ")
    name = input()
    print("enter age : ")
    age = int(input())
    print("enter train no : ")
    tno = input()
    if (tno == 'T1' or tno == 'T2' or tno == 'T3' or tno == 'T4' or tno == 'T5'):

        print("enter Train name : ")
        tname = input()
        print("enter DOJ : ")
        doj = input()
        print(doj)
        print("Enter ticket no : ")
        copy = ticketno = int(input())
        print("Enter couch : ")
        coach = input()
        print("Enter seats : ")
        s = seats = int(input())
        if (seats > 0 and seats < 6):
            t = (name, age, tno, tname, doj, ticketno, coach, seats)
            mycursor.execute(sql,t)
            # print(ticketno)
            # ticket(ticketno)
            mydb.commit()
            ticket(copy)
            print("Ticket has been booked sucessfully : ")
        else:
            print("You cannot book ticket more than 5 ")
    else:
        print("Such Type of Train no. does't exit ")


def ticket(a):
    tic = a

    a = (a,)
    sql = "select pid from passengers where ticket_no=%s"
    mycursor.execute(sql, a)
    id = mycursor.fetchone()
    # print("PASSENGER'S ID : ",id)
    # getting price
    sql = "select TNO FROM passengers where pid=%s"
    # id = int(input("enter id no. : "))
    # id = (id,)
    total = 0
    mycursor.execute(sql, id)
    tno = mycursor.fetchone()
    sql = "select seats FROM passengers where pid=%s"
    mycursor.execute(sql, id)
    seats = mycursor.fetchone()
    sql = "select coach FROM passengers where pid=%s"
    mycursor.execute(sql, id)
    coach = mycursor.fetchone()
    # print("tno : ", tno)
    # print("seats : ", seats)

    # print("coach : ", coach)
    seats = list(seats)
    coach = list(coach)

    coach = ''.join(coach)  # changing coach into string :
    # print((coach))

    # seats= int(seats)
    for i in seats:  # converting list into interger value :
        p = int(i)

        # print("seats : ",p)
        # print(n)
        # help(mycursor.execute)
    if (coach == 'A1'):
        sql = "select A1 from fair where TNO=%s"

        mycursor.execute(sql, tno)
        fair = mycursor.fetchone()
        fair = list(fair)
        for i in fair:
            n = int(i)
        total = n * p
        # print("Total fair : ", n * p)
    elif (coach == 'B1'):
        sql = "select B1 from fair where Tno=%s"
        mycursor.execute(sql, tno)
        fair = mycursor.fetchone()
        fair = list(fair)
        for i in fair:
            n = int(i)
            total = n * p
        # print("Total fair : ",total)
    else:
        sql = "select S1 from fair where Tno=%s"
        mycursor.execute(sql, tno)
        fair = mycursor.fetchone()
        fair = list(fair)
        for i in fair:
            n = int(i)
        total = n * p
        # print(n)
        # print("Total fair : ", n * p)

    s = "insert into ticket(ticket_no,price) values(%s,%s)"
    # a=list(a)
    # a=''.join(a)
    # print("ticket no : ",a)
    t = (tic, total)

    mycursor.execute(s, t)
    mydb.commit()
    sql = "select seats from passengers where tno=%s"
    mycursor.execute(sql, tno)
    s = mycursor.fetchone()
    s = list(s)
    for i in s:
        seats = i
    if (coach == "A1"):
        sql = "select avail_A1 from seats where tno=%s"
        mycursor.execute(sql, tno)
        avail = mycursor.fetchone()
        avail = list(avail)
        for i in avail:
            new_avail = i
        if (new_avail > seats):
            status = "C"
            sql = "update ticket set status=%s where ticket_no=%s"
            t = (status, tic)
            mycursor.execute(sql, t)
            mydb.commit()
            c = 1
        else:
            status = "W"
            sql = "update ticket set status=%s where ticket_no=%s"
            t = (status, tic)
            mycursor.execute(sql, t)
            mydb.commit()
            c = 0
    elif (coach == "B1"):
        sql = "select avail_B1 from seats where tno=%s"
        mycursor.execute(sql, tno)
        avail = mycursor.fetchone()
        avail = list(avail)
        for i in avail:
            new_avail = i
        if (new_avail > seats):
            status = "S"
            sql = "update ticket set status=%s where ticket_no=%s"
            t = (status, tic)
            mycursor.execute(sql, t)
            mydb.commit()
            c = 1
        else:
            status = "W"
            sql = "update ticket set status=%s where ticket_no=%s"
            t = (status, tic)
            mycursor.execute(sql, t)
            mydb.commit()
            c = 0
    else:
        sql = "select avail_S1 from seats where tno=%s"
        mycursor.execute(sql, tno)
        avail = mycursor.fetchone()
        avail = list(avail)
        for i in avail:
            new_avail = i
        if (new_avail > seats):
            status = "S"
            sql = "update ticket set status=%s where ticket_no=%s"
            t = (status, tic)
            mycursor.execute(sql, t)
            mydb.commit()
            c = 1
        else:
            status = "W"
            sql = "update ticket set status=%s where ticket_no=%s"
            t = (status, tic)
            mycursor.execute(sql, t)
            mydb.commit()
            c = 0

    ##### coding for seats table starts : #####

    # converting into tuple
    sql1 = "select coach from passengers where pid=%s"
    sql2 = "select seats from passengers where pid=%s"
    sql3 = "select tno from passengers where pid=%s"
    mycursor.execute(sql1, id)
    coach = mycursor.fetchone()
    mycursor.execute(sql2, id)
    seats = mycursor.fetchone()
    mycursor.execute(sql3, id)
    tno = mycursor.fetchone()
    # print(coach)
    seats = list(seats)
    for i in seats:
        avail = i
    # print("Seats : ",avail)
    coach = list(coach)

    coach = ''.join(coach)
    # print("Coach : ",coach)
    # print("Tno : ",tno)
    if(c==1):
        if (coach == 'A1'):
            sql = "select total_a1 from seats where tno=%s"
            mycursor.execute(sql, tno)
            a = mycursor.fetchone()
            a = list(a)
            for i in a:
                total_seats = i
            new_avail = total_seats - avail
        # print("new_avail : ",new_avail)

            sql = "update seats set avail_A1=%s where tno=%s"
            tno = list(tno)
            tno = ''.join(tno)
            t = (new_avail, tno)
            mycursor.execute(sql, t)
            mydb.commit()

        elif (coach == 'B1'):
            sql = "select total_b1 from seats where tno=%s"
            mycursor.execute(sql, tno)
            a = mycursor.fetchone()
            a = list(a)
            for i in a:
                total_seats = i
            new_avail = total_seats - avail
        # print("new_avail : ", new_avail)

            sql = "update seats set avail_b1=%s where tno=%s"
            tno = list(tno)
            tno = ''.join(tno)
            t = (new_avail, tno)
            mycursor.execute(sql, t)
            mydb.commit()
        else:
            sql = "select total_s1 from seats where tno=%s"
            mycursor.execute(sql, tno)
            a = mycursor.fetchone()
            a = list(a)
            for i in a:
                total_seats = i
            new_avail = total_seats - avail
        # print("new_avail : ", new_avail)

            sql = "update seats set avail_s1=%s where tno=%s"
            tno = list(tno)
            tno = ''.join(tno)
            t = (new_avail, tno)
            mycursor.execute(sql, t)
            mydb.commit()
    else:
        pass

def cancel():
    tic = int(input("Enter ticket_no : "))
    tic = (tic,)

    sql1 = "select seats from passengers where ticket_no=%s"
    sql2 = "select coach from passengers where ticket_no=%s"
    sql3 = "select tno from passengers where ticket_no = %s"
    mycursor.execute(sql1, tic)
    book = mycursor.fetchone()
    mycursor.execute(sql2, tic)
    coach = mycursor.fetchone()
    mycursor.execute(sql3, tic)
    tno = mycursor.fetchone()
    book = list(book)
    for i in book:
        seats = i
    coach = list(coach)
    coach = ''.join(coach)
    # print("seats : ",seats)
    # print("coach : ",coach)
    # print("tno   : ",tno)

    if (coach == 'A1'):
        sql = "select avail_A1 from seats where tno = %s"
        mycursor.execute(sql, tno)
        avail_a1 = mycursor.fetchone()
        avail_a1 = list(avail_a1)
        for i in avail_a1:
            avail = i
        new_avail = avail + seats
        tno = list(tno)
        tno = ''.join(tno)
        sql = "update seats set avail_A1=%s where tno = %s"
        t = (new_avail, tno)
        mycursor.execute(sql, t)
        mydb.commit()


    elif (coach == 'B1'):
        sql = "select avail_B1 from seats where tno = %s"
        mycursor.execute(sql, tno)
        avail_b1 = mycursor.fetchone()
        avail_b1 = list(avail_b1)
        for i in avail_b1:
            avail = i
        new_avail = avail + seats
        tno = list(tno)
        tno = ''.join(tno)
        sql = "update seats set avail_b1=%s where tno = %s"
        t = (new_avail, tno)
        mycursor.execute(sql, t)
        mydb.commit()

    else:
        sql = "select avail_s1 from seats where tno = %s"
        mycursor.execute(sql, tno)
        avail_s1 = mycursor.fetchone()
        avail_s1 = list(avail_s1)
        for i in avail_s1:
            avail = i
        new_avail = avail + seats
        tno = list(tno)
        tno = ''.join(tno)
        sql = "update seats set avail_s1=%s where tno = %s"
        t = (new_avail, tno)
        mycursor.execute(sql, t)
        mydb.commit()

    sql1 = "delete from passengers where TICKET_NO =%s"
    sql2 = "delete from ticket where Ticket_No = %s"
    mycursor.execute(sql1, tic)
    mydb.commit()
    mycursor.execute(sql2, tic)
    mydb.commit()
    print("Ticket has been cancelled successfully")


def ticket_record():
    # showing full records of the ticket's:
    mycursor.execute("select * from ticket")
    myresult = mycursor.fetchall()
    for rows in myresult:
        print(rows)
        print("\n")


def update_ticket():
    print("Enter Passenger id  : ")
    pid = int(input())
    name = input("Enter the new name : ")
    age = int(input("Enter the new age  : "))
    doj = input("Enter the new date of journey : ")
    t = (name, age, doj, pid)
    sql = "UPDATE passengers set PNAME =%s,PAGE =%s,DOJ= %s where pid = %s"
    mycursor.execute(sql, t)
    mydb.commit()
    print("Data has been updated successfully ")


def all_seats():
    sql = 'select * from seats'
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    print("tno  a1  b1  s1  a_a1  a_b1  a_s1")
    for rows in myresult:
        print(rows)
        print('\n')


def main():
    print("Enter 1 for reading all the records           : ")
    print("Enter 2 to book ticket                        : ")
    print("Enter 3 to get details of a passenger         : ")
    print("Enter 4 to cancel any ticket                  : ")
    print("Enter 5 to get information about the ticket   : ")
    print("Enter 6 to update any ticket                  : ")
    print("Enter 7 to see availabity of seats            : ")
    print("Enter 8 to exit  : ")
    a = int(input())
    if a == 1:
        showall()
    elif a == 2:
        insert()

    elif a == 3:
        search()
    elif a == 4:
        cancel()
    elif (a == 5):
        # showing full records of the ticket's:
        ticket_record()

    elif (a == 6):
        update_ticket()
    elif (a == 7):
        all_seats()
    else:
        print("you entered invalid value ")


print("Enter user name : ")
username = input()
print("Enter password  : ")
password = input()
if (username == 'admin' and password == 'password'):
    main()
else:
    print("Invalid login ")

