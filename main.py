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

### Code for RPS game here
import random
import rps

player_choice = input('What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors\n')
computer_choice = random.randint(0,2)
player_choice = int(player_choice)
if player_choice >2 or player_choice <0:
  print('You chose an invalid number: you lose!')
else:
  print('\n')
  rps.rps_print(player_choice,rock,paper,scissors)
  print('\n')
  print('Computer chose: \n')
  rps.rps_print(computer_choice,rock,paper,scissors)

  if player_choice == computer_choice:
    print('It\'s a draw!')
  elif (player_choice == 0 and computer_choice == 1) or (player_choice == 1 and computer_choice == 2) or (player_choice == 2 and computer_choice == 0):
    print('You lose')
  else:
    print('You win!')






    