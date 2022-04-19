try:
    open('database.sqlite')
except OSError:
    raise RuntimeError from None

# (Output)
"""
 Traceback (most recent call last): (Output)
  File "<stdin>", line 4, in <module> (Output)
 RuntimeError (Output)
"""