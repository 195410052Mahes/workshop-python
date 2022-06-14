import math
print(f'The value of pi is approximately {math.pi:.3f}.')
# The value of pi is approximately 3.142 (Output)

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')
# Sjoerd     ==>       4127 (Output)
# Jack       ==>       4098 (Output)
# Dcab       ==>       7678 (Output)

animals = 'eels'
print(f'My hovercraft is full of {animals}.')
# My hovercraft is full of eels. (Output)
print(f'My hovercraft is full of {animals!r}.')
# My hovercraft is full of 'eels'. (Output)