import random
from sys import exit
from decimal import Decimal, getcontext

print("Welcome to the Decimals Game!")

print("Choose your operation:")
print("1 - Multiplication")
print("2 - Addition")
print("3 - Subtraction")
print("4 - Division")

# ask for input for the operation
operation = int(input("Operation:"))

print("Choose a level:")
print("1 - Easy")
print("2 - Difficult")
# ask for level
level = int(input("Level: "))

precision = 2
limit = 10
# the difficult level; increased precision (how many decimal places)
if level == 2:
	precision = 6
	limit = 100

# The number of questions we've asked so far
count = 0

# ask 5 questions (a while loop)
while count < 5:

	# increase the question count or else we have a forever loop
	count = count + 1

	# we're using the decimal library and getcontext controls the precision
	getcontext().prec = precision

	# generate random numbers
	n1 = Decimal(random.randint(1, limit))
	d1 = Decimal(random.randint(1, limit))
	first = n1 / d1

	n2 = Decimal(random.randint(1, limit))
	d2 = Decimal(random.randint(1, limit))
	second = n2 / d2

	# calculations should be done with higher precision
	# or else our answers are rounded up and dont match
	# the user input, even when it is right.
	getcontext().prec = 20

	# if the user chooses multiplication
	if operation == 1:
		print(f"Calculate {first} x {second}")
		correct = first * second
	# if the user chooses addition
	if operation == 2:
		print(f"Calculate {first} + {second}")
		correct = first + second
	# if the user chooses subtraction
	if operation == 3:
		print(f"Calculate {first} - {second}")
		correct = first - second
	# if the user chooses division
	if operation == 4:
		print(f"Calculate {first} / {second}")
		correct = first / second
# if the user gets the question right or wrong
	given = Decimal(input("Your answer: "))
	if given == correct:
		print(f"{given} is the correct answer! ")
	else:
		print(f"You're wrong. The correct answer is {correct}. ")
		print("Game Over!")
		exit()

print("You Win! You're good at this!")

