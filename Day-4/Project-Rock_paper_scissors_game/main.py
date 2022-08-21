import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

# for_rock = 0
# for_paper = 1
# for_scissor = 2

images = [rock, paper, scissors]

player_choice = int(input("Please provide your choice -> \n 0 for Rock \n 1 for paper \n 2 for scissors \n"))
if player_choice >= 3 or player_choice < 0 :
  print("Enter a valid number. You lose!!!")
else :
  print("Your choice : ")
  print(images[player_choice])
  
  ai_input = random.randint(0,2)
  print("AI's choice : ")
  print(images[ai_input])


  if player_choice == 0 and ai_input == 2 :
    print("You Won!!!")
  elif ai_input == 0 and player_choice == 2 :
    print("You lose :(")
  elif ai_input > player_choice :
    print("You Lose:(")
  elif player_choice > ai_input :
    print("You won!!!")
  else :
    print("It's draw")
