import weakref, gc
class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = A(10)                   # buat referensi
d = weakref.WeakValueDictionary()
d['primary'] = a            # tidak membuat referensi
d['primary']                # ambil objek jika masih hidup
# 10 (Output)
del a                       # hapus satu referensi
gc.collect()                # jalankan pengumpulan sampah segera
# 0 (Output)
d['primary']                # entri dihapus secara otomatis
# (Output)
"""
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    d['primary']                # entri dihapus secara otomatis
  File "C:/python310/lib/weakref.py", line 46, in __getitem__
    o = self.data[key]()
KeyError: 'primary'
"""