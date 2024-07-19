# import os
# # from w3 schools - using os
# path = os.path.realpath(__file__) 
# print(path) 

# p. 97 - Chapter 4
# p. 101 - Reading a text file
# read the our-class.txt file and print to console

# read entire file into one string
with open('./scripts/files/our-class.txt') as file_in:
    contents = file_in.read()
print(contents)

print("\n===== read file line by line =====")
with open('./scripts/files/our-class.txt') as file_in:
    for raw_line in file_in:
        #print(f"raw_line: {raw_line}")
        # strip will remove extra new line character
        line = raw_line.strip()
        print(f"line: {line}")
        
# p. 102
# read entire file into list of lines (without new lines)
with open('./scripts/files/our-class.txt') as file_in:
    people_in_class = file_in.read().splitlines()

for person in people_in_class:
    print(f"Person: {person}")
    
# p. 107
# create a file named us-states.txt and write 5 states to it
# Ohio, Pennsylvania, Michigan, Iowa, Illinois

states_list = ["Ohio", "Pennsylvania", "Michigan", "Iowa", "Illinois"]

with open("./scripts/files/state.txt", "w") as states_out:
    for state in states_list:
        states_out.write(state + "\n")
        
        
        
#CSV
# import csv

# with open('file.csv', newline='') as f:
#     reader = csv.reader(f)
#     data = list(reader)

# print(data)
        
print("bye")