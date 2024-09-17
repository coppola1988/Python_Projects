from os import system
from auction_Art import logo
from bid_function import bid_function

print(logo)

more_bidders = True
auction_list = {}


while more_bidders:
    name = input("What is your Name?: ")
    bid = int(input("What is your Bid? : $"))
    person = input("Are there any other Bidder? ")
    auction_list[name] = bid

    bid_function(auction_list)

    if person == "yes":
        more_bidders = True
        system('cls')
    elif person == "no":
        more_bidders = False
