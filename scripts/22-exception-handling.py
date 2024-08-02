# p. 183
print("welcome to exception handling\n")
# code that causes an error - wrap this in a try block (p. 184)

while True:
    try:
        whole_number = int(input("Enter a whole number: "))
        print(f'You entered {whole_number}')
        break
    except ValueError as err:
        print("Error: not a whole number. Please try again.")
        #print(err)

print("Bye")