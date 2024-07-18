print("Welcome to the number guessing game!\n")
print("You will pick a whole number, between 1 and 100,000, and the computer will try to guess it.")
print("Once guessed, the total number of guesses will be displayed.\n")

# initialize variables
min_val = 0
max_val = 100001
guess_count = 0
count = 0

the_number = int(input("What's the number to guess? "))
print("You picked the number "+str(the_number)+".")

# while loop
while True:
    guess = (max_val + min_val)//2
    count+=1
    answer = input(f"I'm guessing {guess}. (L)ow, (H)igh, or (Y) for correct? ").lower()
    if answer == "l":
        min_val = guess
    elif answer == "h":
        max_val = guess
    elif answer == "y":
        print(f"The computer guessed the number ({the_number}) in {count} guesses.")
        break
    else:
        print("Invalid selection. Start over")
        break

print("Bye. Thanks for playing!")
    
    