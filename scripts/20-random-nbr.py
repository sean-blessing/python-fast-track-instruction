# generate a random number
#import random
from random import random, randrange

# 0.0 <= nbr < 1.0
#random_nbr = random.random()
random_nbr = random()
print(f'random_nbr = {random_nbr}')

# generate a die roll (whole number between 1 and 6)
#die_roll = random.random(1,6)
die_roll = randrange(1,7)
print(f'die_roll = {die_roll}')

print("\nNumber Guessing. I'm thinking of a number between 1 and 20!")
random_nbr = randrange(1, 21)
print(f"Cheat: my number is {random_nbr}")
guess = int(input("What's your guess? "))
if (guess > random_nbr):
    print("Too high!")
elif guess < random_nbr:
    print("Too low!")
else:
    print("You guessed it!")
