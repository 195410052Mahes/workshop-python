# 8. Kesalahan dan Pengecualian / Errors and Exceptions
di modul ke 8 ini terdapat dua jenis kesalahan yang dapat dibedakan, yaitu kesalahan sintaksis dan pengecualian.

---

## 8.1. Kesalahan Sintaks / Syntax Errors
Kesalahan sintaks juga dikenal sebagai kesalahan penguraian, contoh:
```python
 >>> while True print('Hello world')
 # (Output)
 """
  File "<stdin>", line 1
    while True print('Hello world')
                   ^
 SyntaxError: invalid syntax
 """
 ```

**Penjelasan**:

dalam contoh, kesalahan terdeteksi pada fungsi print(), karena titik dua ``(':')`` hilang sebelumnya. Nama file dan nomor baris dicetak sehingga dapat diketahui di mana letak mencarinya jika input berasal dari skrip.

---

## 8.2. Pengecualian / Exceptions
suatu pernyataan atau ekspresi secara sintaksis benar, hal itu dapat menyebabkan kesalahan ketika dilakukan upaya untuk mengeksekusinya.

Kesalahan yang terdeteksi selama eksekusi disebut pengecualian dan tidak fatal tanpa syarat jika mempelajari cara menanganinya dalam program Python. 

Namun, sebagian besar pengecualian tidak ditangani oleh program, dan menghasilkan pesan kesalahan seperti yang ditunjukkan di sini, contoh:

```python
 >>> 10 * (1/0)
 # (Output)
 """
 Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
 ZeroDivisionError: division by zero
 """

 >>> 4 + spam*3
 # (Output)
 """
 Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
 NameError: name 'spam' is not defined
 """

 >>> '2' + 2
 # (Output)
 """
 Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
 TypeError: can only concatenate str (not "int") to str
 """
 ```

**Penjelasan**:

Baris terakhir dari pesan kesalahan menunjukkan apa yang terjadi. Pengecualian datang dalam tipe yang berbeda, dan tipe tersebut dicetak sebagai bagian dari pesan tipe dalam contoh adalah *ZeroDivisionError*, *NameError* dan *TypeError*.

String yang dicetak sebagai tipe pengecualian adalah nama pengecualian bawaan yang terjadi. Karena ini berlaku untuk semua pengecualian bawaan, tetapi tidak harus benar untuk pengecualian yang ditentukan pengguna walaupun ini adalah konvensi yang berguna.

Nama pengecualian standar sebagai pengidentifikasi bawaan bukan sebagai kata kunci yang dicadangkan dan Sisa baris memberikan detail berdasarkan jenis pengecualian dan apa yang menyebabkannya.

Bagian pesan kesalahan sebelumnya menunjukkan konteks di mana pengecualian terjadi dalam bentuk pelacakan balik tumpukan, karena secara umum ini berisi baris sumber daftar traceback stack. Namun, itu tidak akan menampilkan baris yang dibaca dari input standar.

---

## 8.3. Menangani Pengecualian / Handling Exceptions
Menangani pengecualian memungkinkan untuk menulis program yang menangani pengecualian yang dipilih. Contoh berikut meminta pengguna untuk memasukkan hingga bilangan bulat yang valid telah dimasukkan, tetapi memungkinkan pengguna untuk menginterupsi program (menggunakan Control-C atau apa pun yang didukung sistem operasi). Perhatikan bahwa interupsi yang dibuat pengguna ditandai dengan menaikkan pengecualian *KeyboardInterrupt*. Contoh:

```python
 >>> while True:
 ...   try:
 ...       x = int(input("Please enter a number: "))
 ...       break
 ...   except ValueError:
 ...       print("Oops!  That was no valid number.  Try again...")
 ...
 ```

Pernyataan ``try`` berfungsi sebagai berikut:
* Pertama, klausa ``try`` (sebagai pernyataan antara kata kunci ``try`` dan ``except``) dieksekusi.
* Jika tidak ada pengecualian yang terjadi, maka klausa ``except`` akan dilewati dan eksekusi pernyataan ``try`` selesai.
* Jika pengecualian terjadi selama eksekusi klausa ``try``, maka sisa klausa akan dilewati. Jika tipenya cocok dengan pengecualian yang dinamai kata kunci ``except``, klausa ``except`` dijalankan, dan kemudian eksekusi dilanjutkan setelah blok ``try`` atau ``except``.
* Jika terjadi pengecualian yang tidak cocok dengan pengecualian yang disebutkan dalam klausa ``except``, maka akan diteruskan ke pernyataan percobaan luar, jika tidak ada penangan yang ditemukan, itu merupakan pengecualian yang tidak tertangani dan eksekusi berhenti dengan pesan seperti yang ditunjukkan di atas.

Pernyataan ``try`` mungkin memiliki lebih dari satu klausa ``except`` guna untuk menentukan penangan untuk pengecualian yang berbeda. Paling banyak satu handler akan dieksekusi. 

Handler hanya menangani pengecualian yang terjadi di klausa ``try`` yang sesuai, bukan di handler lain dari pernyataan ``try`` yang sama. Klausa pengecualian dapat menyebutkan beberapa pengecualian sebagai tupel dalam kurung, misalnya:

```python
 ... except (RuntimeError, TypeError, NameError):
 ...     pass
 ```

**Penjelasan**:

Kelas dalam klausa ``except`` kompatibel dengan pengecualian jika itu adalah kelas yang sama atau kelas dasar. Sebagai contoh kode berikut akan mencetak B, C, D dalam urutan tersebut:

```python
 class B(Exception):
    pass

 class C(B):
    pass

 class D(C):
    pass

 for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")
 ```

**Penjelasan**:

Perhatikan bahwa jika klausa ``except`` dibalik dengan kecuali B pertama, maka akan dicetak B, B, B — pencocokan pertama klausa ``except`` akan dipicu.

Semua pengecualian mewarisi dari ``BaseException``, sehingga dapat digunakan sebagai karakter pengganti. Gunakan ini dengan sangat hati-hati, karena mudah untuk menutupi kesalahan pemrograman yang sebenarnya dengan cara ini. Hal tersebut juga dapat digunakan untuk mencetak pesan kesalahan dan kemudian menaikkan kembali pengecualian. contoh:

```python
 import sys

 try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
 except OSError as err:
    print("OS error: {0}".format(err))
 except ValueError:
    print("Could not convert data to an integer.")
 except BaseException as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise
 ```

**Penjelasan**:

klausa pengecualian terakhir dapat menghilangkan nama pengecualian, namun nilai pengecualian kemudian harus diambil dari ``sys.exc_info()[1]``.

Pernyataan ``try`` dan ``except`` memiliki klausa ``else`` opsional, yang jika ada harus mengikuti semua klausa ``except``. Berguna untuk kode yang harus dijalankan jika klausa ``try`` tidak memunculkan eksepsi. Sebagai contoh:

```python
 for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()
 ```

**Penjelasan**:

Penggunaan klausa ``else`` lebih baik daripada menambahkan kode tambahan ke klausa ``try`` karena menghindari secara tidak sengaja dengan  menangkap pengecualian yang tidak dimunculkan oleh kode yang dilindungi oleh pernyataan ``try`` dan ``except``.

Ketika pengecualian terjadi, hal tersebut mungkin memiliki nilai terkait dan juga dikenal sebagai argumen pengecualian. Kehadiran dan tipe argumen bergantung pada tipe pengecualian.

Klausa ``except`` dapat menentukan variabel setelah nama pengecualian. Variabel terikat ke instance pengecualian dengan argumen yang disimpan di ``instance.args``. Untuk kenyamanan, instance pengecualian mendefinisikan ``__str__()`` sehingga argumen dapat dicetak secara langsung tanpa harus merujuk ke ``.args``. User juga dapat membuat instance pengecualian terlebih dahulu sebelum menaikkannya dan menambahkan atribut apa pun ke dalamnya seperti yang diinginkan. Sebagai contoh:

```python
 >>> def this_fails():
 ...     x = 1/0
 ...
 >>> try:
 ...     this_fails()
 ... except ZeroDivisionError as err:
 ...     print('Handling run-time error:', err)
 ...
 # Handling run-time error: division by zero (Output)
 ```

---

## 8.4. Meningkatkan Pengecualian / Raising Exceptions

Pernyataan ``raise`` memungkinkan programmer untuk memaksa pengecualian tertentu terjadi. Sebagai contoh:

```python
 >>> raise NameError('HiThere')
 # (Output)
 """
 Traceback (most recent call last):
   File "<stdin>", line 1, in <module>
 NameError: HiThere
 """
 ```

**Penjelasan**:

Satu-satunya argumen untuk ``raise`` menunjukkan pengecualian yang akan diajukan. Hal ini harus berupa instance pengecualian atau kelas pengecualian yaitu kelas yang berasal dari pengecualian. Jika kelas pengecualian dilewatkan, maka secara implisit dipakai dengan memanggil konstruktornya tanpa argumen. Sebagai contoh:

```python
 raise ValueError  # singkatan untuk 'raise ValueError()'
 ```

Jika perlu menentukan apakah pengecualian dimunculkan tetapi tidak untuk menanganinya, maka bentuk pernyataan kenaikan yang lebih sederhana memungkinkan untuk menaikkan kembali pengecualian. Sebagai contoh:

```python
 >>> try:
 ...     raise NameError('HiThere')
 ... except NameError:
 ...     print('An exception flew by!')
 ...     raise
 ...
 #(Output)
 """
 An exception flew by!
 Traceback (most recent call last):
   File "<stdin>", line 2, in <module>
 NameError: HiThere
 """
 ```
---
## 8.5. Rantai Pengecualian / Exception Chaining

Pernyataan ``raise`` memungkinkan pilihan yang memungkinkan rantai pengecualian. Sebagai contoh:

```python
 # pengecualian harus berupa instance pengecualian atau Tidak Ada
 raise RuntimeError from exc
 ```

Ini bisa berguna saat mengubah pengecualian. Sebagai contoh:

```python
 >>> def func():
 ...     raise ConnectionError
 ...
 >>> try:
 ...     func()
 ... except ConnectionError as exc:
 ...     raise RuntimeError('Failed to open database') from exc
 ...
 # (Output)
 """
 Traceback (most recent call last):
   File "<stdin>", line 2, in <module>
   File "<stdin>", line 2, in func
 ConnectionError
 """

 # Pengecualian di atas adalah penyebab langsung dari pengecualian berikut:

 # (Output)
 """
 Traceback (most recent call last):
   File "<stdin>", line 4, in <module>
 RuntimeError: Failed to open database
 """
 ```

Rantai pengecualian terjadi secara otomatis ketika pengecualian dinaikkan di dalam bagian ``except`` atau ``finally``. Ini dapat dinonaktifkan dengan menggunakan ```from None```. Contoh:

```python
 >>> try:
 ...   open('database.sqlite')
 ... except OSError:
 ...   raise RuntimeError from None
 ...
 # (Output)
 """
 Traceback (most recent call last):
   File "<stdin>", line 4, in <module>
 RuntimeError
 """
 ```
---

## 8.6. Pengecualian yang Ditentukan Pengguna / User-defined Exceptions

Program dapat memberi nama pengecualian mereka sendiri dengan membuat kelas pengecualian baru. 

Pengecualian biasanya harus diturunkan dari kelas Pengecualian baik secara langsung maupun tidak langsung.

Kelas pengecualian dapat didefinisikan dengan melakukan apa pun yang dapat dilakukan di kelas lain, tetapi biasanya dibuat sederhana. seringkali hanya menawarkan sejumlah atribut yang memungkinkan informasi tentang kesalahan diekstraksi oleh penangan untuk pengecualian.

---
## 8.7. Mendefinisikan Tindakan Pembersihan / Defining Clean-up Actions
Pernyataan ``try`` memiliki klausa opsional lain yang dimaksudkan untuk mendefinisikan tindakan pembersihan yang harus dilakukan dalam semua keadaan. Sebagai contoh:

```python
  >>> try:
 ...     raise KeyboardInterrupt
 ... finally:
 ...     print('Goodbye, world!')
 ...
 # (Output)
 """
 Goodbye, world!
 KeyboardInterrupt
 Traceback (most recent call last):
   File "<stdin>", line 2, in <module>
 """
 ```

Klausa ``finally`` berjalan apakah pernyataan try menghasilkan pengecualian atau tidak. Poin-poin berikut membahas kasus yang lebih kompleks ketika pengecualian terjadi:
* Jika eksepsi terjadi selama eksekusi klausa ``try``, eksepsi tersebut dapat ditangani oleh klausa exception. Jika pengecualian tidak ditangani oleh klausa ``exception``, maka pengecualian dinaikkan kembali setelah klausa akhirnya dieksekusi.
* Pengecualian dapat terjadi selama eksekusi klausa ``except`` atau ``else`` ada.
* Jika klausa ``finally`` mengeksekusi pernyataan ``break``, ``continue``, atau ``return``, eksepsi tidak dimunculkan kembali.
* Jika pernyataan ``try`` mencapai pernyataan ``break``, ``continue``, atau ``return``, maka klausa ``finally`` akan dieksekusi tepat sebelum eksekusi pernyataan ``break``, ``continue``, atau ``return``.
* Jika klausa ``finally`` menyertakan pernyataan ``return``, maka nilai yang dikembalikan akan menjadi nilai dari pernyataan klausa ``return``, bukan nilai dari pernyataan ``return`` klausa ``try``.

Sebagai contoh:
```python
  >>> def bool_return():
 ...     try:
 ...         return True
 ...     finally:
 ...         return False
 ...
  >>> bool_return()
 False # (Output)
 ```
Contoh lainnya:
```python
  >>> def divide(x, y):
 ...     try:
 ...         result = x / y
 ...     except ZeroDivisionError:
 ...         print("division by zero!")
 ...     else:
 ...         print("result is", result)
 ...     finally:
 ...         print("executing finally clause")
 ...
  >>> divide(2, 1)
  # (Output)
  """
  result is 2.0
  executing finally clause
  """

  >>> divide(2, 0)
  # (Output)
  """
  division by zero!
  executing finally clause
  """

  >>> divide("2", "1")
  # (Output)
  """
 executing finally clause
 Traceback (most recent call last):
   File "<stdin>", line 1, in <module>
   File "<stdin>", line 3, in divide
 TypeError: unsupported operand type(s) for /: 'str' and 'str'
 """
 ```

**Penjelasan**:

Klausa ``finally`` dieksekusi dalam program. ``TypeError`` yang dimunculkan dengan membagi dua string tidak ditangani oleh klausa ``except`` dan karena itu dimunculkan kembali setelah klausa ``finally`` dieksekusi.

Dalam aplikasi dunia nyata, klausa last berguna untuk melepaskan sumber daya eksternal, seperti file atau koneksi jaringan.

---

## 8.8. Tindakan Pembersihan yang Sudah Ditentukan / Predefined Clean-up Actions

Beberapa objek menentukan tindakan pembersihan standar yang harus dilakukan ketika objek tidak lagi diperlukan, dan terlepas dari apakah operasi menggunakan objek berhasil atau gagal. Contoh:

```python
 for line in open("myfile.txt"):
    print(line, end="")
 ```

**Penjelasan**:

Masalah pada kode ini adalah membiarkan file terbuka untuk waktu yang tidak ditentukan setelah bagian kode ini telah selesai dieksekusi. 

Ini bukan masalah dalam skrip sederhana, tetapi bisa menjadi masalah untuk aplikasi yang lebih besar. 

Pernyataan ``with`` memungkinkan objek seperti file untuk digunakan dengan cara yang memastikan untuk dibersihkan dengan cepat dan benar. 

```python
 with open("myfile.txt") as f:
    for line in f:
        print(line, end="")
 ```

**Penjelasan**: 

Setelah pernyataan dieksekusi, maka file *f* ditutup, bahkan jika ada masalah saat memproses baris. Objek seperti file menyediakan tindakan pembersihan yang telah ditentukan sebelumnya, dan akan menunjukkan hal ini dalam dokumentasinya.