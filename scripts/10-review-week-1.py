# when do i use a list vs a tuple?
# From Google Search:
# - Lists:
#   + Are mutable: This means you can change their content (add, remove, or modify elements) after creation.
#   + Created with: square brackets [], entries separated by commas
# - Tuples:
#   + Are immutable: This means once you create a tuple, you cannot change its content.
#   + Created with: parenthesis (), entries separated by commas

# Create a tuple to store elements that won't change
month_numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
seven_dwarfs = ("Sneezy", "Sleepy", "Dopey", "Doc", "Bashful", "Grumpy", "Happy")

# Create a list to store elements that could change
even_numbers = [0, 2, 4, 10]
print(even_numbers)
even_numbers.append(6)
even_numbers.append(7)
even_numbers.append(8)
print(even_numbers)
even_numbers.remove(7)
print(even_numbers)
even_numbers.sort()
print(even_numbers)

# try to change a tuple
# seven_dwarfs.append("new dwarf") - illegal - can't do that
# seven_dwarfs.remove("Dopey") - also illegal

# try to sort a tuple
# seven_dwarfs.sort() - illegal, sorting also changes the tuple
# what can you do with a tuple?
print(seven_dwarfs.count("Dopey"))
print(len(seven_dwarfs))
print(seven_dwarfs.index("Dopey"))

# when to use a for loop?
# while True:, for-i-in-range, for-x-of
# loop through seven_dwarfs and print each to console
print(seven_dwarfs)
# wouldn't use while True: because how do you know when to end?
# for-i-in-range? Doesn't know there's 7, doesn't know when to start/stop
# let's try it
for i in range(len(seven_dwarfs)):
    print(seven_dwarfs[i])

print()
# for-x-in is better here
for d in seven_dwarfs:
    print(d)

print("-------------------")
#when would we need an indexed for loop to print dwarf names?
#if we needed to know the order in the tuple
for idx in range(0, len(seven_dwarfs)):
    print(f'{idx} {seven_dwarfs[idx]}')

print("--- while statements ---")
# prompt user for a color (red, green, blue) - validate correct color entered
while True:
    color = input("Enter a color (red, green, or blue): ").lower()
    if color == "red":
        print("RED")
        break
    elif color == "blue":
        print("BLUE")
        break
    elif color == "green":
        print("GREEN")
        break
    else:
        print("invalid selection")
        continue
    
    