from random import randrange

MIN_VAL = 1
MAX_VAL = 20

print("Welcome to the guess the number game!")
print("="*37)
print()

# the game starts
choice = "y"

while choice.lower() == "y":
    print(f"I'm thinking of a number between {MIN_VAL} and {MAX_VAL}. try to guess it.")
    the_number = randrange(MIN_VAL,MAX_VAL+1)
    print(f"Cheat: # is {the_number}\n")

    while True:
        try:
            guess = int(input("Guess the number: "))
            if (guess < MIN_VAL):
                print(f"Invalid entry. Must be greater than or equal to {MIN_VAL}")
                continue
            elif (guess > MAX_VAL):
                print(f"Invalid entry. Must be less than or equal to {MAX_VAL}")
                continue
        except ValueError:
            print(f"Invalid entry. Try again.")
            continue
        if (guess > the_number):
            print("Too high!")
        elif guess < the_number:
            print("Too low!")
        else:
            print("You guessed it!")
            break
    choice = input("Continue (y/n)? ")
    
print("Bye. Thanks for playing!")