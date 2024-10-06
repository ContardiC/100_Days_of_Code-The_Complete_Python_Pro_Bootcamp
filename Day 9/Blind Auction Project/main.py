from art import logo
print(logo)
bids={}
max_bid=0
# TODO-4: Compare bids in dictionary
def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {bidder} with a bid of ${highest_bid}")

continue_bidding=True
while continue_bidding:
    # TODO-1: Ask the user for input
    name = input("What is your name?: ")
    price= int(input("What's your bid?: $"))
    # TODO-2: Save data into dictionary {name: price}
    bids[name]=price
    # TODO-3: Whether if new bids need to be added
    should_continue=input("Are there any other bidders? Type 'yes' or 'no'\n").lower()
    if should_continue == 'no':
        continue_bidding=False
        find_highest_bidder(bidding_dictionary=bids)
    elif should_continue == "yes":
        print("\n" * 20)



