# build a list based on a range
# build a list of even numbers, from 0 to 20
# hard-coded
# even_numbers = [0,2,4,6,8,10,12,14,16,18,20]
# print(even_numbers)

# for num in range(0,101,2):
#     print(num)
# use list comprehension to build the list from 0 to 20
even_numbers = [num for num in range(0,101,2)]
print(even_numbers)
# boss says that list needs to go to 100!

# Danielle asks - can we create a list dynamically 
# without list comprehension?
# odd numbers, 1 to 101
odd_numbers = []
for i in range(1, 102, 2):
    odd_numbers.append(i)
print(f"odd #s: {odd_numbers}")

# list comprehension, multiply #s in a list, generating new list
numbers = [1,2,3,4,5]
# new list, x10
numbers_times_ten = [nbr * 10 for nbr in numbers]
print(f"numbers: {numbers}, numbers_times_ten: {numbers_times_ten}")
