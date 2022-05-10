import zlib
s = b'witch which has which witches wrist watch'
len(s)
# 41 (Output)
t = zlib.compress(s)
len(t)
# 37 (Output)
zlib.decompress(t)
# b'witch which has which witches wrist watch' (Output)
zlib.crc32(s)
# 226805979 (Output)