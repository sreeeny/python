#Basic Python Snippet to calculate total price for ticket purchases Done as part of TTH - Python Basics by Craig Dennis (minus exception handling)

TICKET_PRICE = 10.0
SERVICE_FEE = 2.0

tickets_remaining = 100

def total_sum(num_of_tickets):
    return int((num_of_tickets * TICKET_PRICE) + SERVICE_FEE)

print("Welcome to Master Ticket Purchase site! We have {} tickets remaining! Act fast, if you want one!".format(tickets_remaining))
user_name = raw_input("While you're here, how may we address you? ")
user_tickets = int(input("Hi {}, How many tickets would you like to buy today? ".format(user_name)))
if(user_tickets <  tickets_remaining):
    total_price = total_sum(user_tickets)
    user_confirm = raw_input("Hi {}, you're about to purchase {} tickets for the show. It will cost you $ {}. Do you like to confirm this order? Please Y to confirm, N to cancel ".format(user_name,user_tickets,total_price))
    user_confirm = user_confirm.lower()
    if (user_confirm == 'y'):
        tickets_remaining -= user_tickets;
        print("Purchase Successful! We have {} tickets left!".format(tickets_remaining))
    else:
        print("Thanks for visiting the site! Please do consider buying tickets next time!")
    print("Thank you & Good day!")
else:
    print ("Sorry, we have only {} tickets remaining.".format(tickets_remaining))
