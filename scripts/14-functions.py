# p. 133 Functions


# variable args
def add(*nbrs):
    sum = 0
    for n in nbrs:
        sum += n
        # sum = sum + n
    return sum

def subtract(nbr1, nbr2):
    return nbr1 - nbr2

def get_whole_number(prompt):
    return int(input(prompt))

# calculator - add and subtract
print("=== add ===")
# number_1 = get_whole_number("Enter first number: ")
# number_2 = get_whole_number("Enter second number: ")
# sum = add(number_1, number_2)
# print(f'Sum: {sum}')
print(f"Add 2, 3: {add(2,3)}")
print(f"Add 2, 3, 5: {add(2,3,5)}")
print(f"Add bunch of nums: {add(2,3,5,45,2,7,2,8,9,100,235,43)}")

#print("=== subtract ====")
# number_1 = get_whole_number("Enter number 1: ")
# number_2 = get_whole_number("Enter number 2: ")
# diff = subtract(number_1,number_2)
# print(f'Diff: {diff}')

# keyword arguments
# print hello
# giving name a default value
def hello(name = 'George'):
    print(f'hello {name}')
    
hello()
hello("World")

def calc_line_total(price, quantity, shipping_fee):
    return price * quantity + shipping_fee

print("---- line totals ----")
print(calc_line_total(shipping_fee=4.99, price=35, quantity=2))