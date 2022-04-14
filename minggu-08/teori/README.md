# 10. Tur Singkat Perpustakaan Standar / Brief Tour of the Standard Library 

## 10.1. Sistem Operasi Antarmuka / Operating System Interface

Modul sistem operasi menyediakan lusinan fungsi untuk berinteraksi dengan sistem operasi. Pastikan untuk menggunakan ``import os`` alih-alih ``from os import *``, hal ini akan mencegah ``os.open()`` membayangi fungsi ``open()`` bawaan yang beroperasi jauh berbeda. Contoh:

```python
 >>> import os
 >>> os.getcwd()      # Kembalikan direktori kerja saat ini
 # 'C:\\Python310' (Output)
 >>> os.chdir('/server/accesslogs')   # Ubah direktori kerja saat ini
 >>> os.system('mkdir today')   # Jalankan perintah mkdir di sistem shell
 # 0 (Output)
 ```

Fungsi built-in dir() dan help() berguna sebagai bantuan interaktif untuk bekerja dengan modul besar, misal seperti sistem operasi:

```python
 >>> import os
 >>> dir(os)
 # <mengembalikan daftar semua fungsi modul> (Output)
 >>> help(os)
 # <mengembalikan halaman manual ekstensif yang dibuat dari docstrings modul> (Output)
 ```

Untuk tugas manajemen file dan direktori harian, modul ``shutil`` menyediakan antarmuka tingkat tinggi yang lebih mudah digunakan. Contoh:

```python
 >>> import shutil
 >>> shutil.copyfile('data.db', 'archive.db')
 # 'archive.db' (Output)
 >>> shutil.move('/build/executables', 'installdir')
 # 'installdir' (Output)
 ```

## 10.2. File Wildcards

Modul glob menemukan semua nama lokasi yang cocok dengan pola yang ditentukan sesuai dengan aturan yang digunakan oleh shell Unix, meskipun hasilnya dikembalikan dalam urutan arbitrer. Modul glob menyediakan fungsi untuk membuat daftar file dari pencarian wildcard direktori. Contoh:

```python
 >>> import glob
 >>> glob.glob('*.py')
 # ['primes.py', 'random.py', 'quote.py'] (Output)
 ```

## 10.3. Argumen Baris Perintah / Command Line Arguments

Skrip utilitas umum sering kali perlu memproses argumen baris perintah. Argumen ini disimpan dalam atribut *argv* di modul ``sys`` sebagai daftar. Misalnya hasil keluaran berikut dari menjalankan python ``demo.py one two three`` di baris perintah:

```python
 >>> import sys
 >>> print(sys.argv)
 # ['demo.py', 'one', 'two', 'three'] (Output)
 ```

Modul ``argparse`` menyediakan mekanisme yang lebih canggih untuk memproses argumen baris perintah. Skrip berikut mengekstrak satu atau lebih nama file dan sejumlah baris opsional yang akan ditampilkan. Contoh:

```python
 import argparse

 parser = argparse.ArgumentParser(
    prog='top',
    description='Show top lines from each file')
 parser.add_argument('filenames', nargs='+')
 parser.add_argument('-l', '--lines', type=int, default=10)
 args = parser.parse_args()
 print(args) 
 ```

**Penjelasan**: Saat dijalankan pada baris perintah dengan ``python top.py --lines=5 alpha.txt beta.txt``, skrip menyetel ``args.lines`` ke ``5`` dan ``args.filenames`` ke ``['alpha.txt', 'beta.txt']``.

## 10.4. Pengalihan Kesalahan Output dan Penghentian Program / Error Output Redirection and Program Termination

Modul *sys* juga memiliki atribut untuk *stdin*, *stdout*, dan *stderr*. Modul ini menyediakan akses ke beberapa variabel yang digunakan atau dipelihara oleh interpreter dan ke fungsi yang berinteraksi kuat dengan interpreter. Yang terakhir ini berguna untuk memancarkan peringatan dan pesan kesalahan untuk membuatnya terlihat bahkan ketika *stdout* telah dialihkan. Contoh:

```python
 >>> sys.stderr.write('Warning, log file not found starting a new one\n')
 # Warning, log file not found starting a new one (Output)
 ```

**Penjelasan**: Cara paling langsung untuk menghentikan skrip adalah dengan menggunakan ``sys.exit()``.

## 10.5. Pencocokan Pola String / String Pattern Matching

Modul re menyediakan alat ekspresi reguler untuk pemrosesan string tingkat lanjut. Untuk pencocokan dan manipulasi yang kompleks, ekspresi reguler menawarkan solusi yang ringkas dan dioptimalkan:

```python
 >>> import re
 >>> re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
 # ['foot', 'fell', 'fastest'] (Output)
 >>> re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')
 # 'cat in the hat' (Output)
 ```

Ketika hanya kemampuan sederhana yang diperlukan, metode string lebih disukai karena lebih mudah dibaca dan di-debug. Contoh:

```python
 >>> 'tea for too'.replace('too', 'two')
 # 'tea for two' (Output)
 ```

## 10.6. Matematika / Mathematics

Modul ``math`` memberikan akses ke fungsi pustaka C yang mendasari untuk matematika float. Contoh:

```python
 >>> import math
 >>> math.cos(math.pi / 4)
 # 0.70710678118654757 (Output)
 >>> math.log(1024, 2)
 # 10.0 (Output)
 ```

Contoh modul acak yang menyediakan alat untuk membuat pilihan acak:

```python
 >>> import random
 >>> random.choice(['apple', 'pear', 'banana'])
 # 'apple' (Output)
 >>> random.sample(range(100), 10)   # pengambilan sampel tanpa penggantian
 [30, 83, 16, 4, 8, 81, 41, 50, 18, 33]
 >>> random.random()    # float acak
 # 0.17970987693706186 (Output)
 >>> random.randrange(6)    # bilangan bulat acak yang dipilih dari rentang (6)
 # 4 (Output)
 ```

Modul statistik menghitung properti statistik dasar (rata-rata, median, varians, dll.) dari data numerik. Modul ini tidak dimaksudkan untuk menjadi pesaing perpustakaan pihak ketiga seperti NumPy, SciPy, atau paket statistik berfitur lengkap yang ditujukan untuk ahli statistik profesional seperti Minitab, SAS, dan Matlab. Ini ditujukan untuk tingkat grafik dan kalkulator ilmiah. Contoh:

```python
 >>> import statistics
 >>> data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
 >>> statistics.mean(data)
 # 1.6071428571428572 (Output)
 >>> statistics.median(data)
 # 1.25 (Output)
 >>> statistics.variance(data)
 # 1.3720238095238095 (Output)
 ```

## 10.7. Akses Internet / Internet Access

Ada sejumlah modul untuk mengakses internet dan memproses protokol internet. Dua yang paling sederhana adalah ``urllib.request`` digunakan untuk mengambil data dari URL dan ``smtplib`` digunakan untuk mengirim email. Contoh:

```python
 >>> from urllib.request import urlopen
 >>> with urlopen('http://worldtimeapi.org/api/timezone/etc/UTC.txt') as response:
 ...     for line in response:
 ...         line = line.decode()             # Mengonversi byte menjadi str
 ...         if line.startswith('datetime'):
 ...             print(line.rstrip())         # Hapus baris baru yang tertinggal
 ...
 # datetime: 2022-01-01T01:36:47.689215+00:00 (Output)

 >>> import smtplib
 >>> server = smtplib.SMTP('localhost')
 >>> server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
 ... """To: jcaesar@example.org
 ... From: soothsayer@example.org
 ...
 ... Beware the Ides of March.
 ... """)
 >>> server.quit()
 ```

**Catatan**: Bahwa contoh kedua membutuhkan server email yang berjalan di localhost.

## 10.8. Tanggal dan Waktu / Dates and Times
Modul ``datetime`` menyediakan kelas untuk memanipulasi tanggal dan waktu dengan cara yang sederhana dan kompleks. Sementara aritmatika tanggal dan waktu fokus implementasinya adalah pada ekstraksi anggota yang efisien untuk pemformatan dan manipulasi keluaran. Modul ini juga mendukung objek yang sadar zona waktu. Contoh:

```python
 >>> # tanggal mudah dibuat dan diformat
 >>> from datetime import date
 >>> now = date.today()
 >>> now
 datetime.date(2003, 12, 2)
 >>> now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
 # '12-02-03. 02 Dec 2003 is a Tuesday on the 02 day of December.' (Output)

 >>> # tanggal mendukung aritmatika kalender
 >>> birthday = date(1964, 7, 31)
 >>> age = now - birthday
 >>> age.days
 # 14368 (Output)
 ```

## 10.9. Kompresi data / Data Compression

Pengarsipan data umum dan format kompresi secara langsung didukung oleh modul seperti ``zlib``, ``gzip``, ``bz2``, ``lzma``, ``zipfile`` dan ``tarfile``. Contoh:

```python
 >>> import zlib
 >>> s = b'witch which has which witches wrist watch'
 >>> len(s)
 # 41 (Output)
 >>> t = zlib.compress(s)
 >>> len(t)
 # 37 (Output)
 >>> zlib.decompress(t)
 # b'witch which has which witches wrist watch' (Output)
 >>> zlib.crc32(s)
 # 226805979 (Output)
 ```

## 10.10. Pengukuran Kinerja / Performance Measurement

Beberapa pengguna Python mengembangkan minat yang mendalam untuk mengetahui kinerja relatif dari pendekatan yang berbeda untuk masalah yang sama. Misalnya, untuk menggunakan fitur pengepakan dan pembongkaran Tuple alih-alih pendekatan tradisional untuk bertukar argumen. Modul ``timeit`` dengan cepat menunjukkan keunggulan kinerja yang sederhana. Contoh:

```python
 >>> from timeit import Timer
 >>> Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
 # 0.57535828626024577 (Output)
 >>> Timer('a,b = b,a', 'a=1; b=2').timeit()
 # 0.54962537085770791 (Output)
 ```

**Penjelasan**: modul profil dan statistik menyediakan alat untuk mengidentifikasi bagian kritis waktu dalam blok kode yang lebih besar.

## 10.11. Kontrol Kualitas / Quality Control

Salah satu pendekatan untuk mengembangkan perangkat lunak berkualitas tinggi adalah dengan menulis tes untuk setiap fungsi saat dikembangkan dan menjalankan tes tersebut sesering mungkin selama proses pengembangan. Modul doctest menyediakan alat untuk memindai modul dan memvalidasi tes yang tertanam dalam program docstrings. Konstruksi pengujian sesederhana memotong dan menempelkan panggilan beserta hasilnya ke dalam docstring. Hal ini meningkatkan dokumentasi dengan memberikan contoh kepada pengguna dan memungkinkan modul doctest untuk memastikan kode tetap sesuai dengan dokumentasi. Contoh:

```python
 def average(values):
    """Menghitung rata-rata aritmatika dari daftar angka.

    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)

 import doctest
 doctest.testmod()   # secara otomatis memvalidasi tes yang disematkan
 ```

Modul unittest tidak semudah modul doctest, tetapi memungkinkan serangkaian tes yang lebih komprehensif untuk dipertahankan dalam file terpisah. Contoh:

```python
 import unittest

 class TestStatisticalFunctions(unittest.TestCase):

    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        with self.assertRaises(ZeroDivisionError):
            average([])
        with self.assertRaises(TypeError):
            average(20, 30, 70)

 unittest.main()  # Memanggil dari baris perintah memanggil semua tes
 ```

## 10.12. Termasuk Baterai / Batteries Included

Python memiliki filosofi "termasuk baterai". Ini paling baik dilihat melalui kemampuan canggih dan kuat dari paket-paketnya yang lebih besar. Sebagai contoh:

* Modul ``xmlrpc.client`` dan`` xmlrpc.server`` membuat penerapan panggilan prosedur jarak jauh menjadi tugas yang mudah. Terlepas dari nama modul, tidak ada pengetahuan langsung atau penanganan XML yang diperlukan.

* Paket ``email`` merupakan perpustakaan untuk mengelola pesan email, termasuk MIME dan dokumen pesan berbasis RFC 2822 lainnya. Tidak seperti ``smtplib`` dan ``poplib`` yang mana mengirim dan menerima pesan, paket email memiliki perangkat lengkap untuk membangun atau mendekode struktur pesan yang kompleks termasuk lampiran dan untuk mengimplementasikan encoding internet dan protokol header.

* Paket ```json``` menyediakan dukungan kuat untuk menguraikan format pertukaran data populer. Modul ``csv`` mendukung pembacaan dan penulisan file secara langsung dalam format Comma-Separated Value, umumnya didukung oleh database dan spreadsheet. Pemrosesan XML didukung oleh paket ``xml.etree.ElementTree``, ``xml.dom``, dan ``xml.sax``. Modul dan paket ini sangat menyederhanakan pertukaran data antara aplikasi Python dan alat lainnya.

* Modul ``sqlite3`` merupakan pembungkus untuk perpustakaan database SQLite, menyediakan database persisten yang dapat diperbarui dan diakses menggunakan sintaks SQL yang sedikit tidak standar.

* Internasionalisasi didukung oleh sejumlah modul termasuk ``gettext``, ``locale``, dan paket ``codec``.