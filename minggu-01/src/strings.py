# 3.1.2. Strings

print ('spam eggs')  # single quotes
print ('doesn\'t') # use \' to escape the single quote...
print ("doesn't")  # ...or use double quotes instead
print ('"Yes," they said.')
print ("\"Yes,\" they said.")
print ('"Isn\'t," they said.')
print("")

s = 'First line.\nSecond line.'  # \n means newline
#s  # without print(), \n is included in the output 'First line.\nSecond line.'
print(s)  # with print(), \n produces a new line
print("")

print('C:\some\name') # here \n means newline!
print("")
print(r'C:\some\name')  # note the r before the quote
print("")

# 3 times 'un', followed by 'ium'
hasil1=3 * 'un' + 'ium'
print(hasil1)
print("")

print('Py' 'thon')
print("")

word = 'Python'
word[0]
print(word[0]) # character in position 0
print(word[5])  # character in position 5
print(word[-1])  # last character
print(word[-2])  # second-last character
print(word[-6]) 
print("")

print(word[0:2])  # characters from position 0 (included) to 2 (excluded)
print(word[2:5])  # characters from position 2 (included) to 5 (excluded)

print("")
print(word[:2])   # character from the beginning to position 2 (excluded)
print(word[4:])   # characters from position 4 (included) to the end
print(word[-2:])  # characters from the second-last (included) to the end
print("")

print(word[:2] + word[2:])
print(word[:4] + word[4:])
print("")

print(word[4:42])
print(word[42:])
print("")

print('J' + word[1:])
print(word[:2] + 'py')
print("")