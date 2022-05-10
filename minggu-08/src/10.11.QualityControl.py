def average(values):
    """Menghitung rata-rata aritmatika dari daftar angka.

    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)

import doctest
doctest.testmod()   # secara otomatis memvalidasi tes yang disematkan