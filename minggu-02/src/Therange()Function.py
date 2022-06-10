# 4.3. The range() Function

for i in range(5):
    print(i)

print("")

list1=list(range(5, 10))

list2=list(range(0, 10, 3))

list3=list(range(-10, -100, -30))
print(list1)
print(list2)
print(list3)

print("")

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

print("")

print(range(10))

print("")

print(sum(range(4))) # 0 + 1 + 2 + 3