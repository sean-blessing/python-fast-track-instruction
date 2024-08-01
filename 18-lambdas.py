fruits = ["pomegranate", "cherry", "apricot", "date", "Apple", "lemon", "Kiwi",
 "ORANGE", "lime", "Watermelon", "guava", "papaya", "FIG", "pear", "banana",
 "Tamarind", "persimmon", "elderberry", "peach", "BLUEberry", "lychee",
 "grape"]
print(f'fruits unsorted: {fruits}')
# fruits.sort() # sorts the list 'in place'
sorted_fruits = sorted(fruits, key=str.lower)
print(f'fruits sorted: {sorted_fruits}')

nums = [800, 80, 1000, 32, 255, 400, 5, 5000]

fs1 = sorted(fruits, key=lambda e: e.lower()) # each element to lowercase
print(f"Ignoring case: {fs1}")
# print(' '.join(fs1))
# print()

fs2 = sorted(fruits, key=lambda e: (len(e), e.lower())) # lambda returns tuple
print(f"By length, then name: {fs2}")
# print(' '.join(fs2))
# print()

fs3= sorted(nums)
print(f"Numbers sorted numerically: {fs3}")
# for n in fs3:
#     print(n, end=' ')  # prints horizontally, rather than vertically
# print()
# print()