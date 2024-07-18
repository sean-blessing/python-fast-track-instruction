# sorting lists
# p. 62 

names = ["Sean", "Danielle", "Ron", "jenny"]
print(names)
# upper vs lower case resolution in sort
names.sort(key=str.lower)
print(names)

numbers = [6,89,23,54,11,9,0]
print(numbers)
numbers.sort(reverse=True)
print(numbers)