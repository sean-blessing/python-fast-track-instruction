# 1. read the presidents file into a dictionary
#    - key: prez_number, value: tuple of remaining fields
presidents_dictionary = {}

with open("./scripts/files/presidents.txt") as presidents_in:
    print(f'presidents_in: {presidents_in}')
    for line in presidents_in:
        prez_nbr, last_name, first_name, dob, dod, birth_city, birth_state, term_start, term_end, party = line.rstrip('\n\r').split(":")
        presidents_dictionary[prez_nbr] = first_name, last_name, dob, dod, birth_city, birth_state, term_start, term_end, party

# 2. print out list of presidents': first_name, last_name, state_of_birth
#    - sort by last_name, then first_name

def by_last_first(item):
    return item[1], item[0]
#(x[0], x[1])
# sort using function
# for item in sorted(presidents_dictionary.values(), key=by_last_first):
#     print(f'{item[0]} {item[1]}, {item[5]}')

# sort using lambda
for item in sorted(presidents_dictionary.values(), key=lambda e: (e[1], e[0])):
    print(f'{item[0]} {item[1]}, {item[5]}')
