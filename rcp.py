"""
===================
Rock Scissors Paper
===================

======== ======== =======
computer   user   outcome
======== ======== =======
Rock     Rock     Draw
Rock     Scissors Lose
Rock     Paper    Win
Scissors Rock     Win
Scissors Scissors Draw
Scissors Paper    Lose
Paper    Rock     Lose
Paper    Scissors Win
Paper    Paper    Draw
======== ======== =======
"""
import random

def main():
	n = 10
	
	while (n >0):
		you = input("rock? scissors? paper? : ")
		you = you.lower()
		
		# set computer's fingers
		computer = random.randint(1,3)
		if (computer == 1):
			computer = "rock"
		elif (computer == 2):
			computer = "scissors"
		else:
			computer = "paper"

		# play game
		if (you == computer):
			print("Draw")
		elif (you == "rock"):
			if (computer == "scissors"):
				print("Win")
			else:
				print("Lose")
		elif (you == "scissors"):
			if (computer == "rock"):
				print("Lose")
			else:
				print("Win")
		else:
			if (computer == "rock"):
				print("Win")
			else:
				print("Lose")
		n -= 1

main()
