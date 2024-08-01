# p. 174
# list of tuples, each tuple is one computer person
# each computer person tuple has the following attributes:
# - index 0: first name
# - index 1: last name
# - index 2: company
# - index 3: birth date

computer_people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

# how do we sort these?
print(f'computer people unsorted: ')
for cp in computer_people:
    print(cp)

# print always includes a new line
# print("hello")
# print("there")
# print("how")
# print("are you?")

print('computer people 1 sorted - by first index position[0]:')
cp_sorted_1 = sorted(computer_people)
for cp in cp_sorted_1:
    print(cp)

print('\ncomputer people 1 sorted again by first name, another way:')
for first_name, last_name, organization, dob in sorted(computer_people):
    print(first_name, last_name, organization, dob)
# string multiplier...
print('-' * 60)

# sort by last name
print('\ncomputer people sorted by last name, element [1]:')
for first_name, last_name, organization, dob in sorted(computer_people, key=lambda e: e[1]):  # Select element of nested tuple for sorting
    print(first_name, last_name, organization, dob)
print('-' * 60)

# sort by company
print('\ncomputer people sorted by company, element [2]:')
for first_name, last_name, organization, dob in sorted(computer_people, key=lambda e: e[2]): # Select different element of nested tuple for sorting
    print(first_name, last_name, organization, dob)
print('-' * 60)
    
    
# how would we do a secondary sort (like company, then lastname)?
# see final example in this script

# p. 176 sorting dictionaries
colors = dict(red=5, scarlet=18, blue=1, pink=0, grey=27, yellow=5, green=18)
#colors = {'red': 5, 'scarlet': 18... } # the other way to create dictionary
print(f'colors dictionary unsorted: {colors}')
print('-' * 60)

colors_sorted_1 = sorted(colors)
print(f'colors dictionary sorted: {colors_sorted_1}')
print('-' * 60)

# sort by key
print(f'colors dictionary sort using items(), default is key: ')
for color, num in sorted(colors.items()):  # No sort key function needed to sort by key
    print(color, num)
print('-' * 60)

# sort by value
print(f'colors dictionary sort using items(), sort by value: ')
def by_value(item):
    return item[1], item[0] # sort first by value, then by key

for color, num in sorted(colors.items(), key=by_value):
    print(color, num)
print('-' * 60)
# how would we do a secondary sort on computer people (like company, then lastname)?
def by_comp_ln(item):
    return item[2], item[1] # sort first by company [2], then lastname [1]

for first_name, last_name, organization, dob in sorted(computer_people, key=by_comp_ln):
    print(first_name, last_name, organization, dob)