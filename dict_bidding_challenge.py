from replit import clear
from dict_bidding_challenge_logo import logo
#HINT: You can call clear() to clear the output in the console.

print(logo)

list_of_bidders = {}
bidding_finished = False


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f'The winner is {winner} with a bid of ${highest_bid}')


while not bidding_finished:
    bidder_name = input("what is you bidding name?: ")
    bidder_price = int(input("what is your bidding price?: $"))
    list_of_bidders[bidder_name] = bidder_price
    should_continue = input("Are there any other bidders? Type 'yes or no'.\n")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(list_of_bidders)
    elif should_continue == "yes":
        clear()



# def list_of_bidders(name: "bidder_name", price:"bidder_price"):

