fruits = [
    '    MANGO', 'Apple', '   peach   ', 'PLUM   ', '  Apricot',
    'BaNaNa', 'Persimmon   '
]

# list comprehension to clean the fruits:
# - lower case, trim leading/trailing white space

# regular for loop - no list comprehension:
# cleaned_fruits = []
# for fruit in fruits:
#     clean_fruit = fruit.lower().strip()
#     cleaned_fruits.append(clean_fruit)
# use list comprehension

cleaned_fruits = [f.lower().strip() for f in fruits]
print(cleaned_fruits)