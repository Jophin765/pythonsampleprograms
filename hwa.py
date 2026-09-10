total_seats=10
price_amount=112
seats=[None]*(total_seats + 1)
while True:

    print("------Bus Ticket Booking System-----")
    print("1. Book Ticket")
    print("2.View Seat Availability")
    print("3.Cancel Ticket")
    print("4.Exit")

    choice=input("Enter your choice: ")
    if choice == "1":
        seat_available=True
        for i in range(1,total_seats+1):
            if seats[i]==None:
                break
        else:
            seat_available=False
        if seat_available == True:    
            
            name=input("Enter Passenger Name:")
            age_entered=True
            while age_entered == True:
                 age=input("Enter The Passenger Age: ")
                 if age.isdigit():
                     age=int(age)
                     age_entered=False
                 else:
                     print("Please Enter Age in Numbers only")
            print("Available Seats: ")
            for i in range(1, total_seats +1):
                if seats[i] == None:
                    print(i, end=" ")
            print()

            seat_no=input("Enter the Seat Number: ")
            if seat_no.isdigit():
                seat_no=int(seat_no)
                if seat_no >=1 and seat_no <= total_seats:
                    if seats [seat_no] == None:
                        price=price_amount

                        if age < 12:
                            price= price -(price*0.5)
                            print("Childe Discount Applied")
                        else:
                            if age > 60:
                                price= price-(price*0.3)
                                print("Senior Citizen Applied")
                            else:
                                pass

                        price=int(price)
                        pass

                        seats[seat_no]=name
                        print("Ticket Booked Successfully")
                        print("Seat Number: ", seat_no)
                        print("Final Ticket Price: ",price)
                    else:
                        print("Seat already Booked,choose another seat please")
                else:
                    print("invalid Seat Number")
            else:
                print("Plz enter Seat Number in Numbers only")
        else:
            print("Sorry all seats are booked")

    elif choice =="2":
        print("Available Seats: ")
        for i in range(1, total_seats+1):
            if seats[i] == None:
                print(i, end=" ")
        print()

    elif choice =="3":
        seat_no=input("Enter seat no to Cancel: ")
        if seat_no.isdigit():
            seat_no=int(seat_no)
            for i in range(1,total_seats+1):
                if i ==seat_no and seats[i]!=None:
                    print("Ticket Cancelled for",seats[i])
                    seats[i]=None
                    break
            else:
                print("Seat not found")
        else:
            print("Plz Enter seat no in Numbers only")

    elif choice=="4":
        print("thank you for using bus ticket booking system")
        break
    else:
        print("Invalid choice,try again ")
        continue

                
            