# p. 128 Sets
number_set_1 = {1,2,3,4,5,6,7,8,9,10}
number_set_2 = {6,7,8,9,10,11,12,13,14,15}
print(f"=== comparing sets ===")
print(f"set1: {number_set_1}")
print(f"set2: {number_set_2}")

print("\nUnion, Intersection, Diff, Symmetric Difference")
# Union ( | ): unique combination of both sets
print(f"Union ( | ): {number_set_1 | number_set_2}")
# Intersection ( & ): common items
print(f"Intersection ( & ): {number_set_1 & number_set_2}")
# Difference ( - ): items unique to left set
print(f"Difference ( - ): {number_set_1 - number_set_2}")
print(f"Difference ( - ): {number_set_2 - number_set_1}")
# Symmetric Difference / XOR ( ^ ): non-common items
print(f"Symmetric Difference ( ^ ): {number_set_1 ^ number_set_2}")