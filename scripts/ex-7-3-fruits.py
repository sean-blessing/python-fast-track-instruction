with open("./scripts/files/fruit.txt") as fruit_in:
    fruit_lines = fruit_in.read().splitlines()


print(f'{fruit_lines}')