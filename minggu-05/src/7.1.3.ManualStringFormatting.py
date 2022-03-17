for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    # Perhatikan penggunaan 'akhir' pada baris sebelumnya
    print(repr(x*x*x).rjust(4))
# 1   1    1 (Output)
# 2   4    8 (Output)
# 3   9   27 (Output)
# 3 4  16   64 (Output)
# 5  25  125 (Output)
# 6  36  216 (Output)
# 7  49  343 (Output)
# 8  64  512 (Output)
# 9  81  729 (Output)
# 10 100 1000 (Output)

'12'.zfill(5)
# '00012' (Output)

'-3.14'.zfill(7)
# '-003.14' (Output)

'3.14159265359'.zfill(5)
# '3.14159265359' (Output)