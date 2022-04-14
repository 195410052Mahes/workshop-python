ef divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")

divide(2, 1)
# result is 2.0 (Output)
# executing finally clause (Output)
divide(2, 0)
# division by zero! (Output)
# executing finally clause (Output)
divide("2", "1")
# executing finally clause (Output)

# Output:
"""

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in divide
TypeError: unsupported operand type(s) for /: 'str' and 'str'

"""