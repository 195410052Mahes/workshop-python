# 3.2. First Steps Towards Programming

# Fibonacci series:
# the sum of two elements defines the next

a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b
print("")

i = 256*256
print('The value of i is', i)
print("")

a, b = 0, 1
while a < 1000:
    print(a, end=',')
    a, b = b, a+b
print("")