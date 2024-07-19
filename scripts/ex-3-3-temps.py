ctemps = [-40, 0, 37, 75, 100]

# loop through ctemps, and display the ctemp and fahrenheit conversion
for c in ctemps:
    f = ((9 * c) / 5) + 32
    print(f"c: {c}, f: {f}")