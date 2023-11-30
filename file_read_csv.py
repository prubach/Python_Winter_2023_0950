my_file = 'users.csv'

with open(my_file, 'r') as f:
    lines = f.readlines()
    i = 0
    for line in lines:
        i += 1
        print(f'{i}: {line}', end='')
        for cell in line.split(';'):
            print(type(cell))
            print(cell)
