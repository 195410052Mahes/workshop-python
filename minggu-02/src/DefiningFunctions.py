# 4.7. Defining Functions

def fib(n):    # tulis deret fibonacci hingga n
    """Cetak deret Fibonacci hingga n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

# Sekarang panggil fungsi yang baru saja kita definisikan:
fib(2000)

print("")

print(fib)

f = fib
print(f(100))

print("")

fib(0)
print(fib(0))

print("")

def fib2(n):  # return Fibonacci series up to n
    """Kembalikan daftar yang berisi deret Fibonacci hingga n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)    
        a, b = b, a+b
    return result    # kembalikan deret Fibonacci hingga n
    
f100 = fib2(100)    # sebut saja
print(f100)         # tulis hasilnya

# 4.8. More on Defining Functions
# 4.8.1. Default Argument Values
i = 5

def f(arg=i):
    print(arg)

i = 6
f()

print("")

def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

print("")

#4.8.2. Keyword Arguments
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")
print("")

#4.8.5. Unpacking Argument Lists
print(list(range(3, 6))) # panggilan normal dengan argumen terpisah
args = [3, 6]
print(list(range(*args))) # panggilan dengan argumen yang dibongkar dari daftar

print("")

#4.8.6. Lambda Expressions
def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)
f(0)
f(1)
print("")

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
print(pairs)
print("")

#4.8.7. Documentation Strings
def my_function():
    """Do nothing, but document it.

    No, really, it doesn't do anything.
    """
    pass

print(my_function.__doc__)
print("")

#4.8.8. Function Annotations
def f(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs

f('spam')