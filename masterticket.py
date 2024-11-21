from pprint import PrettyPrinter

TICKET_PRICE = 10

tickets_remaining = 100

#Run this code continuously until all the tickets are out
while tickets_remaining >= 1:
#output how many tickets are remaining using the tickets_remaining variable

    print(f"There are {tickets_remaining} tickets remaining")
#
#
# #Gather the user's name and assign it to a new variable
#
    name = input("What is your name? ")
    print(f"Hello {name}")

#prompt the user by name and ask how many tickets they would like

#calculate the price (number of tickets multiplied by the price ) and assign it to a variable

#output the price to the screen

    no_of_tickets = input("how many tickets would you like, {}? ".format(name))

#price_of_tickets = input("What is the price of the ticket? ")

    total_price = TICKET_PRICE * int(no_of_tickets)

    print(f"Total price is {total_price}")

#prompt user if they want to proceed, Y/N

# if they want to proceed
    #print out to the screen "SOLD!" to confirm purchase

    #and then decreement the tickets remaining by the number of tickets purchased

    # Otherwise.....
    # Thank them by name

    purchase_next = input("Do you want to purchase another ticket? Y/N")
    if purchase_next.lower() == "y":
        print("SOLD!")

        tickets_remaining -=int( no_of_tickets)
    else:
        print(f"Thank you for purchasing!, {name}")


#print(f"There are {tickets_remaining} tickets remaining")

#Notify user that the tickets are sold out
print("Sorry the tickets are sold out")




