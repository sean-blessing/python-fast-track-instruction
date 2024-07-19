# p. 60
fruits = ['apple', 'cherry', 'orange', 'kiwi', 'banana', 'pear', 'fig']
print(fruits)

whole_numbers = [1, 7, 3, 23, 45, 101, 2]
print(whole_numbers)

float_numbers = [76.8, 56.2, 77.0]
print(float_numbers)

numbers = [1, 5.5, 2, 8.3]
print(numbers)

things = ["a", 5, 8.4, "hello"]
print(things)

print(f"3rd element in whole_numbers = {whole_numbers[3]}")
#print(f"7th element in whole_numbers = {whole_numbers[7]}")
print(f"-1th element in whole_numbers = {whole_numbers[-1]}")

whole_numbers[3] = 100
print(whole_numbers)

# p. 61 - lists
even_numbers = [2, 4, 6, 8, 10]
print(f"even_numbers array = {even_numbers}")

print(f"index position 3 = {even_numbers[3]}")

for n in range (0, 5):
    print(f"n is {n}")

# iterate through even_numbers using a for loop
for n in range(0,5):
    print(f"n: {n}, even_number: {even_numbers[n]}")

#even_numbers[5] = 12
even_numbers.append(12)
print(f"even_numbers array = {even_numbers}")
even_numbers.insert(3,11)
print(f"even_numbers array = {even_numbers}")
even_numbers.pop(3)
print(f"even_numbers array = {even_numbers}")
even_numbers.pop()
print(f"even_numbers array = {even_numbers}")

print("\n======= fruits list - slicing ------")
print(fruits)
print(f"list's slice!")
print(f"[2:] {fruits[2:]}")
print(f"[2:5] {fruits[2:5]}")
print(f"[:5] {fruits[:5]}")
print(f"[-2] {fruits[-2]}")
print(f"[:-2] {fruits[:-2]}")
print(f"[-5:-2] {fruits[-5:-2]}")
print(f"[0::2] {fruits[0::2]}")
print(f"[1::2] {fruits[1::2]}")
print(f"[::2] {fruits[::2]}")

# p. 70 iterating over list using for loop
print("\n--------- fruits")
print(fruits)
for n in range(0,len(fruits)):
    print(f"fruit({n}): {fruits[n]}")
print("easier way to loop...")
for f in fruits:
    print(f"fruit: {f}")

print("========== iterate over string =============")
name = "Bob Marley"
for c in name:
    print(c)
for c in name:
    print(c,end='')

print()
# p. 73 tuples
birth_date = (1955, 4, 21)
print(birth_date)

# final examples before exercises
# raising to a power
print(f"2 to the 5th power: {2**5}")

# iterate through a list and multiply each element by 2
print(f"even numbers: {even_numbers}")
for n in even_numbers:
    print(n*2, end=', ')

print()
# loop through years 2000 through 2050, display every 5 years
for n in range(2000, 2051, 5):
    print(n)
    
# when to use range in a for loop, or not??
names = ["Danielle", "Ron", "Sean"]

# this is easier!
for name in names:
    print(f"name is {name}")
    
# print even years from 2000 to 2024
for year in range(2000,2025,2):
    print(f"year: {year}")
    
# print the names with the order in the list
# (in addition to the value, we want to print the index position)
for n in range(0, len(names)):
    #name_length = len(names[n])
    #print(f"name: {names[n]}, length: {name_length}")
    print(f"{n}: name is {names[n]}")