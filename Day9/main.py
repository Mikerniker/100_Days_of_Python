from replit import clear
from art import logo

print(logo)

print("Welcome to the secret auction program.")

keep_bidding = True
total_bids = {}


def all_bidders():
  highest_bidder = max(total_bids, key=total_bids.get)
  all_bids = total_bids.values()
  max_bid = max(all_bids)
  print(f"The winner is {highest_bidder} with a bid of {max_bid}")
  

while keep_bidding:
  bidder = input("What is your name?: ").title()
  bid_amount = int(input("What's your bid?: $"))
  total_bids[bidder] = bid_amount
  other_bids = input("Are there any other bidders? Type 'yes' or 'no'.\n" ).lower()
  if other_bids == "no":
    keep_bidding = False
    clear()
    all_bidders()
  else:
    clear()
  
print(total_bids)


 

 
 




