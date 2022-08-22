import art
import random
import game_data
from replit import clear

def choice_gen_A(data) :
  """Fn to find the random choice A to compare against B"""
  #Find the length of the data list
  total_length = len(data) - 1
  
  #To find random options for comparison
  option_A = random.randint(0, total_length)

  return option_A
  
  
def choice_gen_B(data) :
  """Fn to find the random choice B to compare against A"""
  total_length = len(data) - 1
  option_B = random.randint(0, total_length)
  return option_B

#To check whether both options A & B are same
def fn_check(A, B, data) :
  """To check whether both options A & B are same. If yes, change it to be different from one another"""
  total_length = len(data) - 1
  while(A == B) :
    B = random.randint(0, total_length)
  return B

def won_or_lost(option, opt_A, opt_B, data) :
  """To check whether we won or not"""
  if option == "A" :
    follower_user = data[opt_A]['follower_count']
    follower_other = data[opt_B]['follower_count']
  else :
    follower_user = data[opt_B]['follower_count']
    follower_other = data[opt_A]['follower_count']

  print(f"User = {follower_user}, other = {follower_other}")

  if follower_user > follower_other :
    return True
  else :
    return False

  

correct_ans = True
score = 0
option_A = choice_gen_A(game_data.data)

while correct_ans :
  clear()
  #Print the logo
  print(art.logo)
  option_B = choice_gen_B(game_data.data)
  fn_check(option_A, option_B, game_data.data)
  print(f"Compare A : {game_data.data[option_A]['name']}, {game_data.data[option_A]['description']}, {game_data.data[option_A]['country']}")
  print(art.vs)
  print(f"Against B : {game_data.data[option_B]['name']}, {game_data.data[option_B]['description']}, {game_data.data[option_B]['country']}")
  
  your_option = input("Who has more followers, Type A or B : ")
  
  
  if won_or_lost(your_option, option_A, option_B, game_data.data) :
    score += 1
    option_A = option_B
    print("You won")
  else :
    print(f"Sorry, that's wrong. Final score : {score}")
    correct_ans = False
