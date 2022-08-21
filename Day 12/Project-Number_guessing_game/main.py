#Number Guessing Game Objectives:
import art
import random
# Include an ASCII art logo.
print(art.logo)

#Welcome message
print("Welcome to the number guessing game")
print("I am thinking of a number between 1 to 100")

#Creating the numbers list and adding values to it
numbers = []
for n in range(1,101) :
  numbers.append(n)

answer = random.choice(numbers)
#print(f"Psst. The answer is {answer}")

#Asking the level of the game
level = input("What level do you wanna play\n 1. Easy\n 2. Hard\n Enter your choice : ").lower()

#Providing chances according to the levels
chance = 0
if level == "easy" :
  chance = 10
else :
  chance = 5

# Allow the player to submit a guess for a number between 1 and 100.
while chance :
  guess = int(input("Enter your guessed number : "))
  
  # Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
  if guess == answer :
    print(f"Hurray. The number you guessed {guess} & the answer {answer} are same. Kudos. You won")
    chance = 0
  elif guess > answer :
    print(f"{guess} is too high. Try again")
    chance -= 1
    print(f"You have {chance} turns remaining")
  else :
    print(f"{guess} is too low. Try again")
    chance -= 1
    print(f"You have {chance} turns remaining")

# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
if guess != answer :
  print("You have run out of guesses, You lost")
