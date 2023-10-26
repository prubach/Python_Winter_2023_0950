for i in range(0, 5):
    print(f'i={i}')

print('---------')

for i in reversed(range(-3, 10, 2)):
    print(f'i={i}')

print('---------')
i = 0
while i < 8:
    i += 1
    if i == 2:
        continue
    if i == 6:
        break
    print(f'i={i}')
    #i = i + 1


