#p. 112 - Dictionaries

# List of states
states_list = ["IN", "OH", "KY", "FL"]
#print(states_list)
# what is a state object? It has Abbreviation, Name
# key value pairs make sense here
# dictionaries are created w/ curly braces
# dictionaries are changeable / mutable
# entries are separated by commas
# entries are defined w/ single quotes 'key': 'value'
# states = {
#     'IN': 'Indiana',
#     'OH': 'Ohio',
#     'KY': 'Kentucky',
#     'FL': 'Florida'
# }
# print(f'State dictionary: {states}')

# Dictionaries store elements of key - value pairs
# Create a dictionary of states (abbrev, state name ie. OH, Ohio)

states = {
    'AL': 'Alabama',
    'AK': 'Alaska',
    'AZ': 'Arizona',
    'AR': 'Arkansas',
    'CA': 'California',
    'CO': 'Colorado',
    'CT': 'Connecticut',
    'DE': 'Delaware',
    'FL': 'Florida',
    'GA': 'Georgia',
    'HI': 'Hawaii',
    'ID': 'Idaho',
    'IL': 'Illinois',
    'IN': 'Indiana',
    'IA': 'Iowa',
    'KS': 'Kansas',
    'KY': 'Kentucky',
    'LA': 'Louisiana',
    'ME': 'Maine',
    'MD': 'Maryland',
    'MA': 'Massachusetts',
    'MI': 'Michigan',
    'MN': 'Minnesota',
    'MS': 'Mississippi',
    'MO': 'Missouri',
    'MT': 'Montana',
    'NE': 'Nebraska',
    'NV': 'Nevada',
    'NH': 'New Hampshire',
    'NJ': 'New Jersey',
    'NM': 'New Mexico',
    'NY': 'New York',
    'NC': 'North Carolina',
    'ND': 'North Dakota',
    'OH': 'Ohio',
    'OK': 'Oklahoma',
    'OR': 'Oregon',
    'PA': 'Pennsylvania',
    'RI': 'Rhode Island',
    'SC': 'South Carolina',
    'SD': 'South Dakota',
    'TN': 'Tennessee',
    'TX': 'Texas',
    'UT': 'Utah',
    'VT': 'Vermont',
    'VA': 'Virginia',
    'WA': 'Washington',
    'WV': 'West Virginia',
    'WI': 'Wisconsin',
    'WY': 'Wyoming'
}
#print(states)

# what state is AK?
#print(states.get("OH"))

# prompt user for abbreviation and look up the name
# choice = ""
# while choice != 'x':
#     choice = input("Enter state abbreviation to find: ")
#     answer = states.get(choice)
#     print(f"State is {answer}")
    
    
# new dictionary of colors
colors = {'R':'Red', 'B':'Blue', 'O': 'Orange', 'G':'Green'}

# # get something out of dictionary
print(f"B is {colors.get('B')}")
print(f"R is {colors['R']}")

# # add something to the dict
colors['P'] = 'Purple'
colors['Y'] = 'Yellow'
print(f"colors: {colors}")

# # replace an item
colors['P'] = 'Plant'
print(f"colors: {colors}")

# # remove items from dict
# color_deleted = colors.pop('P')
# print(f"colors: {colors}")
color_deleted = colors.popitem()
print(f"color_deleted: {color_deleted}")

# p. 119 iterate over the dictionary
# .items(), .keys(), .values()
print(f"color items: {colors.items()}")
print(f"color keys: {colors.keys()}")
print(f"color values: {colors.values()}")

# # Check to see if key or value exists
print(f"Does color key Z exist? {'Z' in colors}")
print(f"Does color key B exist? {'B' in colors}")
print(f"Does color value Blue exist? {'Blue' in colors.values()}")

# # p. 120 iterable of key value pairs
for key, value in colors.items():
    print(f"abv: {key}, color: {value}")
print("=== sorted items ====")
for abv, color in sorted(colors.items()):
    print(f"abv: {abv}, color: {color}")
    
# # p. 121 read into dict of tuples

from pprint import pprint

knight_info = {}  # create empty dict

with open("./scripts/files/knights.txt") as knights_in:
    for line in knights_in:
        name, title, color, quest, comment = line.rstrip('\n\r').split(":")
        knight_info[name] = title, color, quest, comment  # create new dict element with name as key and a tuple of the other fields as the value
#print(f"print: {knight_info}")
pprint(knight_info)
print()

for name, info in knight_info.items():
    print(info[0], name)

print()
print(knight_info['Robin'][2])

# # p. 128 Sets
# number_set_1 = {1,2,3,4,5,6,7,8,9,10}
# number_set_2 = {6,7,8,9,10,11,12,13,14,15}
# print(f"=== comparing sets ===")
# print(f"set1: {number_set_1}")
# print(f"set2: {number_set_2}")

# print("\nUnion, Intersection, Diff, Symmetric Difference")
# # Union ( | ): unique combination of both sets
# print(f"Union ( | ): {number_set_1 | number_set_2}")
# # Intersection ( & ): common items
# print(f"Intersection ( & ): {number_set_1 & number_set_2}")
# # Difference ( - ): items unique to left set
# print(f"Difference ( - ): {number_set_1 - number_set_2}")
# # Symmetric Difference / XOR ( ^ ): non-common items
# print(f"Symmetric Difference ( ^ ): {number_set_1 ^ number_set_2}")


print("bye")