f.read()
# 'This is the entire file.\n' (Output)

f.read()
# '' (Output)

f.readline()
# 'This is the first line of the file.\n' (Output)

f.readline()
# 'Second line of the file\n' (Output)

f.readline()
# '' (Output)

for line in f:
    print(line, end='')
# Ini adalah baris pertama dari file.
# Baris kedua dari file

f.write('This is a test\n')
# 15 (Output)

value = ('the answer', 42)
s = str(value)  # convert the tuple to string
f.write(s)
# 18

f = open('workfile', 'rb+')
f.write(b'0123456789abcdef')
# 16 (Output)

f.seek(5) # Pergi ke byte ke-6 dalam file
# 5 (Output)

f.read(1)
# b'5' (Output)

f.seek(-3, 2) # Pergi ke byte ke-3 sebelum akhir
# 13 (Output)

f.read(1)
# b'd' (Output)