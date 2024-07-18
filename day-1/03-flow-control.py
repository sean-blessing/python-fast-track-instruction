# p. 44
# Traffic Light Example
# Light Color: Red, Yellow, Green
#light_color = input("What color is the traffic light? ").lower()

# inspect light_color and tell user what to do
# if light_color is:
# - red - stop
# - yellow - slow down
# - green - go
# - any other color - bad color
# if light_color == "red":
#     print("stop")
# elif light_color == "yellow":
#     print("slow down")
# elif light_color == "green":
#     print("go")
# else:
#     print("invalid color")

# print("\nTemperature comfort check...")
# current_temp = int(input("What's the temp? "))

# > 75 Hot
# 60 <= 75 Comfortable
# 52 <= 60 Cool
# <= 52 Cold

# if current_temp > 75:
#     print("HOT!!!")
# elif current_temp > 60:
#     print("Comfortable")
# elif current_temp > 52:
#     print("Cool")
# else:
#     print("Freezing dude!!!")

# p. 53 - while loop
# menu option
# menu options would be: List movies, Add movie, Quit

menu_options = """Menu Options:
- List
- Add
- Quit
Select Option: 
"""

# # default choice to anything other than "quit"
# choice = ""
# while choice != "quit":
#     choice = input(menu_options).lower()
#     if choice == "list":
#         print("List movies")
#     elif choice == "add":
#         print("Add a movie")
#     elif choice == "quit":
#         print("Quit")
#     else:
#         print("Invalid option")

# p. 54 loop control


# while True:
#     print("in while loop...")
#     n = int(input("enter a number: "))
#     if n > 20:
#         print("greater than 20.")
#         continue
#     elif n == 20:
#         print("20")
#         break
#     else:
#         print("less than 20.")
#         continue

# for loop
# for loop executes a certain number of times
# print all even numbers between 1 and 100
for i in range(0,101,10):
    print(f"number: {i}")

# Exercise 2-1 - celsius to fahrenheit converter - repeat
# same as last version, but repeat until user enters 'q'
# If use simply hits enter w/ no entry, continue


while True:
    celsius_str = input("Enter temp in celsius: ")
    # check celsius_str: if empty - continue, if q - quit
    if celsius_str == '':
        print("Entry is required. Try again.")
        continue
    elif celsius_str == 'q':
        break
    celsius = int(celsius_str)
    fahrenheit = ((9 * celsius) / 5) + 32
    print("Fahrenheit = "+str(fahrenheit))
print("Bye")