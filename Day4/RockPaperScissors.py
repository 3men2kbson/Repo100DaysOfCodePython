import random

rock = '''
      _______
  ---'   ____)
        (_____)
        (_____)
VK      (____)
  ---.__(___)
'''

paper = '''
      _______
  ---'   ____)____
            ______)
            _______)
VK         _______)
  ---.__________)
'''


scissors = '''
      _______
  ---'   ____)____
            ______)
         __________)
VK      (____)
  ---.__(___)
'''

game_options = [rock, paper, scissors]

you_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")

print(game_options[int(you_choice)])
print("Computer choose:\n")

computer_choice = random.choice(game_options)

print(computer_choice)

if (int(you_choice) == 0 and game_options.index(computer_choice) == 0) or (int(you_choice) == 1 and game_options.index(computer_choice) == 1) or (int(you_choice) == 2 and game_options.index(computer_choice) == 2):
  print("There is a tie")
elif (int(you_choice) == 0 and game_options.index(computer_choice) == 2) or (int(you_choice) == 2 and game_options.index(computer_choice) == 1) or (int(you_choice) == 1 and game_options.index(computer_choice) == 0):
  print("You win!")
else:
  print("You lose!")
  