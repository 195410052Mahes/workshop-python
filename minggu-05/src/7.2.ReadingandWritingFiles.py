f = open('workfile', 'w')

 with open('workfile') as f:
   read_data = f.read()

# Kami dapat memeriksa apakah file telah ditutup secara otomatis.
f.closed
# True (Output)

f.close()
f.read()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: I/O operation on closed file.