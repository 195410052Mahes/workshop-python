# 9. Kelas / Classes

Kelas menyediakan sarana untuk menggabungkan data dan fungsionalitas bersama-sama. Membuat kelas baru membuat tipe objek baru, memungkinkan instance baru dari tipe itu dibuat. Setiap instance kelas dapat memiliki atribut yang dilampirkan untuk mempertahankan statusnya.

mekanisme kelas Python menambahkan kelas dengan sintaks dan semantik baru yang minimal. Kelas Python menyediakan semua fitur standar Pemrograman Berorientasi Objek. Mekanisme pewarisan kelas memungkinkan beberapa kelas dasar, kelas turunan dapat mengganti metode apa pun dari kelas atau kelas dasarnya, dan metode dapat memanggil metode kelas dasar dengan nama yang sama. Objek dapat berisi jumlah dan jenis data yang berubah-ubah. Seperti halnya modul, kelas mengambil bagian dari sifat dinamis.

---

## 9.1. Sepatah Kata Tentang Nama dan Objek / A Word About Names and Objects

Objek memiliki individualitas, dan beberapa nama (alam beberapa cakupan dapat diikat ke objek yang sama atau yang dikenal sebagai aliasing dalam bahasa lain. Namun, aliasing memiliki efek yang mungkin mengejutkan pada semantik kode Python yang melibatkan objek yang bisa berubah seperti daftar, kamus, dan sebagian besar jenis lainnya dan biasanya digunakan untuk kepentingan program, karena alias berperilaku seperti pointer dalam beberapa hal. Misalnya, melewatkan sebuah objek karena hanya sebuah pointer yang dilewatkan oleh implementasi dan jika suatu fungsi memodifikasi objek yang diteruskan sebagai argumen, pemanggil akan melihat perubahannya dan menghilangkan kebutuhan akan dua mekanisme penerusan argumen yang berbeda seperti dalam Pascal.

---

## 9.2. Lingkup Python dan Ruang Nama / Python Scopes and Namespaces

Ruan nama adalah pemetaan dari nama ke objek. Sebagian besar ruang nama saat ini diimplementasikan sebagai kamus Python, tetapi biasanya tidak terlihat dengan cara apa pun kecuali untuk kinerja, dan mungkin berubah di masa mendatang. 

Contoh ruang nama adalah: kumpulan nama bawaan berisi fungsi seperti ``abs()``, dan nama pengecualian bawaan nama global dalam modul dan nama lokal dalam pemanggilan fungsi. Dalam arti set atribut dari suatu objek juga membentuk namespace.

Hal penting yang perlu diketahui tentang namespace adalah bahwa sama sekali tidak ada hubungan antara nama di namespace yang berbeda misalnya, dua modul yang berbeda dapat mendefinisikan fungsi maksimal tanpa pengguna modul harus mengawalinya dengan nama modul.

Atribut mungkin hanya dibaca atau dapat ditulis. Dalam kasus terakhir, penugasan ke atribut dimungkinkan. Atribut modul dapat ditulis: ``modname.the_answer = 42``.  Atribut yang dapat ditulis juga dapat dihapus dengan pernyataan del. Misalnya, ``del modname.the_answer`` akan menghapus atribut ``the_answer`` dari objek yang dinamai dengan ``modname``. 

Ruang nama dibuat pada saat yang berbeda dan memiliki waktu yang berbeda. Namespace yang berisi nama bawaan dibuat saat interpreter Python dijalankan, dan tidak pernah dihapus. Namespace global untuk sebuah modul dibuat ketika definisi modul dibaca biasanya, ruang nama modul juga bertahan hingga juru bahasa berhenti.

Pernyataan yang dieksekusi oleh pemanggilan tingkat atas dari juru bahasa, baik yang dibaca dari file skrip atau secara interaktif, dianggap sebagai bagian dari modul yang disebut ``__main__``, jadi mereka memiliki ruang nama global mereka sendiri. Ruang nama lokal untuk suatu fungsi dibuat saat fungsi dipanggil, dan dihapus saat fungsi mengembalikan atau memunculkan pengecualian yang tidak ditangani dalam fungsi. Tentu saja, pemanggilan rekursif masing-masing memiliki ruang nama lokal mereka sendiri.

Setiap saat selama eksekusi, ada 3 atau 4 cakupan bersarang yang ruang namanya dapat diakses secara langsung:

* lingkup terdalam, yang dicari terlebih dahulu, berisi nama-nama lokal.

* cakupan dari setiap fungsi terlampir, yang dicari mulai dengan lingkup terlampir terdekat, berisi nama non-lokal, tetapi juga non-global.

* lingkup berikutnya-ke-terakhir berisi nama global modul saat ini.

* lingkup terluar dicari terakhir adalah namespace yang berisi nama bawaan.

Jika sebuah nama dideklarasikan global, maka semua referensi dan penugasan langsung menuju ke ruang lingkup tengah yang berisi nama global modul. Untuk rebind variabel yang ditemukan di luar lingkup terdalam, pernyataan nonlocal dapat digunakan jika tidak dideklarasikan nonlocal, variabel-variabel tersebut hanya dibaca untuk menulis ke variabel semacam itu dan hanya akan membuat variabel lokal baru di lingkup terdalam, sehingga membiarkan variabel luar bernama identik tidak berubah.

---

### 9.2.1. Ruang Lingkup dan Contoh Ruang Nama / Scopes and Namespaces Example

dibawah ini merupakan contoh yang menunjukkan cara mereferensikan cakupan dan ruang nama yang berbeda, dan bagaimana pengaruh global dan nonlokal terhadap pengikatan variabel:

```python
 def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

 scope_test()
 print("In global scope:", spam)
 ``` 

**Output program diatas**: 
```python
 After local assignment: test spam
 After nonlocal assignment: nonlocal spam
 After global assignment: nonlocal spam
 In global scope: global spam
 ```  

---

## 9.3. Pandangan Pertama di Kelas / A First Look at Classes

Kelas memperkenalkan sedikit sintaks baru, tiga tipe objek baru, dan beberapa semantik baru.

---

### 9.3.1. Sintaks Definisi Kelas / Class Definition Syntax

contoh sederhana definisi kelas:
```python
 class ClassName:
    <statement-1>
    .
    .
    .
    <statement-N>
 ```

Definisi kelas, seperti definisi fungsi pernyataan def harus dijalankan sebelum memiliki efek apa pun. Kita bisa menempatkan definisi kelas di cabang pernyataan if, atau di dalam fungsi. Pernyataan di dalam definisi kelas biasanya berupa definisi fungsi, tetapi pernyataan lain juga diperbolehkan. 

Definisi fungsi di dalam kelas biasanya memiliki bentuk daftar argumen yang khas, ditentukan oleh konvensi pemanggilan untuk beberapa metode. Ketika definisi kelas dimasukkan, ruang nama baru dibuat, dan digunakan sebagai lingkup lokal, dengan demikian semua tugas ke variabel lokal masuk ke ruang nama baru ini. Secara khusus, definisi fungsi mengikat nama fungsi baru. Ketika definisi kelas dibiarkan secara normal, objek kelas otomatis dibuat. Ini pada dasarnya adalah pembungkus konten namespace yang dibuat oleh definisi kelas.

---

### 9.3.2. Objek kelas / Class Objects

Referensi atribut menggunakan sintaks standar yang digunakan untuk semua referensi atribut di Python yaitu ```obj.name```. 

**Contoh**:
```python
 class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'
 ```

**Penjelasan**:
``MyClass.i`` dan ``MyClass.f`` adalah referensi atribut yang valid, masing-masing mengembalikan integer dan objek fungsi. Atribut kelas juga dapat ditetapkan, sehingga  dapat mengubah nilai ``MyClass.i`` berdasarkan penetapan. ``__doc__`` juga merupakan atribut yang valid, mengembalikan docstring milik kelas "Kelas contoh sederhana".

Instansiasi kelas menggunakan notasi fungsi. Anggap saja objek kelas adalah fungsi tanpa parameter yang mengembalikan instance baru dari kelas. Misalnya:
```python
 x = MyClass()
 ```
**Penjelasan**:
membuat instance baru dari kelas dan menetapkan objek ini ke variabel lokal ``x``.

Operasi instantiasi "memanggil" objek kelas membuat objek kosong. Banyak kelas membuat objek dengan instance yang disesuaikan dengan keadaan awal tertentu. Oleh karena itu, sebuah kelas dapat mendefinisikan metode khusus bernama ``__init__()``, Contoh:
```python
 def __init__(self):
    self.data = []
 ```
**Penjelasan**:
Ketika sebuah kelas mendefinisikan metode ``__init__()``, instantiasi kelas secara otomatis memanggil ``__init__()`` untuk instance kelas yang baru dibuat. Jadi dalam contoh ini, instance baru yang diinisialisasi dapat diperoleh dengan:
```python
 x = MyClass()
 ```

Tentu saja, metode ``__init__()`` mungkin memiliki argumen untuk fleksibilitas yang lebih besar. Dalam hal ini, argumen yang diberikan ke operator instantiasi kelas diteruskan ke ``__init__()``. Contoh:
```python
 >>> class Complex:
 ...     def __init__(self, realpart, imagpart):
 ...         self.r = realpart
 ...         self.i = imagpart
 ...
 >>> x = Complex(3.0, -4.5)
 >>> x.r, x.i
(3.0, -4.5)
 ```

---

### 9.3.3. Objek Instance / Instance Objects

Atribut data sesuai dengan "variabel instan" di Smalltalk, dan "anggota data" di C++. Atribut data tidak perlu dideklarasikan seperti variabel lokal, mereka muncul saat pertama kali ditugaskan. Misalnya, jika ``x`` adalah instance ``MyClass`` yang dibuat di atas, potongan kode berikut akan mencetak nilai ``16`` tanpa meninggalkan jejak. Contoh:
```python
 x.counter = 1
 while x.counter < 10:
    x.counter = x.counter * 2
 print(x.counter)
 del x.counter
 ```

**Penjelasan**:
Metode adalah fungsi yang “milik” suatu objek. Dalam Python, istilah metode tidak unik untuk instance kelas: tipe objek lain dapat memiliki metode juga. Misalnya, objek daftar memiliki metode yang disebut append, insert, remove, sort, dan sebagainya.

Nama metode yang valid dari objek instance bergantung pada kelasnya. Menurut definisi, semua atribut kelas yang merupakan objek fungsi mendefinisikan metode yang sesuai dari instance-nya.

---

### 9.3.4. Objek Metode / Method Objects

Biasanya, suatu metode dipanggil  dengan ``x.f()``. pada contoh ``MyClass`` ini akan mengembalikan string 'hello world'. Namun, tidak perlu memanggil metode ``x.f`` yang merupakan objek metode, dan dapat disimpan dan dipanggil di lain waktu. Sebagai contoh:

```python
 xf = x.f
 while True:
    print(xf())
 ```

**Penjelasan**:
Hal khusus tentang metode adalah bahwa objek instance dilewatkan sebagai argumen pertama dari fungsi tersebut. Dalam contoh, panggilan ``x.f()`` sama persis dengan ``MyClass.f(x)``. Secara umum, memanggil metode dengan daftar argumen *n* sama dengan memanggil fungsi yang sesuai dengan daftar argumen yang dibuat dengan memasukkan objek instance metode sebelum argumen pertama.

---

### 9.3.5. Variabel Kelas dan Instance / Class and Instance Variables

Variabel instan untuk data yang unik setiap instance dan variabel kelas untuk atribut dan metode yang dibagikan oleh semua instance kelas. Contoh:
```python
 class Dog:

    kind = 'canine'         # variabel kelas yang dibagikan oleh semua instance

    def __init__(self, name):
        self.name = name    # variabel instance unik untuk setiap instance

 >>> d = Dog('Fido')
 >>> e = Dog('Buddy')
 >>> d.kind                  # dibagikan oleh semua anjing
 # 'canine' (Output)
 >>> e.kind                  # dibagikan oleh semua anjing
 # 'canine' (Output)
 >>> d.name                  # untuk d
 # 'Fido' (Output)
 >>> e.name                  # untuk e
 # 'Buddy' (Output)
 ```

Seperti yang dibahas dalam A Word About Names and Objects, data bersama dapat memiliki efek yang mungkin mengejutkan dengan melibatkan objek yang dapat berubah seperti daftar dan kamus. Misalnya, daftar trik dalam kode berikut tidak boleh digunakan sebagai variabel kelas karena hanya satu daftar yang akan dibagikan oleh semua instance Anjing. Contoh:
```python
 class Dog:

    tricks = []             # kesalahan penggunaan variabel kelas

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)

 >>> d = Dog('Fido')
 >>> e = Dog('Buddy')
 >>> d.add_trick('roll over')
 >>> e.add_trick('play dead')
 >>> d.tricks                # secara tak terduga dibagikan oleh semua anjing
 # ['roll over', 'play dead'] (Output)
 ```

Desain kelas yang benar harus menggunakan variabel instan, maka sebagai gantinya:
```python 
 class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []    # membuat daftar kosong baru untuk setiap anjing

    def add_trick(self, trick):
        self.tricks.append(trick)

 >>> d = Dog('Fido')
 >>> e = Dog('Buddy')
 >>> d.add_trick('roll over')
 >>> e.add_trick('play dead')
 >>> d.tricks
 # ['roll over'] (Output)
 >>> e.tricks
 # ['play dead'] (Output)
 ```

---

## 9.4. Keterangan Acak / Random Remarks

Jika nama atribut yang sama terjadi di kedua instance dan di kelas, maka pencarian atribut memprioritaskan instance. Contoh:
```python
 >>> class Warehouse:
        purpose = 'storage'
        region = 'west'

 >>> w1 = Warehouse()
 >>> print(w1.purpose, w1.region)
 # storage west (Output)
 >>> w2 = Warehouse()
 >>> w2.region = 'east'
 >>> print(w2.purpose, w2.region)
 # storage east (Output)
 ```
**Penjelasan**:
Atribut data dapat direferensikan oleh metode serta oleh pengguna biasa atau klien dari suatu objek. Dengan kata lain, kelas tidak dapat digunakan untuk mengimplementasikan tipe data yang bersifat abstrak murni. Faktanya, tidak ada dalam Python yang memungkinkan untuk memaksakan penyembunyian data, semuanya didasarkan pada konvensi.

Objek fungsi apa pun yang merupakan atribut kelas mendefinisikan metode untuk instance kelas tersebut. Definisi fungsi tidak perlu secara tekstual dilampirkan dalam definisi kelas untuk menetapkan objek fungsi ke variabel lokal di kelas. Sebagai contoh:
```python
 # Fungsi didefinisikan di luar kelas
def f1(self, x, y):
    return min(x, x+y)

class C:
    f = f1

    def g(self):
        return 'hello world'

    h = g
 ```

**Penjelasan**:
Sekarang ``f``, ``g`` dan ``h`` adalah semua atribut kelas C yang merujuk ke objek fungsi, dan akibatnya semua adalah metode dari instance C — ``h`` yang persis sama dengan ``g``. Perhatikan bahwa praktik ini biasanya hanya berfungsi untuk membingungkan pembaca suatu program.

Metode dapat memanggil metode lain dengan menggunakan atribut metode argumen ``self``. Contoh :
```python
 class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)
 ```

Metode dapat mereferensikan nama global dengan cara yang sama seperti fungsi biasa. Lingkup global yang terkait dengan suatu metode adalah modul yang berisi definisinya.

---

## 9.5. Pewarisan / Inheritance

Fitur bahasa tidak akan layak disebut "kelas" tanpa mendukung pewarisan. Contoh sintaks untuk definisi kelas turunan seperti ini:
```python
 class DerivedClassName(BaseClassName):
    <statement-1>
    .
    .
    .
    <statement-N>
 ```
**Penjelasan**:
Nama ``BaseClassName`` harus didefinisikan dalam lingkup yang berisi definisi kelas turunan. Di tempat nama kelas dasar, ekspresi arbitrer lainnya juga diperbolehkan. Hal ini bisa berguna, misalnya, ketika kelas dasar didefinisikan di modul lain. Contoh:
```python 
 class DerivedClassName(modname.BaseClassName):
 ```
Eksekusi definisi kelas turunan berlangsung sama seperti untuk kelas dasar. Ketika objek kelas dibangun, kelas dasar akan diingat. Hal ini digunakan untuk menyelesaikan referensi atribut. Jika atribut yang diminta tidak ditemukan di kelas, maka pencarian akan dilanjutkan untuk mencari di kelas dasar. Aturan ini diterapkan secara rekursif jika kelas dasar itu sendiri diturunkan dari beberapa kelas lain.

Python memiliki dua fungsi bawaan yang bekerja dengan pewarisan:
* Gunakan ``isinstance()`` untuk memeriksa tipe instance ``isinstance(obj, int)`` maka akan bernilai ``True`` hanya jika ``obj.__class__`` merupakan ``int`` atau beberapa kelas turunan dari ``int``.

* Gunakan ``issubclass()`` untuk memeriksa pewarisan kelas ``issubclass(bool, int)`` adalah ``True`` karena ``bool`` merupakan subclass dari ``int``. Namun, ``issubclass(float, int)`` merupakan ``False`` karena ``float`` bukan subclass dari ``int``.

---
### 9.5.1. Pewarisan Berganda / Multiple Inheritance
Python juga mendukung bentuk pewarisan berganda. Definisi kelas dengan beberapa kelas dasar terlihat seperti ini:
```python
 class DerivedClassName(Base1, Base2, Base3):
    <statement-1>
    .
    .
    .
    <statement-N>
 ```
**Penjelasan**:
Untuk sebagian besar tujuan, dalam kasus yang paling sederhana, dapat dianggap sebagai pencarian atribut yang diwarisi dari kelas induk sebagai depth-first, left-to-right, bukan pencarian dua kali di kelas yang sama di mana terdapat tumpang tindih dalam hierarki. Jadi, jika suatu atribut tidak ditemukan di DerivedClassName, maka dapat dicari di Base1, kemudian secara rekursif di kelas dasar Base1, dan jika tidak ditemukan , maka akan  dicari di Base2, dan seterusnya.

---
### 9.6. Variabel Privat / Private Variables
Variabel instance "Privat" yang tidak dapat diakses kecuali dari dalam objek tidak ada di Python. Namun, ada konvensi yang diikuti oleh sebagian besar kode Python yaitu nama yang diawali dengan garis bawah misalnya ``_spam`` harus diperlakukan sebagai bagian non-publik dari API apakah itu fungsi, metode, atau anggota data dan ini harus dianggap sebagai detail implementasi dan dapat berubah tanpa pemberitahuan.

Karena ada kasus penggunaan yang valid untuk anggota kelas privat yaitu untuk menghindari bentrokan nama-nama dengan nama yang ditentukan oleh subkelas, ada dukungan terbatas untuk mekanisme seperti itu, yang disebut dengan *mangling*. Setiap pengidentifikasi dari formulir ``__spam`` setidaknya dua garis bawah di depan, paling banyak satu garis bawah di akhir secara tekstual diganti dengan ``_classname__spam``, di mana ``classname`` merupakan nama kelas saat ini dengan garis bawah utama. Mangling ini dilakukan tanpa memperhatikan posisi sintaks dari identifier, selama itu terjadi dalam definisi kelas.

Name mangling berguna untuk membiarkan subclass menimpa metode tanpa memutus panggilan metode intraclass. Sebagai contoh:
```python
 class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # salinan privat dari metode update() 

 class MappingSubclass(Mapping):

    def update(self, keys, values):
        # memberikan tanda tangan baru untuk pembaruan ()
        # tetapi tidak merusak __init__()
        for item in zip(keys, values):
            self.items_list.append(item)
 ```
**Penjelasan**:
Contoh di atas akan berfungsi bahkan jika ``MappingSubclass`` memperkenalkan pengenal ``__update`` karena diganti dengan ``_Mapping__update`` di kelas ``Mapping`` dan ``_MappingSubclass__update`` di masing-masing kelas ``MappingSubclass``.

---

## 9.7. Barang sisa / Odds and Ends
Definisi kelas kosong akan berfungsi dengan baik dan berguna untuk memiliki tipe data yang mirip dengan "record" Pascal atau "struct" C dengan menggabungkan beberapa item data ternama. Contoh:
```python
 class Employee:
    pass

 john = Employee()  # Buat catatan karyawan kosong

 # Isi bidang catatan (Output)
 '''
 john.name = 'John Doe'
 john.dept = 'computer lab'
 john.salary = 1000
 '''
 ```
**Penjelasan**:
Sepotong kode Python yang mengharapkan tipe data abstrak tertentu sering kali dapat dilewatkan ke kelas yang mengemulasi metode tipe data itu sebagai gantinya. Misalnya, jika memiliki fungsi yang memformat beberapa data dari objek file, maka bisa dengan melalukakn definisi kelas dengan metode ``read``() dan ``readline() ``yang mendapatkan data dari buffer string, dan meneruskannya sebagai argumen.

Objek metode instance juga dimiliki atribut: ``m.__self__`` yang merupakan objek instance dengan metode ``m()``, dan ``m.__func__`` yang merupakan objek fungsi yang sesuai dengan metode tersebut.

---

## 9.8. Iterator/ Iterators
bahwa sebagian besar objek kontainer dapat diulang menggunakan pernyataan for. Contoh:
```python
 for element in [1, 2, 3]:
    print(element)
 for element in (1, 2, 3):
    print(element)
 for key in {'one':1, 'two':2}:
    print(key)
 for char in "123":
    print(char)
 for line in open("myfile.txt"):
    print(line, end='')
 ```
**Penjelasan**:
Akses ini jelas, ringkas, dan nyaman. Penggunaan iterator meliputi dan menyatukan Python. Di balik layar, pernyataan for memanggil ``iter()`` pada objek container. Fungsi mengembalikan objek iterator yang mendefinisikan metode ``__next__()`` yang mengakses elemen dalam wadah satu per satu. Ketika tidak ada lagi elemen, ``__next__()`` memunculkan pengecualian ``StopIteration`` yang memberi tahu perulangan for untuk berhenti. Dapat dipanggil menggunakan metode ``__next__()`` menggunakan fungsi bawaan ``next()``. contoh ini menunjukkan cara kerjanya:

```python
 >>> s = 'abc'
 >>> it = iter(s)
 >>> it
 # <str_iterator object at 0x10c90e650>
 >>> next(it)
 # 'a' (Output)
 >>> next(it)
 # 'b' (Output)
 >>> next(it)
 # 'c' (Output)
 >>> next(it)
 # (Output)
 '''
 Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    next(it)
 StopIteration
'''
 ```

Setelah melihat mekanisme di balik protokol iterator, mudah untuk menambahkan perilaku iterator ke kelas. Tentukan metode ``__iter__()`` yang mengembalikan objek dengan metode ``__next__()``. Jika kelas mendefinisikan ``__next__()``, maka ``__iter__()`` hanya dapat mengembalikan ``self``. Contoh:
```python
 class Reverse:
    """Iterator untuk mengulang urutan mundur."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]
 ```

```python
 >>> rev = Reverse('spam')
 >>> iter(rev)
 <__main__.Reverse object at 0x00A1DB50>
 >>> for char in rev:
 ...     print(char)
 ...
 # (Output)
 '''
 m
 a
 p
 s
 '''
 ```

---

## 9.9. Generator / Generators

Generator melanjutkan di mana ia tinggalkan. dia mengingat semua nilai data dan pernyataan mana yang terakhir dieksekusi. Sebuah contoh menunjukkan bahwa generator dapat dengan mudah dibuat:
```python
 def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]
 ```

```python
 >>> for char in reverse('golf'):
 ...     print(char)
 ...
 # (Output)
 '''
 f
 l
 o
 g
 '''
 ```

**Penjelasan**:
Apa pun yang dapat dilakukan dengan generator juga dapat dilakukan dengan iterator berbasis kelas apa yang membuat generator begitu kompak adalah bahwa metode ``__iter__()`` dan ``__next__()`` dibuat secara otomatis. Fitur utama lainnya adalah variabel lokal dan status eksekusi secara otomatis disimpan di antara panggilan. Ini membuat fungsi lebih mudah untuk ditulis dan jauh lebih jelas daripada pendekatan yang menggunakan variabel instan seperti ``self.index`` dan ``self.data``.

---

## 9.10. Generator Ekspresi / Generator Expressions

Beberapa generator sederhana dapat dikodekan secara ringkas sebagai ekspresi menggunakan sintaks yang mirip dengan pemahaman daftar tetapi dengan tanda kurung alih-alih tanda kurung siku. Ekspresi ini dirancang untuk situasi di mana generator digunakan langsung oleh fungsi terlampir. Ekspresi generator lebih ringkas tetapi kurang fleksibel daripada definisi generator lengkap dan cenderung lebih ramah memori daripada pemahaman daftar yang setara. Contoh:
```python
 >>> sum(i*i for i in range(10))                 # jumlah kuadrat
 # 285 (Output)

 >>> xvec = [10, 20, 30]
 >>> yvec = [7, 5, 3]
 >>> sum(x*y for x,y in zip(xvec, yvec))         # produk titik
 # 260 (Output)

 >>> unique_words = set(word for line in page  for word in line.split())

 >>> valedictorian = max((student.gpa, student.name) for student in graduates)

 >>> data = 'golf'
 >>> list(data[i] for i in range(len(data)-1, -1, -1))
 # ['f', 'l', 'o', 'g'] (Output)
 ```

**Catatan Tambahan**:
Objek modul memiliki atribut read-only rahasia yang disebut dengan ``__dict__`` yang mengembalikan kamus yang digunakan untuk mengimplementasikan modul ruang nama. Nama ``__dict__`` adalah atribut tetapi bukan nama global dan jelas menggunakan hal tersebut melanggar abstraksi implementasi ruang nama, dan harus dibatasi untuk hal-hal seperti debugger post-mortem.