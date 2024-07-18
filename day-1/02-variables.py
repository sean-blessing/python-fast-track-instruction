# This is a Python comment

a = 5
first_name = 'Bob'
last_name = "Marley"

# another_last_name = "O'Malley"
another_last_name = 'O\'Malley'

print(a)
print(first_name)
print(last_name)
print(another_last_name)

# a gets reassigned a different type
a = "Fred"

# x is a string
x = "8"

# y is a number
y = 5

# Python doesn't know how to combine str and num
#z = x + y

x = 8
z = x + y
print(z)

# another example, converting the type
c = "9"
d = 2

#print(int(c) + d)
print(c + str(d))

#print("Name = " + first_name + " " + last_name)
# another way to print, using formatted strings
print(f"Name = {first_name} {last_name}")

# a string split across lines
sentence = "This is a sentence \nsplit across two lines"
print(sentence)
print("Sometimes\twe\tneed\ttabs")

name_2 = """James Earl "Jimmy" Carter"""
print(name_2)
warning_str = """
Warning
Danger
Driver operating on closed course"""
print(warning_str)

# spanish example from unicode.py
print("\u00a1\u0048\u006f\u006c\u0061\u0020\u004d\u0075\u006e\u0064\u006f\u0021") # spanish
print("\u00a1Hola Mundo!")
print("copyright character \u00a9")
print('26\u00b0')

# p. 30 String operators and methods
print(first_name.upper())
print(first_name)

# from strings.py
a = "My hovercraft is full of EELS"

print("original:", a)
print("upper:", a.upper())
print("lower:", a.lower())
print("swapcase:", a.swapcase()) # Swap upper and lower case
print("title:", a.title())  # All words are capitalized

# p. 25 numbers
x = 5
y = 7.35
z = 75

print(x + y)
print(int(y / x))
print(y % x)

x = 1
x = x + 1
# can do += in Python
x += 1
print(x)
# can't do ++ in Python
#x++

# p. 30 writing to the screen
print("hello", 5)
print("hello",5, sep="-")

# p. 34 formatting strings
float_val = 57.3456789
# format 2 decimal places
print(f"float_val w/ two decimal places: {float_val:.2f}")

# p. 39 keyboard input
# calculator app
# prompt for two numbers, then multiply them
# num_1 = int(input("Enter a whole number: "))
# num_2 = int(input("Enter another whole number: "))
# print(num_1 * num_2)

#exercise
celsius_str = input("Enter celsius: ")
celsius = float(celsius_str)
fahrenheit = ((9 * celsius) / 5) + 32
print("Fahrenheit = "+str(fahrenheit))
print(f"Fahrenheit = {fahrenheit:.1f}")