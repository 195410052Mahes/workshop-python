# 11. Tur Singkat Standar Perpustakaan — Bagian II / Brief Tour of the Standard Library — Part II
---
## 11.1. Format Keluaran / Output Formatting
Modul `reprlib` menyediakan versi `repr()` yang disesuaikan untuk tampilan singkat container besar atau bersarang. Contoh:

```python
 >>> import reprlib
 >>> reprlib.repr(set('supercalifragilisticexpialidocious'))
 # "{'a', 'c', 'd', 'e', 'f', 'g', ...}" (Output)
 ```

**Penjelasan**:
Modul ``pprint`` menawarkan kontrol yang lebih canggih atas pencetakan objek bawaan dan objek yang ditentukan pengguna dengan cara yang dapat dibaca oleh penerjemah. Ketika hasilnya lebih dari satu baris,maka program akan menambahkan jeda baris dan lekukan untuk mengungkapkan struktur data dengan lebih jelas. Contoh:

```python
 >>> import pprint
 >>> t = [[[['black', 'cyan'], 'white', ['green',   'red']], [['magenta',
 ...     'yellow'], 'blue']]]
 ...
 >>> pprint.pprint(t, width=30)
 # (Output)
 """
 [[[['black', 'cyan'],
   'white',
   ['green', 'red']],
  [['magenta', 'yellow'],
   'blue']]]
 """
 ```

Modul ``textwrap`` memformat paragraf teks agar sesuai dengan lebar layar tertentu. Modul ``textwrap`` memformat paragraf teks agar sesuai dengan lebar layar yang diberikan. Contoh:

```python 
 >>> import textwrap
 >>> doc = """The wrap() method is just like fill()   except that it returns
 ... a list of strings instead of one big string with  newlines to separate
 ... the wrapped lines."""
 ...
 >>> print(textwrap.fill(doc, width=40))
 # (Output)
 """
 The wrap() method is just like fill()
 except that it returns a list of strings
 instead of one big string with newlines
 to separate the wrapped lines.
 """
 ```

Modul lokal mengakses database format data spesifik. Atribut pengelompokan fungsi format lokal dan menyediakan cara langsung memformat angka dengan pemisah grup. Contoh:

```python
 >>> import locale
 >>> locale.setlocale(locale.LC_ALL, 'English_United States.1252')
 # 'English_United States.1252' (Output)
 >>> conv = locale.localeconv()          # mendapatkan pemetaan konvensi
 >>> x = 1234567.8
 >>> locale.format("%d", x, grouping=True)
 # '1,234,567' (Output)
 >>> locale.format_string("%s%.*f", (conv['currency_symbol'],
 ...                      conv['frac_digits'], x), grouping=True)
 # '$1,234,567.80' (Output)
 ```

---

## 11.2. Templating / Templating

Modul ``string`` menyertakan kelas ``Template`` serbaguna dengan sintaks yang disederhanakan yang cocok untuk diedit oleh pengguna akhir. Hal ini memungkinkan pengguna untuk menyesuaikan aplikasi mereka tanpa harus mengubah aplikasi. Contoh:

```python
 >>> from string import Template
 >>> t = Template('${village}folk send $$10 to $cause.')
 >>> t.substitute(village='Nottingham', cause='the ditch fund')
 # 'Nottinghamfolk send $10 to the ditch fund.' (Output)
 ```

**Penjelasan**:
Menggunakan nama Format placeholder yang dibentuk menggunakan ``$`` dengan pengidentifikasian Python yang valid karakter alfanumerik dan garis bawah. Mengelilingi placeholder dengan kurung memungkinkan untuk diikuti oleh lebih banyak huruf alfanumerik tanpa spasi.

Metode ``subtitute()`` memunculkan ``KeyError`` ketika placeholder tidak disediakan dalam kamus atau argumen kata kunci. Untuk aplikasi dengan gaya gabungan surat, data yang diberikan pengguna mungkin tidak lengkap dan metode ``safe_substitute()`` mungkin lebih tepat, hal ini akan membuat placeholder tidak berubah jika data hilang. Contoh:

```python
 >>> t = Template('Return the $item to $owner.')
 >>> d = dict(item='unladen swallow')
 >>> t.substitute(d)
 # (Output)
 """
 Traceback (most recent call last):
  ...
 KeyError: 'owner'
 """
 >>> t.safe_substitute(d)
 # 'Return the unladen swallow to $owner.' (Output)
 ```


Subkelas template dapat menentukan pembatas kustom. Misalnya, utilitas penggantian nama batch untuk browser foto dapat memilih untuk menggunakan tanda persen untuk placeholder seperti tanggal saat ini, nomor urut gambar, atau format file. Contoh:

```python
 >>> import time, os.path
 >>> photofiles = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']
 >>> class BatchRename(Template):
 ...     delimiter = '%'
 >>> fmt = input('Enter rename style (%d-date %n-seqnum %f-format):  ')
 # Enter rename style (%d-date %n-seqnum %f-format):  Ashley_%n%f (Output)

 >>> t = BatchRename(fmt)
 >>> date = time.strftime('%d%b%y')
 >>> for i, filename in enumerate(photofiles):
 ...     base, ext = os.path.splitext(filename)
 ...     newname = t.substitute(d=date, n=i, f=ext)
 ...     print('{0} --> {1}'.format(filename, newname))
 # (Output)
 """
 img_1074.jpg --> Ashley_0.jpg
 img_1076.jpg --> Ashley_1.jpg
 img_1077.jpg --> Ashley_2.jpg
 """
 ```

**Penjelasan**:
Aplikasi lain untuk templating adalah memisahkan logika program dari detail beberapa format output. Hal ini memungkinkan untuk mengganti template kustom untuk file XML, laporan teks biasa, dan laporan web HTML.

---

## 1.3. Bekerja dengan Tata Letak Rekaman Data Biner / Working with Binary Data Record Layouts

Modul struct menyediakan fungsi pack() dan unpack() untuk bekerja dengan format record biner dengan panjang variabel. Contoh:

```python
 import struct

 with open('myfile.zip', 'rb') as f:
    data = f.read()

 start = 0
 for i in range(3):                      # menampilkan 3 header file pertama
    start += 14
    fields = struct.unpack('<IIIHH', data[start:start+16])
    crc32, comp_size, uncomp_size, filenamesize, extra_size = fields

    start += 16
    filename = data[start:start+filenamesize]
    start += filenamesize
    extra = data[start:start+extra_size]
    print(filename, hex(crc32), comp_size, uncomp_size)

    start += extra_size + comp_size     # lompat ke judul berikutnya
 ```

**Penjelasan**:
Contoh diatas menunjukkan cara mengulang informasi header dalam file ZIP tanpa menggunakan modul ``zipfile``. Kode paket ``"H"`` dan ``"I"`` masing-masing mewakili dua dan empat byte angka tidak bertanda. tanda ``"<"`` menunjukkan bahwa ukuran standar dan dalam urutan byte little-endian

---
## 11.4. Utas Ganda / Multi-threading

Threading adalah teknik untuk memisahkan tugas yang tidak bergantung secara berurutan. Utas dapat digunakan untuk meningkatkan daya tanggap aplikasi yang menerima masukan pengguna saat tugas lain berjalan di latar belakang. Kasus penggunaan terkait menjalankan I/O (Input dan Output) secara paralel dengan perhitungan di utas lain. Kode berikut menunjukkan bagaimana modul threading tingkat tinggi dapat menjalankan tugas di latar belakang sementara program utama terus berjalan:

```python
 import threading, zipfile

 class AsyncZip(threading.Thread):
    def __init__(self, infile, outfile):
        threading.Thread.__init__(self)
        self.infile = infile
        self.outfile = outfile

    def run(self):
        f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
        f.write(self.infile)
        f.close()
        print('Finished background zip of:', self.infile)

 background = AsyncZip('mydata.txt', 'myarchive.zip')
 background.start()
 print('The main program continues to run in foreground.')

 background.join()    # Tunggu tugas latar belakang selesai
 print('Main program waited until background was done.')
 ```

**Penjelasan**:
Tantangan utama aplikasi multi-utas adalah mengoordinasikan utas yang berbagi data atau sumber daya lainnya. Untuk itu, modul threading menyediakan sejumlah primitif sinkronisasi termasuk kunci, peristiwa, variabel kondisi, dan semaphore. Meskipun alat-alat tersebut sangat kuat, kesalahan desain kecil dapat mengakibatkan masalah yang sulit untuk direproduksi. Jadi, pendekatan yang lebih disukai untuk koordinasi tugas adalah memusatkan semua akses ke sumber daya dalam satu utas dan kemudian menggunakan modul antrian untuk memberi makan utas itu dengan permintaan dari utas lain. Aplikasi yang menggunakan objek Antrian untuk komunikasi dan koordinasi antar-utas lebih mudah dirancang, lebih mudah dibaca, dan lebih andal.

---
## 11.5. Pencatatan / Logging

Modul logging menawarkan sistem logging berfitur lengkap dan fleksibel. Paling sederhana, pesan log dikirim ke file atau ke ``sys.stderr``. Contoh:

```python
 import logging
 logging.debug('Debugging information')
 logging.info('Informational message')
 logging.warning('Warning:config file %s not found', 'server.conf')
 logging.error('Error occurred')
 logging.critical('Critical error -- shutting down')

 # (Output)
 """
 WARNING:root:Warning:config file server.conf not found
 ERROR:root:Error occurred
 CRITICAL:root:Critical error -- shutting down
 """
 ```

**Penjelasan**:
Secara default, pesan informasi dan debugging ditekan dan output dikirim ke kesalahan standar. Opsi keluaran lainnya termasuk perutean pesan melalui email, datagram, soket, atau ke Server HTTP. Filter baru dapat memilih perutean yang berbeda berdasarkan prioritas pesan. Misal: DEBUG, INFO, WARNING, ERROR, and CRITICAL. Sistem logging dapat dikonfigurasi langsung dari Python atau dapat dimuat dari file konfigurasi yang dapat diedit pengguna untuk logging yang disesuaikan tanpa mengubah aplikasi.

---
## 11.6. Referensi Lemah / Weak References 
Python melakukan manajemen memori otomatis disinya artinya penghitungan referensi untuk sebagian besar objek dan pengumpulan sampah untuk menghilangkan siklus. Memori segera dibebaskan setelah referensi terakhir dihilangkan. Pendekatan ini bekerja dengan baik untuk sebagian besar aplikasi, tetapi terkadang ada kebutuhan untuk melacak objek yang hanya selama mereka digunakan oleh sesuatu yang lain. Modul ``weakref`` menyediakan alat untuk melacak objek tanpa membuat referensi. Ketika objek tidak lagi diperlukan, objek tersebut secara otomatis dihapus dari tabel referensi yang lemah dan panggilan balik dipicu untuk objek referensi yang lemah. Aplikasi umum termasuk objek caching yang mahal untuk dibuat. Contoh:

```python
 >>> import weakref, gc
 >>> class A:
 ...     def __init__(self, value):
 ...         self.value = value
 ...     def __repr__(self):
 ...         return str(self.value)
 ...
 >>> a = A(10)                   # membuat referensi
 >>> d = weakref.WeakValueDictionary()
 >>> d['primary'] = a            # tidak membuat referensi
 >>> d['primary']                # ambil objek jika masih hidup
 # 10 (Output)
 >>> del a                       # hapus satu referensi
 >>> gc.collect()                # segera jalankan pengumpulan sampah 
 # 0 (Output)
 >>> d['primary']                # entri dihapus secara otomatis
 # (Output)
 """
 Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    d['primary']                # entri dihapus secara otomatis
  File "C:/python310/lib/weakref.py", line 46, in __getitem__
    o = self.data[key]()
 KeyError: 'primary'
 """
 ```

---
## 11.7. Alat untuk Bekerja dengan Daftar / Tools for Working with Lists 
Modul ``array`` menyediakan objek ``array()`` seperti daftar yang hanya menyimpan data homogen dan menyimpannya dengan lebih ringkas. Contoh berikut menunjukkan larik angka yang disimpan sebagai dua byte angka biner tidak bertanda (typecode ``"H"``) daripada 16 byte biasa per entri untuk daftar reguler objek int Python:

```python
 >>> from array import array
 >>> a = array('H', [4000, 10, 700, 22222])
 >>> sum(a)
 # 26932 (Output)
 >>> a[1:3]
 # array('H', [10, 700]) (Output)
 ```

Modul ``collections`` menyediakan objek ``deque()`` yang seperti daftar dengan penambahan lebih cepat dan muncul dari sisi kiri tetapi pencarian lebih lambat di tengah. Objek-objek ini sangat cocok untuk mengimplementasikan antrian dan pencarian pohon pertama yang luas. Contoh: 

```python
 >>> from collections import deque
 >>> d = deque(["task1", "task2", "task3"])
 >>> d.append("task4")
 >>> print("Handling", d.popleft())
 # Handling task1 (Output)
 ```

```python
 unsearched = deque([starting_node])
 def breadth_first_search(unsearched):
    node = unsearched.popleft()
    for m in gen_moves(node):
        if is_goal(m):
            return m
        unsearched.append(m)
 ```

Selain implementasi daftar alternatif, library juga menawarkan alat lain seperti modul bagi dua dengan fungsi untuk memanipulasi daftar yang diurutkan. Contoh:

```python
 >>> import bisect 
 >>> scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500,   'python')]
 >>> bisect.insort(scores, (300, 'ruby'))
 >>> scores
 # [(100, 'perl'), (200, 'tcl'), (300, 'ruby'), (400, 'lua'), (500, 'python')] (Output)
 ```

Modul ``heapq`` menyediakan fungsi untuk mengimplementasikan heap berdasarkan daftar reguler. Entri bernilai terendah selalu disimpan di posisi nol. Hal ini berguna untuk aplikasi yang berulang kali mengakses elemen terkecil tetapi tidak menjalankan pengurutan daftar lengkap. Contoh:

```python
 >>> from heapq import heapify, heappop, heappush
 >>> data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
 >>> heapify(data)                      # atur ulang daftar menjadi urutan tumpukan
 >>> heappush(data, -5)                 # tambahkan entri baru
 >>> [heappop(data) for i in range(3)]  # ambil tiga entri terkecil
 # [-5, 0, 1] (Output)
 ```

---
## 11.8. Aritmatika Titik Float Desimal / Decimal Floating Point Arithmetic

Modul desimal menawarkan tipe data Desimal untuk aritmatika titik mengambang desimal. Modul desimal menyediakan dukungan untuk aritmatika floating point desimal yang dibulatkan dengan benar dan cepat. Dibandingkan dengan implementasi float built-in dari floating point biner, kelas ini sangat membantu untuk:

* aplikasi keuangan dan penggunaan lain yang memerlukan representasi desimal yang tepat,
* kontrol atas presisi,
* kontrol atas pembulatan untuk memenuhi persyaratan hukum atau peraturan,
* pelacakan tempat desimal yang signifikan,
* aplikasi di mana pengguna mengharapkan hasil yang sesuai dengan perhitungan yang dilakukan dengan tangan.

Sebagai contoh, menghitung pajak 5% untuk biaya telepon 70 sen memberikan hasil yang berbeda dalam floating point desimal dan floating point biner. Selisihnya menjadi signifikan jika hasilnya dibulatkan ke sen terdekat. Contoh:

```python
 >>> from decimal import *
 >>> round(Decimal('0.70') * Decimal('1.05'), 2)
 # Decimal('0.74') (Output)
 >>> round(.70 * 1.05, 2)
 # 0.73 (Output)
 ```

**Penjelasan**:
Hasil Desimal mempertahankan angka nol, secara otomatis menyimpulkan signifikansi empat tempat dari perkalian dengan signifikansi dua tempat. Desimal mereproduksi matematika seperti yang dilakukan dengan tangan dan menghindari masalah yang dapat muncul ketika titik float biner tidak dapat secara tepat mewakili jumlah desimal.

Representasi yang tepat memungkinkan kelas Desimal untuk melakukan perhitungan modulo dan tes kesetaraan yang tidak cocok untuk floating point biner.Modul desimal menyediakan dukungan untuk aritmatika floating point desimal yang dibulatkan dengan benar dengan cepat. Contoh:

```python
 >>> Decimal('1.00') % Decimal('.10')
 # Decimal('0.00') (Output)
 >>> 1.00 % 0.10
 # 0.09999999999999995 (Output)

 >>> sum([Decimal('0.1')]*10) == Decimal('1.0')
 # True (Output)
 >>> sum([0.1]*10) == 1.0
 # False (Output)
 ```

Modul desimal menyediakan aritmatika dengan presisi sebanyak yang diperlukan. Contoh:

```python
 >>> getcontext().prec = 36
 >>> Decimal(1) / Decimal(7)
 # Decimal('0.142857142857142857142857142857142857') (Output)
 ```