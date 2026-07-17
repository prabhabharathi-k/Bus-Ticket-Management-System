from prabha import *
b=BusticketSystem()
while True:
    print("1.Show places")
    print("2.Child")
    print("3.Adult")
    print("4.View Booked Tickets")
    print("5.Add")
    print("6.Handicrapped")
    print("7.school students")
    print("8.college students")
    print("9.luggage")
    print("10.without ticket")
    print("11.pay_later")
    print("12.view_pay_later")
    print("13.Exit")
    choice=int(input("Enter choice: "))

    if choice == 1:
        b.show_places()
    elif choice == 2:
        b.child_ticket()
    elif choice == 3:
        b.adult_ticket()
    elif choice == 4:
        b.view_tickets()
    elif choice == 5:
        b.add_ticket()
    elif choice == 6:
        b.handi_crapped()
    elif choice == 7:
        b.school_students()
    elif choice == 8:
        b.college_students()
    elif choice == 9:
        b.luggage()
    elif choice == 10:
        b.without_tickets()
    elif choice == 11:
        b.pay_later()
    elif choice == 12:
        b.view_pay_later()
    elif choice == 13:
        quit()
    else:
        print("Invalid choice")