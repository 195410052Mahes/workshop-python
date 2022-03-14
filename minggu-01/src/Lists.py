# 3.1.3. Lists 
squares = [1, 4, 9, 16, 25]
print(squares)
print(squares[0])  # indexing returns the item
print(squares[-1]) 
print(squares[-3:]) # slicing returns a new list
print(squares[:])
print(squares + [36, 49, 64, 81, 100])
print("")

cubes = [1, 8, 27, 65, 125]  # something's wrong here  # the cube of 4 is 64, not 65!
print(cubes)
cubes[3] = 64
print(cubes)
print("")

cubes.append(216)  # add the cube of 6
cubes.append(7 ** 3)  # and the cube of 7
print(cubes)
print("")

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)
print("")
# replace some values
letters[2:5] = ['C', 'D', 'E']
print(letters)
print("")
# now remove them
letters[2:5] = []
print(letters)
print("")
# clear the list by replacing all the elements with an empty list
letters[:] = []
print(letters)
print("")

letters = ['a', 'b', 'c', 'd']
print(len(letters))
print("")

a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)
print(x[0])
print(x[0][1])