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
choices = [rock, paper, scissors]


user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors\n"))
if 0 <= user_choice <= 2:
    print(choices[user_choice])
else:
    print("Invalid number. You LOSE!")

computer_choice = random.randint(0, 2)
print("Computer Chose: \n", choices[computer_choice])

if user_choice == 0 and computer_choice == 2:
    print("You WIN!")
elif user_choice == 1 and computer_choice == 0:
    print("You WIN!")
elif user_choice == 2 and computer_choice == 1:
    print("You WIN!")
elif user_choice == computer_choice:
    print("DRAW!")
else:
    print("You LOSE!")
