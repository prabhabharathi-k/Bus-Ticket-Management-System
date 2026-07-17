import mysql.connector as sql
connected=sql.connect(host="127.0.0.1",user="root",db="bus_ticket")
cur=connected.cursor()
connected.autocommit=True

class BusticketSystem:
    def __init__(self):
        self.places=["Negamam", "Sinneripalayam", "Mootampalayam", "Thanneerpandhal", "Thoppampatti", "Rasakapalayam", "Puliyampatti","Towermedu", "Vijayapuram", "Kottampatti", "Shanthi", "Newscheamroad", "Pinky", "Pollachi"]
        self.tickets=[]
    def show_places(self):
        print("Available places:")
        print(self.places)
        cur.execute("select * from place")
        towns=cur.fetchall()
        if not towns:
            print("no places found")
            return
        for town in towns:
            sno,city=town
            print("\n",sno,city)
        connected.commit()
    def child_ticket(self):
        ticket_type="Child"
        start_place= int(input("Enter starting place number: "))
        end_place= int(input("Enter ending place number: "))
        members = int(input("Enter number of members: "))
        distance = abs(start_place - end_place)
        cost = distance * 3
        total = cost * members
        route =(self.places[start_place-1]+
                " - "+self.places[end_place-1])
        self.tickets.append({
            "Ticket type":ticket_type,
            "Route": route,
            "Members": members,
            "Total": total
        })
        print("Ticket type:",ticket_type)
        print("Route:",route)
        print("Total Price: ₹",total)
        c_child = "insert into bus_route (ticket_type, start_place, end_place, route, members, total) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (ticket_type,start_place, end_place, route, members, total)
        cur.execute(c_child, values)
        connected.commit()

    def adult_ticket(self):
        ticket_type="Adult"
        start_place = int(input("Enter starting place number: "))
        end_place = int(input("Enter ending place number: "))
        members = int(input("Enter number of members: "))
        distance = abs(start_place - end_place)
        cost = distance * 5
        total = cost * members
        route=self.places[start_place-1]+" - "+self.places[end_place-1]
        self.tickets.append({
            "Ticket type":ticket_type,
            "Route":route,
            "Members":members,
            "Total":total
        })
        print("Ticket type:",ticket_type)
        print("Route:",route)
        print("Total Price: ₹",total)
        a_adult = "insert into bus_route (ticket_type, start_place, end_place, route, members, total) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (ticket_type, start_place, end_place, route, members, total)
        cur.execute(a_adult, values)
        connected.commit()

    def handi_crapped(self):
        having_pass = input("if have pass say yes:")
        if having_pass == "yes":
            ticket_type="handi crapped"
            start_place= int(input("Enter starting place number: "))
            end_place= int(input("Enter ending place number: "))
            members = int(input("Enter number of members: "))
            distance = abs(start_place - end_place)
            cost = distance * 0
            total = cost * members
            route=self.places[start_place-1]+" - "+self.places[end_place-1]
            self.tickets.append({
                "Ticket type":ticket_type,
                "Route": route,
                "Members": members,
                "Total":total
            })
            print("Ticket type:", ticket_type)
            print("Route:", route)
            print("members:", members)
            print("Total_price:",total)
            h_handi_crapped = "insert into bus_route (ticket_type, start_place, end_place, route, members, total) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (ticket_type, start_place, end_place, route, members, total)
            cur.execute(h_handi_crapped,values)
            connected.commit()
        else:
            ticket_type="handi crapped"
            start_place= int(input("Enter starting place number: "))
            end_place= int(input("Enter ending place number: "))
            members = int(input("Enter number of members: "))
            distance = abs(start_place - end_place)
            cost = distance * 1
            total = cost * members
            route=self.places[start_place-1]+" - "+self.places[end_place-1]
            self.tickets.append({
                "Ticket type":ticket_type,
                "Route": route,
                "Members": members,
                "Total": total
            })
            print("Apply for pass...")
            print("Ticket type:", ticket_type)
            print("Route:", route)
            print("Total Price:", total)
            h_handi_crapped = "insert into bus_route (ticket_type, start_place, end_place, route, members, total) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (ticket_type, start_place, end_place, route, members, total)
            cur.execute(h_handi_crapped, values)
            connected.commit()

    def school_students(self):
        ticket_type="School Student"
        start_place= int(input("Enter starting place number: "))
        end_place= int(input("Enter ending place number: "))
        members = int(input("Enter number of members: "))
        distance = abs(start_place - end_place)
        cost = distance * 0
        total = cost * members
        route = self.places[start_place - 1] + " - " + self.places[end_place - 1]
        self.tickets.append({
            "Ticket type": ticket_type,
            "Route": route,
            "Members": members,
            "Total": total
        })
        print("Ticket type:", ticket_type)
        print("Route:", route)
        print("members:", members)
        print("Total_price:", total)
        s_school_students = "insert into bus_route (ticket_type, start_place, end_place, route, members, total) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (ticket_type, start_place, end_place, route, members, total)
        cur.execute(s_school_students, values)
        connected.commit()

    def college_students(self):
        having_pass = input("if have pass say yes:")
        if having_pass == "yes":
            ticket_type = "College Student"
            start_place = int(input("Enter starting place number: "))
            end_place = int(input("Enter ending place number: "))
            members = int(input("Enter number of members: "))
            distance = abs(start_place - end_place)
            cost = distance * 0
            total = cost * members
            route = self.places[start_place - 1] + " - " + self.places[end_place - 1]
            self.tickets.append({
                "Ticket type": ticket_type,
                "Route": route,
                "Members": members,
                "Total": total
            })
            print("Ticket type:", ticket_type)
            print("Route:", route)
            print("members:", members)
            print("Total_price:", total)
            c_college_students = "insert into bus_route (ticket_type, start_place, end_place, route, members, total) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (ticket_type, start_place, end_place, route, members, total)
            cur.execute(c_college_students, values)
            connected.commit()
        else:
            ticket_type = "college student"
            start_place = int(input("Enter starting place number: "))
            end_place = int(input("Enter ending place number: "))
            members = int(input("Enter number of members: "))
            distance = abs(start_place - end_place)
            cost = distance * 3
            total = cost * members
            route = self.places[start_place - 1] + " - " + self.places[end_place - 1]
            self.tickets.append({
                "Ticket type": ticket_type,
                "Route": route,
                "Members": members,
                "Total": total
            })
            print("Ticket type:", ticket_type)
            print("Route:", route)
            print("members:", members)
            print("Total_price:", total)
            c_college_students = "insert into bus_route (ticket_type, start_place, end_place, route, members, total) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (ticket_type, start_place, end_place, route, members, total)
            cur.execute(c_college_students, values)
            connected.commit()

    def luggage(self):
        ticket_type="Luggage"
        start_place= int(input("Enter starting place number: "))
        end_place= int(input("Enter ending place number: "))
        members = int(input("Enter number of luggage: "))
        distance = abs(start_place - end_place)
        cost = distance * 8
        total = cost * members
        route = self.places[start_place - 1] + " - " + self.places[end_place - 1]
        self.tickets.append({
            "Ticket type": ticket_type,
            "Route": route,
            "Members": members,
            "Total": total
        })
        print("Ticket type:", ticket_type)
        print("Route:", route)
        print("members:", members)
        print("Total Price:", total)
        l_luggage = "insert into bus_route (ticket_type, start_place, end_place, route, members, total) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (ticket_type, start_place, end_place, route, members, total)
        cur.execute(l_luggage, values)
        connected.commit()

    def without_tickets(self):
        ticket_type= "DONT HAVE TICKETS"
        start_place= int(input("Enter starting place number: "))
        end_place= int(input("Enter ending place number: "))
        members = int(input("Enter number of members: "))
        distance = abs(start_place - end_place)
        cost = distance * 20
        total = cost * members
        route = self.places[start_place - 1] + " - " + self.places[end_place - 1]
        self.tickets.append({
            "Ticket type": ticket_type,
            "Route": route,
            "Members": members,
            "Total": total

        })
        print("Ticket type:", ticket_type)
        print("Route:", route)
        print("members:", members)
        print("Total Price:", total)
        w_without_tickets= "insert into bus_route (ticket_type, start_place, end_place, route, members, total) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (ticket_type, start_place, end_place, route, members, total)
        cur.execute(w_without_tickets,values)
        connected.commit()

    def view_tickets(self):
        print("VIEW ALL TICKETS")
        if not self.tickets:
            print("No tickets in memory")
        else:
            print("Local Booked Tickets")
            for s_no, t in enumerate(self.tickets, 1):
                print(s_no, ".",t["Ticket type"], "|",t["Route"], "| Members:",t["Members"], "| ₹",t["Total"])
        print("Database Tickets")
        db_cursor = connected.cursor(dictionary=True)
        db_cursor.execute("SELECT * FROM bus_route")
        rows = db_cursor.fetchall()

        if not rows:
            print("No tickets found in database")
            return
        for s_no, row in enumerate(rows, 1):
            print(s_no, ".",
                  row["ticket_type"], "|",
                  row["route"], "| Members:",
                  row["members"], "| ₹",
                  row["total"])


    def add_ticket(self):
            sno=int(input("enter s no:"))
            city= input("Enter new place: ")
            self.places.append(city)
            print("Place added successfully!")
            new_city = "INSERT INTO place (sno, city) VALUES (%s, %s)"
            values = (sno, city)
            cur.execute(new_city, values)
            connected.commit()

    def pay_later(self):
        self.name = input("Enter name: ")
        self.aadhar_no = input("Enter Aadhar no: ")

        print("1.Child  2.Adult  3.School  4.College  5.Handicapped  6.Luggage  7.Without Ticket")
        choice = int(input("Enter choice: "))

        if choice == 1:
            self.child_ticket()
        elif choice == 2:
            self.adult_ticket()
        elif choice == 3:
            self.school_students()
        elif choice == 4:
            self.college_students()
        elif choice == 5:
            self.handi_crapped()
        elif choice == 6:
            self.luggage()
        elif choice == 7:
            self.without_tickets()
        else:
            print("Invalid choice")
            return

        # get last ticket
        last_ticket = self.tickets[-1]

        # use correct key
        amount = last_ticket.get("Total", 0)
        cur.execute(
            "INSERT INTO pay_later (name, aadhar_no, amount) VALUES (%s,%s,%s)",
            (self.name, self.aadhar_no, amount)
        )
        connected.commit()

        print("Saved successfully!")

    def view_pay_later(self):
        print("\n--- PAY LATER DETAILS ---")

        cur.execute("SELECT name, aadhar_no, amount FROM pay_later")
        rows = cur.fetchall()

        if not rows:
            print("No records found")
            return

        for row in rows:
            print("Name:", row[0], "| Aadhar:", row[1], "| Amount: ₹", row[2])










