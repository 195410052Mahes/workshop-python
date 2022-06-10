# 5. Struktur Data / Data Structures
---
## 5.1. Selengkapnya tentang Daftar / More on Lists

Tipe data daftar memiliki beberapa metode lagi. Berikut adalah semua metode objek daftar:

list.**append**(x) Tambahkan item ke akhir daftar. Setara dengan ``a[len(a):] = [x]``.

list.**extend**(iterable) Perluas daftar dengan menambahkan semua item dari iterable. Setara dengan ``a[len(a):] = iterable``.

list.**insert**(i, x) Masukkan item pada posisi tertentu. Argumen pertama adalah indeks elemen sebelum dimasukkan, jadi ``a.insert(0, x)`` sisipan di bagian depan daftar, dan ``a.insert(len(a), x)`` setara dengan ``a.append(x)``.

list.**remove**(x) Hapus item pertama dari daftar yang nilainya sama dengan x. Ini menimbulkan ValueError jika tidak ada item seperti itu.

list.**pop**([ i ]) Hapus item pada posisi yang diberikan dalam daftar, dan kembalikan. Jika tidak ada indeks yang ditentukan, ``a.pop()`` menghapus dan mengembalikan item terakhir dalam daftar. (Kurung siku di sekitar i dalam tanda tangan metode menunjukkan bahwa parameternya opsional, bukan berarti Anda harus mengetikkan tanda kurung siku pada posisi itu. Anda akan sering melihat notasi ini di Referensi Pustaka Python.)

list.**clear**() Hapus semua item dari daftar. Setara dengan ``del a[:]``.

list.**index**(x [, start [, end ] ]) Kembalikan indeks berbasis nol dalam daftar item pertama yang nilainya sama dengan x. Menaikkan ValueError jika tidak ada item seperti itu. Argumen opsional mulai dan akhir ditafsirkan seperti dalam notasi irisan dan digunakan untuk membatasi pencarian ke urutan daftar tertentu. Indeks yang dikembalikan dihitung relatif terhadap awal urutan penuh daripada argumen awal.

list.**count**(x) Kembalikan berapa kali x muncul dalam daftar.

list.**sort**(*, key=None, reverse=False) Urutkan item dari daftar di tempat (argumen dapat digunakan untuk penyesuaian pengurutan, lihat diurutkan() untuk penjelasannya).

list.**reverse**() Balikkan elemen daftar di tempatnya.

list.**copy**() Kembalikan salinan daftar yang dangkal. Setara dengan ``a[:]``.

Contoh yang menggunakan sebagian besar metode daftar:
```python
 >>> fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
 >>> fruits.count('apple')
 # output 2 
 >>> fruits.count('tangerine')
 # output 0
 >>> fruits.index('banana')
 # output 3
 >>> fruits.index('banana', 4)  # Temukan pisang berikutnya mulai posisi 4
 # output 6
 >>> fruits.reverse()
 >>> fruits
 # output ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
 >>> fruits.append('grape')
 >>> fruits
 # output ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
 >>> fruits.sort()
 >>> fruits
 # output ['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
 >>> fruits.pop()
 # output 'pear'
 ``` 

Anda mungkin telah memperhatikan bahwa metode seperti ``insert``, ``remove`` atau ``sort``

yang hanya mengubah daftar tidak memiliki nilai pengembalian yang dicetak – mereka mengembalikan default ``None``.

Ini adalah prinsip desain untuk semua struktur data yang dapat diubah dengan Python.

Hal lain yang mungkin Anda perhatikan adalah tidak semua data dapat diurutkan atau dibandingkan. Contohnya, ``[None, 'hello', 10]`` tidak mengurutkan karena bilangan bulat tidak dapat dibandingkan dengan string dan None tidak bisa dibandingkan dengan jenis lainnya. Juga, ada beberapa tipe yang tidak memiliki relasi pengurutan yang ditentukan. Sebagai contoh, ``3+4j < 5+7j`` bukan perbandingan yang valid.

---
## 5.1.1. Menggunakan Daftar sebagai Tumpukan / Using Lists as Queues

Metode daftar membuatnya sangat mudah untuk menggunakan daftar sebagai tumpukan, di mana elemen terakhir yang ditambahkan adalah elemen pertama yang diambil ("masuk terakhir, keluar pertama"). Untuk menambahkan item ke bagian atas tumpukan, gunakan ``append()`` untuk mengambil item dari atas tumpukan, gunakan ``pop()`` tanpa indeks eksplisit. Sebagai contoh:

```python
 >>> stack = [3, 4, 5]
 >>> stack.append(6)
 >>> stack.append(7)
 >>> stack
 # output [3, 4, 5, 6, 7]
 >>> stack.pop()
 # output 7
 >>> stack
 # output [3, 4, 5, 6]
 >>> stack.pop()
 # output 6
 >>> stack.pop()
 # output 5
 >>> stack
 # output [3, 4]
 ```

---
## 5.1.2. Menggunakan Daftar sebagai Antrian /  Using Lists as Queues

Dimungkinkan juga untuk menggunakan daftar sebagai antrian, di mana elemen pertama yang ditambahkan adalah elemen pertama yang diambil ("masuk pertama, keluar pertama"); namun, daftar tidak efisien untuk tujuan ini. Sementara menambahkan dan muncul dari akhir daftar cepat, melakukan sisipan atau muncul dari awal daftar lambat (karena semua elemen lain harus digeser satu).

Untuk mengimplementasikan antrian, gunakan collections.deque yang dirancang untuk menambahkan dan muncul dengan cepat dari kedua ujungnya. Sebagai contoh:

```python
 >>> from collections import deque
 >>> queue = deque(["Eric", "John", "Michael"])
 >>> queue.append("Terry")           # Terry tiba
 >>> queue.append("Graham")          # Graham tiba
 >>> queue.popleft()                 # Yang pertama tiba sekarang pergi
 'Eric'
 >>> queue.popleft()                 # Yang kedua tiba sekarang pergi
 'John'
 >>> queue                           # Antrian yang tersisa sesuai urutan kedatangan
 deque(['Michael', 'Terry', 'Graham'])
 ```

---
## 5.1.3. Pemahaman Daftar / List Comprehensions
Pemahaman daftar menyediakan cara ringkas untuk membuat daftar. Aplikasi umum adalah untuk membuat daftar baru di mana setiap elemen adalah hasil dari beberapa operasi yang diterapkan ke setiap anggota dari urutan lain atau iterable, atau untuk membuat suburutan dari elemen-elemen yang memenuhi kondisi tertentu.

Misalnya, anggap kita ingin membuat daftar kotak, seperti:
```python
 >>> squares = []
 >>> for x in range(10):
 ...     squares.append(x**2)
 ...
 >>> squares
 # output [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
 ```
Perhatikan bahwa ini membuat (atau menimpa) variabel bernama ``x`` yang masih ada setelah loop selesai. Kami dapat menghitung daftar kotak tanpa efek samping menggunakan:
```python
 squares = list(map(lambda x: x**2, range(10)))
 ```
atau, ekuivalen:
```python 
 squares = [x**2 for x in range(10)]
 ```
yang lebih ringkas dan mudah dibaca.

Pemahaman daftar terdiri dari tanda kurung yang berisi ekspresi diikuti oleh ``for`` maka ``nol`` atau lebih ``for`` atau klausa ``if``. Hasilnya akan menjadi daftar baru yang dihasilkan dari evaluasi ekspresi dalam konteks ``for`` dan ``if`` klausa yang mengikutinya. Misalnya, listcomp ini menggabungkan elemen dari dua daftar jika tidak sama:
```python 
 >>> [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
 # output [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
 ```
dan itu setara dengan:
```python
 >>> combs = []
 >>> for x in [1,2,3]:
 ...     for y in [3,1,4]:
 ...         if x != y:
 ...             combs.append((x, y))
 ...
 >>> combs
 # output [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
 ```
Perhatikan bagaimana urutan for dan if pernyataan sama di kedua cuplikan ini. Jika ekspresinya adalah tuple (misal (x, y) dalam contoh sebelumnya), itu harus di dalam kurung.
```python
 >>> vec = [-4, -2, 0, 2, 4]
 >>> # buat daftar baru dengan nilai dua kali lipat
 >>> [x*2 for x in vec]
 # output [-8, -4, 0, 4, 8]
 >>> # filter daftar untuk mengecualikan angka negatif
 >>> [x for x in vec if x >= 0]
 # output [0, 2, 4]
 >>> # menerapkan fungsi untuk semua elemen
 >>> [abs(x) for x in vec]
 # output [4, 2, 0, 2, 4]
 >>> # panggil metode pada setiap elemen
 >>> freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
 >>> [weapon.strip() for weapon in freshfruit]
 # output ['banana', 'loganberry', 'passion fruit']
 >>> # buat daftar 2-tupel seperti (angka, kotak)
 >>> [(x, x**2) for x in range(6)]
 # output [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
 >>> # tupel harus dikurung, jika tidak, kesalahan akan muncul
 >>> [x, x**2 for x in range(6)]
  File "<stdin>", line 1, in <module>
    [x, x**2 for x in range(6)]
               ^
 SyntaxError: invalid syntax
 >>> # meratakan daftar menggunakan listcomp dengan doa 'for'
 >>> vec = [[1,2,3], [4,5,6], [7,8,9]]
 >>> [num for elem in vec for num in elem]
 # output [1, 2, 3, 4, 5, 6, 7, 8, 9]
 ```

Pemahaman daftar dapat berisi ekspresi kompleks dan fungsi bersarang:
```python
 >>> from math import pi
 >>> [str(round(pi, i)) for i in range(1, 6)]
 # output ['3.1', '3.14', '3.142', '3.1416', '3.14159']
 ```

---
## 5.1.4. Pemahaman Nested List /  Nested List Comprehensions

Ekspresi awal dalam pemahaman daftar dapat berupa ekspresi arbitrer, termasuk pemahaman daftar lainnya.

Perhatikan contoh berikut dari matriks 3x4 yang diimplementasikan sebagai daftar 3 daftar panjang 4:
```python 
 >>> matrix = [
 ...     [1, 2, 3, 4],
 ...     [5, 6, 7, 8],
 ...     [9, 10, 11, 12],
 ... ]
 ```

Pemahaman daftar berikut akan mengubah baris dan kolom:
```python
 >>> [[row[i] for row in matrix] for i in range(4)]
 # output [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
 ```

Seperti yang kita lihat di bagian sebelumnya, listcomp bersarang dievaluasi dalam konteks ``for`` yang mengikutinya, jadi contoh ini setara dengan:

```python
 >>> transposed = []
 >>> for i in range(4):
 ...     transposed.append([row[i] for row in matrix])
 ...
 >>> transposed
 # output [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
 ```

yang, pada gilirannya, sama dengan:

```python
 >>> transposed = []
 >>> for i in range(4):
 ...     # 3 baris berikut mengimplementasikan listcomp bersarang
 ...     transposed_row = []
 ...     for row in matrix:
 ...         transposed_row.append(row[i])
 ...     transposed.append(transposed_row)
 ...
 >>> transposed
 # output [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
 ```

Di dunia nyata, Anda harus lebih memilih fungsi bawaan daripada pernyataan aliran yang kompleks. Fungsi ``zip()`` akan melakukan pekerjaan yang baik untuk kasus penggunaan ini:

```python
 >>> list(zip(*matrix))
 # output [(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]
 ```

---

## 5.2. Pernyataan del / The del statement
Ada cara untuk menghapus item dari daftar yang diberikan indeksnya alih-alih nilainya pernyataan ``del``. Ini berbeda dengan metode ``pop`` yang mengembalikan nilai. pernyataan ``del`` juga dapat digunakan untuk menghapus irisan dari daftar atau menghapus seluruh daftar (yang kita lakukan sebelumnya dengan menetapkan daftar kosong ke irisan). Sebagai contoh:

```python
 >>> a = [-1, 1, 66.25, 333, 333, 1234.5]
 >>> del a[0]
 >>> a
 # output [1, 66.25, 333, 333, 1234.5]
 >>> del a[2:4]
 >>> a
 # output [1, 66.25, 1234.5]
 >>> del a[:]
 >>> a
 # output []
 ```

``del`` juga dapat digunakan untuk menghapus seluruh variabel ``del a``

Merujuk nama ``a`` selanjutnya adalah kesalahan (setidaknya sampai nilai lain diberikan padanya). Kami akan menemukan kegunaan lain untuk ``del`` nantinya.

---

## 5.3. Tuple dan Urutan / Tuples and Sequences

Kami melihat bahwa daftar dan string memiliki banyak properti umum, seperti operasi pengindeksan dan pengirisan. Mereka adalah dua contoh tipe data dan urutan. Karena Python adalah bahasa yang berkembang, tipe data urutan lainnya dapat ditambahkan.

Tuple terdiri dari sejumlah nilai yang dipisahkan dengan koma, misalnya:

```python 
 >>> t = 12345, 54321, 'hello!'
 >>> t[0]
 # output 12345
 >>> t
 (12345, 54321, 'hello!')
 >>> # Tuple mungkin bersarang:
 ... u = t, (1, 2, 3, 4, 5)
 >>> u
 # utput ((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))
 >>> # Tuple tidak dapat diubah:
 ... t[0] = 88888
 Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
 TypeError: 'tuple' object does not support item assignment
 >>> # tetapi mereka dapat berisi objek yang bisa berubah:
 ... v = ([1, 2, 3], [3, 2, 1])
 >>> v 
 # output ([1, 2, 3], [3, 2, 1]) 
 ```

Seperti yang Anda lihat, pada tupel keluaran selalu diapit tanda kurung, sehingga tupel bersarang diinterpretasikan dengan benar; mereka mungkin dimasukkan dengan atau tanpa tanda kurung di sekitarnya, meskipun seringkali tanda kurung diperlukan (jika tupel adalah bagian dari ekspresi yang lebih besar). Hal ini tidak mungkin untuk menetapkan ke item individu dari tupel, namun dimungkinkan untuk membuat tupel yang berisi objek yang bisa berubah, seperti daftar.

Meskipun tupel mungkin tampak mirip dengan daftar, mereka sering digunakan dalam situasi yang berbeda dan untuk tujuan yang berbeda. Tuple tidak dapat diubah, dan biasanya berisi urutan elemen heterogen yang diakses melalui pembongkaran (lihat nanti di bagian ini) atau pengindeksan (atau bahkan dengan atribut dalam kasus **namedtuples**). Daftar bisa berubah, dan elemennya biasanya homogen dan diakses dengan mengulangi daftar.

Masalah khusus adalah konstruksi tupel yang berisi 0 atau 1 item: sintaks memiliki beberapa kebiasaan tambahan untuk mengakomodasi ini. Tupel kosong dibangun oleh sepasang tanda kurung kosong; tuple dengan satu item dibangun dengan mengikuti nilai dengan koma (tidak cukup untuk menyertakan satu nilai dalam tanda kurung). Jelek, tapi efektif. Sebagai contoh:

```python
 >>> empty = ()
 >>> singleton = 'hello',    # <-- catatan trailing koma
 >>> len(empty)
 0
 >>> len(singleton)
 1
 >>> singleton
 ('hello',)
 ```

Pernyataan ``t = 12345, 54321, 'hello!'`` adalah contoh pengemasan Tuple: nilainya ``12345``, ``54321`` dan ``'hello!'`` dikemas bersama dalam sebuah tuple. Operasi sebaliknya juga dimungkinkan:

```python
 >>> x, y, z = t 
 ```

Ini disebut, cukup tepat, urutan membongkar dan bekerja untuk setiap urutan di sisi kanan. Pembukaan urutan mensyaratkan bahwa ada banyak variabel di sisi kiri tanda sama dengan jumlah elemen dalam urutan. Perhatikan bahwa beberapa penugasan sebenarnya hanyalah kombinasi dari pengemasan Tuple dan pembongkaran urutan.

---
## 5.4. Set / Sets

Python juga menyertakan tipe data untuk set. Himpunan adalah kumpulan yang tidak berurutan tanpa elemen duplikat. Penggunaan dasar termasuk pengujian keanggotaan dan menghilangkan entri duplikat. Set objek juga mendukung operasi matematika seperti serikat pekerja, persimpangan, perbedaan, dan perbedaan simetris.

kurung kurawal atau ``set()`` fungsi dapat digunakan untuk membuat set. Catatan: untuk membuat set kosong Anda harus menggunakan ``set()`` not ``{}``; yang terakhir membuat kamus kosong, struktur data yang akan kita bahas di bagian selanjutnya.

Berikut adalah demonstrasi singkat:

```python
 >>> basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
 >>> print(basket)                      # tunjukkan bahwa duplikat telah dihapus
 # output {'orange', 'banana', 'pear', 'apple'}
 >>> 'orange' in basket                 # pengujian keanggotaan cepat
 # output True
 >>> 'crabgrass' in basket
 # output False

 >>> # Peragakan operasi himpunan pada huruf unik dari dua kata
 ...
 >>> a = set('abracadabra')
 >>> b = set('alacazam')
 >>> a                                  # huruf unik dalam a
 # output {'a', 'r', 'b', 'c', 'd'}
 >>> a - b                              # huruf di a tapi tidak di b
 # output {'r', 'd', 'b'}
 >>> a | b                              # huruf dalam a atau b atau keduanya
 # output {'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
 >>> a & b                              # huruf a dan b
 # output {'a', 'c'}
 >>> a ^ b                              # huruf a atau b tapi tidak keduanya
 # output {'r', 'd', 'b', 'm', 'z', 'l'}
 ```

Sama halnya dengan pemahaman daftar, pemahaman set juga didukung:

```python
 >>> a = {x for x in 'abracadabra' if x not in 'abc'}
 >>> a
 # output {'r', 'd'}
 ```

---
## 5.5. Kamus / Dictionaries

Tipe data lain yang berguna yang dibangun ke dalam Python adalah kamus. Kamus kadang-kadang ditemukan dalam bahasa lain sebagai "ingatan asosiatif" atau "array asosiatif". Tidak seperti urutan, yang diindeks oleh rentang angka, kamus diindeks oleh kunci, yang dapat berupa jenis apa pun yang tidak dapat diubah; string dan angka selalu bisa menjadi kunci. Tuple dapat digunakan sebagai kunci jika hanya berisi string, angka, atau tupel; jika sebuah tuple berisi objek yang bisa berubah baik secara langsung maupun tidak langsung, itu tidak dapat digunakan sebagai kunci. Anda tidak dapat menggunakan daftar sebagai kunci, karena daftar dapat dimodifikasi di tempat menggunakan penetapan indeks, penetapan irisan, atau metode seperti ``appends()`` dan ``extend()``.

Yang terbaik adalah menganggap kamus sebagai satu set kunci: pasangan nilai, dengan persyaratan bahwa kuncinya unik (dalam satu kamus). Sepasang kurung kurawal membuat kamus kosong: ``{}``. Menempatkan daftar pasangan kunci:nilai yang dipisahkan koma di dalam kurung kurawal menambahkan pasangan kunci:nilai awal ke kamus; ini juga cara kamus ditulis pada output.

Operasi utama pada kamus adalah menyimpan nilai dengan beberapa kunci dan mengekstrak nilai yang diberikan kunci tersebut. Dimungkinkan juga untuk menghapus pasangan kunci:nilai dengan ``del``. Jika Anda menyimpan menggunakan kunci yang sudah digunakan, nilai lama yang terkait dengan kunci tersebut akan terlupakan. Ini adalah kesalahan untuk mengekstrak nilai menggunakan kunci yang tidak ada.

Menampilkan ``list(d)`` pada kamus mengembalikan daftar semua kunci yang digunakan dalam kamus, dalam urutan penyisipan (jika Anda ingin diurutkan, gunakan saja ``sorted(d)`` alih-alih). Untuk memeriksa apakah satu kunci ada dalam kamus, gunakan tombol ``in``.

Berikut adalah contoh kecil menggunakan kamus:
```python
 >>> tel = {'jack': 4098, 'sape': 4139}
 >>> tel['guido'] = 4127
 >>> tel
 # output {'jack': 4098, 'sape': 4139, 'guido': 4127}
 >>> tel['jack']
 # output 4098
 >>> del tel['sape']
 >>> tel['irv'] = 4127
 >>> tel
 # output {'jack': 4098, 'guido': 4127, 'irv': 4127}
 >>> list(tel)
 # output ['jack', 'guido', 'irv']
 >>> sorted(tel)
 # output ['guido', 'irv', 'jack']
 >>> 'guido' in tel
 # output True
 >>> 'jack' not in tel
 # output False
 ```

konstruktor ``dict()`` membangun kamus langsung dari urutan pasangan nilai kunci:
```python
 >>> dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
 # output {'sape': 4139, 'guido': 4127, 'jack': 4098}
 ```

Selain itu, pemahaman dict dapat digunakan untuk membuat kamus dari kunci arbitrer dan ekspresi nilai:
```python
 >>> {x: x**2 for x in (2, 4, 6)}
 # output {2: 4, 4: 16, 6: 36}
 ```

Jika kuncinya adalah string sederhana, terkadang lebih mudah untuk menentukan pasangan menggunakan argumen kata kunci:

```python
 >>> dict(sape=4139, guido=4127, jack=4098)
 # output {'sape': 4139, 'guido': 4127, 'jack': 4098}
 ```

---
## 5.6. Looping Techniques
Saat mengulang kamus, kunci dan nilai yang sesuai dapat diambil secara bersamaan menggunakan metode items().

```python
 >>> knights = {'gallahad': 'the pure', 'robin': 'the brave'}
 >>> for k, v in knights.items():
 ...     print(k, v)
 ...
 # output gallahad the pure
 # output robin the brave
 ```

Saat mengulang melalui urutan, indeks posisi dan nilai yang sesuai dapat diambil pada saat yang sama menggunakan fungsi ``enumerate()``.
```python
 >>> for i, v in enumerate(['tic', 'tac', 'toe']):
 ...     print(i, v)
 ...
 # output
 0 tic
 1 tac
 2 toe
 ```

Untuk mengulang dua atau lebih urutan pada saat yang sama, entri dapat dipasangkan dengan fungsi ``zip().``
```python
 >>> questions = ['name', 'quest', 'favorite color']
 >>> answers = ['lancelot', 'the holy grail', 'blue']
 >>> for q, a in zip(questions, answers):
 ...     print('What is your {0}?  It is {1}.'.format(q, a))
 ...
 # output
 What is your name?  It is lancelot.
 What is your quest?  It is the holy grail.
 What is your favorite color?  It is blue.
 ```

Untuk mengulang urutan secara terbalik, pertama tentukan urutan dalam arah maju dan kemudian panggil fungsi ``reversed()``.
```python
 >>> for i in reversed(range(1, 10, 2)):
 ...     print(i)
 ...
 # output
 9
 7
 5
 3
 1
 ```

Untuk mengulang urutan dalam urutan yang diurutkan, gunakan fungsi ``sorted()`` yang mengembalikan daftar baru yang diurutkan sambil membiarkan sumbernya tidak berubah.

```python
 >>> basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
>>> for i in sorted(basket):
...     print(i)
...
 # output
 apple
 apple
 banana
 orange
 orange
 pear
 ```

Menggunakan ``set()`` pada urutan menghilangkan elemen duplikat. Penggunaan ``sorted()`` dalam kombinasi dengan ``set()`` pada urutan adalah cara idiomatis untuk mengulang elemen unik dari urutan dalam urutan yang diurutkan.

```python
 >>> basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
 >>> for f in sorted(set(basket)):
 ...     print(f)
 ...
 # output
 apple
 banana
 orange
 pear
 ```

Terkadang tergoda untuk mengubah daftar saat Anda mengulangnya; namun, seringkali lebih sederhana dan lebih aman untuk membuat daftar baru.

```python
 >>> import math
 >>> raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
 >>> filtered_data = []
 >>> for value in raw_data:
 ...     if not math.isnan(value):
 ...         filtered_data.append(value)
 ...
 >>> filtered_data
 # output [56.2, 51.7, 55.3, 52.5, 47.8]
 ```

---
## 5.7. Lebih lanjut tentang Ketentuan / More on Conditions

Kondisi yang digunakan dalam pernyataan ``while`` dan ``if`` dapat berisi operator apa saja, bukan hanya perbandingan.

Operator perbandingan ``in`` dan ``not in`` adalah keanggotaan tes yang menentukan apakah suatu nilai ada di (atau tidak) dalam wadah. Operator ``is`` dan ``is not`` membandingkan apakah dua objek benar-benar objek yang sama. Semua operator pembanding memiliki prioritas yang sama, yaitu lebih rendah dari semua operator numerik. Perbandingan dapat dirantai. Sebagai contoh, ``a < b == c`` menguji apakah ``a`` lebih kecil dari ``b`` dan juga ``b`` sama dengan ``c``.

Perbandingan dapat digabungkan menggunakan operator Boolean ``and`` dan ``or``, dan hasil perbandingan (atau ekspresi Boolean lainnya) dapat dinegasikan dengan ``not``. ni memiliki prioritas lebih rendah daripada operator pembanding; diantara mereka, ``not`` memiliki prioritas tertinggi dan ``or``, paling rendah, sehingga ``A and not B or C`` setara dengan ``(A dan (bukan B))`` atau ``C``. Seperti biasa, tanda kurung dapat digunakan untuk menyatakan komposisi yang diinginkan.

The Boolean operators ``and`` dan ``or`` disebut operator hubung singkat: argumen mereka dievaluasi dari kiri ke kanan, dan evaluasi berhenti segera setelah hasilnya ditentukan. Misalnya, jika ``A`` dan ``C`` benar tetapi ``B`` salah, ``A`` dan ``B`` dan ``C`` tidak mengevaluasi ekspresi C. Ketika digunakan sebagai nilai umum dan bukan sebagai Boolean, nilai kembalian dari operator hubung singkat adalah argumen terakhir yang dievaluasi. dimungkinkan untuk menetapkan hasil perbandingan atau ekspresi Boolean lainnya ke variabel. Sebagai contoh,

```python
 >>> string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
 >>> non_null = string1 or string2 or string3
 >>> non_null
 # output 'Trondheim'
 ```

Perhatikan bahwa dalam Python, tidak seperti C, penugasan di dalam ekspresi harus dilakukan secara eksplisit dengan operator walrus :=. Ini menghindari kelas umum masalah yang dihadapi dalam program C: mengetik = dalam ekspresi ketika == dimaksudkan.

---
## 5.8. Membandingkan Urutan dan Jenis Lainnya / Comparing Sequences and Other Types

Objek urutan biasanya dapat dibandingkan dengan objek lain dengan jenis urutan yang sama. perbandingannya menggunakan urutan leksikografis: pertama dua item pertama dibandingkan, dan jika berbeda, ini menentukan hasil perbandingan; jika mereka sama, dua item berikutnya dibandingkan, dan seterusnya, sampai salah satu urutan habis. Jika dua item yang akan dibandingkan itu sendiri merupakan urutan dari jenis yang sama, perbandingan leksikografis dilakukan secara rekursif. Jika semua item dari dua urutan membandingkan sama, urutan dianggap sama. Jika satu barisan merupakan sub-urutan awal dari yang lain, barisan yang lebih pendek adalah yang lebih kecil (lebih kecil). Urutan leksikografis untuk string menggunakan nomor titik kode Unicode untuk mengurutkan karakter individual. Beberapa contoh perbandingan antara urutan dari jenis yang sama:

```python
 (1, 2, 3)              < (1, 2, 4)
 [1, 2, 3]              < [1, 2, 4]
 'ABC' < 'C' < 'Pascal' < 'Python'
 (1, 2, 3, 4)           < (1, 2, 4)
 (1, 2)                 < (1, 2, -1)
 (1, 2, 3)             == (1.0, 2.0, 3.0)
 (1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4)
 ```

Perhatikan bahwa membandingkan objek dari jenis yang berbeda dengan ``<`` atau ``>`` adalah sah asalkan objek tersebut memiliki metode perbandingan yang sesuai. Misalnya, tipe numerik campuran dibandingkan menurut nilai numeriknya, jadi 0 sama dengan 0,0, dll. Jika tidak, alih-alih memberikan urutan arbitrer, penerjemah akan menaikkan penegecualian ``TypeError()``.

**Footnotes**
Bahasa lain dapat mengembalikan objek bermutasi, yang memungkinkan rantai metode, seperti ``d->insert("a")->remove("b")->sort();``.