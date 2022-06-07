# 5.1.3. List Comprehensions
vec = [-4, -2, 0, 2, 4]
# create a new list with the values doubled
print([x*2 for x in vec])
# filter the list to exclude negative numbers
print([x for x in vec if x >= 0])
# apply a function to all the elements
print([abs(x) for x in vec])
# call a method on each element
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
print([weapon.strip() for weapon in freshfruit])
# create a list of 2-tuples like (number, square)
print([(x, x**2) for x in range(6)])
# flatten a list using a listcomp with two 'for'
vec = [[1,2,3], [4,5,6], [7,8,9]]
print([num for elem in vec for num in elem])