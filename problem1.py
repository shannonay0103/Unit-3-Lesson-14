import time
import random

print('*'* 80)
print('Rock, Paper, Scissors Game')

my_choice = input('Choice your weapon: Rock, Paper, or Scissors?')
choices = ['Rock','Paper', 'Scissors']

time.sleep(1)
print('Rock')
print()

time.sleep(1)
print('Paper')
print()

time.sleep(1)
print('Scissors')
print()

time.sleep(1)
print('Shoot!')
print()

computer_choice = random.randint(1,3)

if computer_choice == 1:
	computer_choice='Rock'
	time.sleep(1)
	print('Rock')

elif computer_choice == 2:
	computer_choice='Paper'
	time.sleep(1)
	print('Paper')

elif computer_choice == 3:
	computer_choice='Scissors'
	time.sleep(1)
	print('Scissors')

if my_choice == "Rock" and computer_choice == "Scissors":
	print('You Win!')

elif my_choice == "Paper" and computer_choice == "Rock":
	print('You Win!')

elif my_choice == "Scissors" and computer_choice == "Paper":
	print('You Win!')

elif my_choice == "Scissors" and computer_choice == "Scissors":
	print('Tied!')

elif my_choice == "Paper" and computer_choice == "Paper":
	print('Tied!')

elif my_choice == "Rock" and computer_choice == "Rock":
	print('Tied!')

elif computer_choice == "Rock" and my_choice == "Scissors":
	print('You Lose!')

elif computer_choice == "Paper" and my_choice == "Rock":
	print('You Lose!')

else:
	print('You Lose!')

