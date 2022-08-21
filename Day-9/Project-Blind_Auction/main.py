from replit import clear
#HINT: You can call clear() to clear the output in the console.

#Create an empty dictionary
blind_auction = {}

#This variable helps to add more bidders
repeat = True

#Blind auction logo
import art
print(art.logo)

#Welcome msg
print("Welcome to online blind auction website")
#Fn for calculating the highest bid
def highest_bid(blind_auction) :

  #variable to store the highest temp variable
  temp = 0
  for bidder in blind_auction :
    bid_amt = blind_auction[bidder]
    if bid_amt > temp :
      temp = bid_amt
      winner = bidder
  print(f"The winner of this bid is{winner} with amount {temp}")

while repeat :
  
  #Getting the bidder name & bid value from user
  name = input("The name of the bidder is : ")
  bid = int(input("The bid amount is : $ "))
  
  #Inserting the user inputted values to blind_auction dict as name as a key and bid as value
  blind_auction[name] = bid

  #For clearing the screen
  clear()
  
  #Ask if any other bidders are available
  other_bidder = input("Are any other bidders there ? Type yes or no : ").lower()
  if other_bidder == "no" :
    repeat = False

    #Function call for the bid result
    highest_bid(blind_auction)
