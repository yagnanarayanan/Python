# choose your own adventure
name = input("Enter your name: ")
print(f"Hi {name}! Start your adventure.")
answer = input("Choose movie or biking")
if answer.lower() == "movie":
    book_ticket = input("Do you want ot book a movie ticket (yes/no):").lower()
    if book_ticket == "yes":
        movie = input("Choose movie A or B").lower()
        if movie == "a":
            print("Tickets are full!")
        elif movie == "b":
            print("Booking available seat")
            print("Seat booked!")
        else:
            print("invalid input")
    elif book_ticket == "no":
        print("Stay home and read a good book!")
    else:
        print("invalid input")
elif answer.lower() == "biking":
    location = input("Where do you want ot bike to (A or B)?")
    if location.lower() == 'a':
        print("The weather is pleasant. Enjoy the ride!")
    elif location.lower() == 'b':
        print("The weather is stormy. Be safe at home!")
    else:
        print("Try again with valid input")
else:
    print("Try again with valid input")
