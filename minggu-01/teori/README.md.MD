3. Pengantar Informal untuk Python

Dalam contoh berikut, input dan output dibedakan dengan ada atau tidaknya prompt (>>> dan ...): untuk mengulang contoh, Anda harus mengetikkan semuanya setelah prompt, ketika prompt muncul; baris yang tidak dimulai dengan prompt adalah output dari interpreter. Perhatikan bahwa perintah sekunder pada baris dengan sendirinya dalam contoh berarti Anda harus mengetikkan baris kosong; ini digunakan untuk mengakhiri perintah multi-baris.

Anda dapat mengaktifkan tampilan prompt dan output dengan mengklik ">>>" di sudut kanan atas kotak contoh. Jika Anda menyembunyikan perintah dan output sebagai contoh, maka Anda dapat dengan mudah menyalin dan menempelkan baris input ke penerjemah Anda.

Banyak contoh dalam manual ini, bahkan yang dimasukkan pada prompt interaktif, termasuk komentar. Komentar dalam Python dimulai dengan karakter hash, #, dan diperpanjang hingga akhir baris fisik. Sebuah komentar mungkin muncul di awal baris atau setelah spasi atau kode, tetapi tidak dalam literal string. Karakter hash dalam string literal hanyalah karakter hash. Karena komentar adalah untuk memperjelas kode dan tidak ditafsirkan oleh Python, komentar tersebut dapat dihilangkan saat mengetikkan contoh.

Banyak contoh dalam manual ini, bahkan yang dimasukkan pada prompt interaktif, termasuk komentar. Komentar dalam Python dimulai dengan karakter hash, #, dan diperpanjang hingga akhir baris fisik. Sebuah komentar mungkin muncul di awal baris atau setelah spasi atau kode, tetapi tidak dalam literal string. Karakter hash dalam string literal hanyalah karakter hash. Karena komentar adalah untuk memperjelas kode dan tidak ditafsirkan oleh Python, komentar tersebut dapat dihilangkan saat mengetikkan contoh.

Beberapa contoh:
#ini adalah komentar pertama
spam = 1 # dan ini adalah komentar kedua
          # ... dan sekarang yang ketiga!
text = "# Ini bukan komentar karena ada di dalam tanda kutip."

3.1. Menggunakan Python sebagai Kalkulator

Mari kita coba beberapa perintah Python sederhana. Jalankan interpreter dan tunggu prompt utama, >>>. (Seharusnya tidak butuh waktu lama.)

3.1.1. Nomor

Penerjemah bertindak sebagai kalkulator sederhana: Anda dapat mengetikkan ekspresi padanya dan itu akan menulis nilainya. Sintaks ekspresi sangat mudah: operator +, -, * dan / bekerja seperti kebanyakan bahasa lain (misalnya, Pascal atau C); tanda kurung (()) dapat digunakan untuk pengelompokan. Sebagai contoh:
>>> 2 + 2
4
>>> 50 - 5*6
20
>>> (50 - 5*6) / 4
5.0
>>> 8 / 5 # divisi selalu mengembalikan angka floating point
1.6

Bilangan bulat (misalnya 2, 4, 20) memiliki tipe int, yang dengan bagian pecahan (misalnya 5.0, 1.6) memiliki tipe float. Kita akan melihat lebih banyak tentang tipe numerik nanti di tutorial.

Divisi (/) selalu mengembalikan float. Untuk melakukan pembagian lantai dan mendapatkan hasil bilangan bulat (membuang hasil pecahan apa pun), Anda dapat menggunakan operator //; untuk menghitung sisanya, Anda dapat menggunakan %:
>>> 17 / 3 # divisi klasik mengembalikan float
5.66666666666666667
>>>
>>> 17 // 3 # pembagian lantai membuang bagian pecahan
5
>>> 17 % 3 # operator % mengembalikan sisa pembagian
2
>>> 5 * 3 + 2 # hasil bagi berlantai * pembagi + sisa
17

Dengan Python, dimungkinkan untuk menggunakan operator ** untuk menghitung pangkat 1:
>>> 5 ** 2 # 5 kuadrat
25
>>> 2 ** 7 # 2 pangkat 7
128

Tanda sama dengan (=) digunakan untuk memberikan nilai pada variabel. Setelah itu, tidak ada hasil yang ditampilkan sebelum prompt interaktif berikutnya:
>>> lebar = 20
>>> tinggi = 5 * 9
>>> lebar * tinggi
900

Jika suatu variabel tidak "didefinisikan" (diberi nilai), mencoba menggunakannya akan memberi Anda kesalahan:
>>> n # coba akses variabel yang tidak ditentukan
Traceback (panggilan terakhir terakhir):
  File "<stdin>", baris 1, di <module>
NameError: nama 'n' tidak ditentukan

Ada dukungan penuh untuk floating point; operator dengan operan tipe campuran mengubah operan integer menjadi floating point:
>>> 4 * 3.75 - 1
14.0

Dalam mode interaktif, ekspresi tercetak terakhir ditetapkan ke variabel _. Ini berarti bahwa ketika Anda menggunakan Python sebagai kalkulator meja, akan lebih mudah untuk melanjutkan perhitungan, misalnya:
>>> pajak = 12,5 / 100
>>> harga = 100.50
>>> harga * pajak
12.5625
>>> harga + _
113.0625
>>> round(_, 2)
113.06

Variabel ini harus diperlakukan sebagai hanya-baca oleh pengguna. Jangan secara eksplisit memberikan nilai padanya — Anda akan membuat variabel lokal independen dengan nama yang sama menutupi variabel bawaan dengan perilaku ajaibnya.

Selain int dan float, Python mendukung jenis angka lain, seperti Desimal dan Pecahan. Python juga memiliki dukungan bawaan untuk bilangan kompleks, dan menggunakan akhiran j atau J untuk menunjukkan bagian imajiner (mis. 3+5j).

3.1.2. Strings

Selain angka, Python juga dapat memanipulasi string, yang dapat diekspresikan dalam beberapa cara. Mereka dapat diapit dalam tanda kutip tunggal ('...') atau tanda kutip ganda ("...") dengan hasil yang sama 2. \ dapat digunakan untuk menghindari tanda kutip:
>>> 'telur spam' # tanda kutip tunggal
'telur spam'
>>> 'tidak' # menggunakan \' untuk menghindari kutipan tunggal...
"tidak"
>>> "tidak" # ...atau gunakan tanda kutip ganda sebagai gantinya
"tidak"
>>> '"Ya," kata mereka.'
'"Ya," kata mereka.'
>>> "\"Ya,\" kata mereka."
'"Ya," kata mereka.'
>>> '"Tidak," kata mereka.'
'"Bukan," kata mereka.'

n interpreter interaktif, string keluaran diapit oleh tanda kutip dan karakter khusus diloloskan dengan garis miring terbalik. Meskipun ini terkadang terlihat berbeda dari input (tanda kutip terlampir dapat berubah), kedua string tersebut setara. String diapit dalam tanda kutip ganda jika string berisi tanda kutip tunggal dan tidak ada tanda kutip ganda, selain itu diapit dalam tanda kutip tunggal. Fungsi print() menghasilkan keluaran yang lebih mudah dibaca, dengan menghilangkan tanda kutip terlampir dan dengan mencetak karakter khusus dan karakter khusus:
>>> '"Tidak," kata mereka.'
'"Bukan," kata mereka.'
>>> print('"Tidak," kata mereka.')
"Bukan," kata mereka.
>>> s = 'Baris pertama.\nBaris kedua.' # \n artinya baris baru
>>> s # tanpa print(), \n disertakan dalam output
'Baris pertama.\nBaris kedua.'
>>> print(s) # dengan print(), \n menghasilkan baris baru
Garis pertama.
Baris kedua.

Jika Anda tidak ingin karakter yang diawali dengan \ ditafsirkan sebagai karakter khusus, Anda dapat menggunakan string mentah dengan menambahkan r sebelum kutipan pertama:
>>> print('C:\some\name') # di sini \n berarti baris baru!
C:\beberapa
ame
>>> print(r'C:\some\name') # perhatikan r sebelum kutipan
C:\beberapa\nama

String literal dapat menjangkau beberapa baris. Salah satu caranya adalah dengan menggunakan tanda kutip tiga: """...""" atau '''...'''. Akhir baris secara otomatis disertakan dalam string, tetapi Anda dapat mencegahnya dengan menambahkan \ di akhir baris. Contoh berikut:
mencetak("""\
Penggunaan: thingy [OPTIONS]
     -h Tampilkan pesan penggunaan ini
     -H hostname Hostname untuk terhubung ke
""")

menghasilkan output berikut (perhatikan bahwa baris baru awal tidak termasuk):
Penggunaan: thingy [OPTIONS]
     -h Tampilkan pesan penggunaan ini
     -H hostname Hostname untuk terhubung ke
    
String dapat digabungkan (direkatkan) dengan operator +, dan diulang dengan *:
>>> # 3 kali 'un', diikuti oleh 'ium'
>>> 3 * 'un' + 'ium'
'unununium'

Dua atau lebih literal string (yaitu yang terlampir di antara tanda kutip) di samping satu sama lain secara otomatis digabungkan.
>>> 'Py' 'thon'
'Python'

Fitur ini sangat berguna ketika Anda ingin memutuskan senar yang panjang:
>>> text = ('Letakkan beberapa string di dalam tanda kurung '
... 'agar mereka bergabung bersama.')
>>> text
'Letakkan beberapa string dalam tanda kurung agar mereka bergabung bersama.'

Ini hanya berfungsi dengan dua literal, tidak dengan variabel atau ekspresi:
>>> awalan = 'Py'
>>> awalan 'thon' # tidak dapat menggabungkan variabel dan string literal
  File "<stdin>", baris 1
    awalan 'thon'
                ^
SyntaxError: sintaks tidak valid
>>> ('un' * 3) 'ium'
  File "<stdin>", baris 1
    ('un' * 3) 'ium'
                   ^
SyntaxError: sintaks tidak valid

jika Anda ingin menggabungkan variabel atau variabel dan literal, gunakan +:
>>> prefix + 'thon'
'Python'

String dapat diindeks (berlangganan), dengan karakter pertama memiliki indeks 0. Tidak ada tipe karakter terpisah; karakter hanyalah string ukuran satu:
>>> kata = 'Python'
>>> kata[0] # karakter di posisi 0
'P'
>>> kata[5] # karakter di posisi 5
'n'

Indeks juga bisa berupa angka negatif, untuk mulai menghitung dari kanan:
>>> kata[-1] # karakter terakhir
'n'
>>> kata[-2] # karakter kedua-terakhir
'o'
>>> kata[-6]
'P'

Perhatikan bahwa karena -0 sama dengan 0, indeks negatif dimulai dari -1.

Selain pengindeksan, pengirisan juga didukung. Sementara pengindeksan digunakan untuk mendapatkan karakter individu, slicing memungkinkan Anda untuk mendapatkan substring:
>>> kata[0:2] # karakter dari posisi 0 (termasuk) hingga 2 (tidak termasuk)
'Py'
>>> kata[2:5] # karakter dari posisi 2 (termasuk) hingga 5 (tidak termasuk)
'tho'

Indeks irisan memiliki default yang berguna; indeks pertama yang dihilangkan defaultnya adalah nol, indeks kedua yang dihilangkan defaultnya adalah ukuran string yang diiris.
>>> kata[:2] # karakter dari awal hingga posisi 2 (dikecualikan)
'Py'
>>> kata[4:] # karakter dari posisi 4 (termasuk) hingga akhir
'on'
>>> kata[-2:] # karakter dari yang kedua-terakhir (termasuk) sampai akhir
'on'

Perhatikan bagaimana awal selalu disertakan, dan akhir selalu dikecualikan. Ini memastikan bahwa s[:i] + s[i:] selalu sama dengan s:
>>> kata[:2] + kata[2:]
'Python'
>>> kata[:4] + kata[4:]
'Python'

Salah satu cara untuk mengingat cara kerja irisan adalah dengan menganggap indeks sebagai penunjuk antar karakter, dengan tepi kiri karakter pertama bernomor 0. Kemudian tepi kanan karakter terakhir dari string n karakter memiliki indeks n, misalnya:
+---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1

Baris pertama angka memberikan posisi indeks 0…6 dalam string; baris kedua memberikan indeks negatif yang sesuai. Irisan dari i ke j terdiri dari semua karakter antara tepi berlabel i dan j, masing-masing.

Untuk indeks non-negatif, panjang irisan adalah selisih indeks, jika keduanya berada dalam batas. Misalnya, panjang kata[1:3] adalah 2.

Mencoba menggunakan indeks yang terlalu besar akan menghasilkan kesalahan:
>>> kata[42] # kata hanya memiliki 6 karakter
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range

Namun, indeks irisan di luar jangkauan ditangani dengan anggun saat digunakan untuk mengiris:
>>> kata[4:42]
'on'
>>> kata[42:]
''

String Python tidak dapat diubah — mereka tidak dapat diubah. Oleh karena itu, menetapkan ke posisi yang diindeks dalam string menghasilkan kesalahan:
>>> kata[0] = 'J'
Traceback (most recent call last):
 File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
>>> kata[2:] = 'py'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment

Jika Anda membutuhkan string yang berbeda, Anda harus membuat yang baru:
>>> 'J' + kata[1:]
'Jython'
>>> kata[:2] + 'py'
'Pypy'

Fungsi bawaan len() mengembalikan panjang string:
>>> s = 'supercalifragilisticexpialidocious'
>>> len(s)
34

3.1.3. Lists

Python mengetahui sejumlah tipe data gabungan, yang digunakan untuk mengelompokkan nilai-nilai lain. Yang paling serbaguna adalah daftar, yang dapat ditulis sebagai daftar nilai (item) yang dipisahkan koma di antara tanda kurung siku. Daftar mungkin berisi item dari jenis yang berbeda, tetapi biasanya semua item memiliki jenis yang sama.
>>> squares = [1, 4, 9, 16, 25]
>>> squares
[1, 4, 9, 16, 25]

Seperti string (dan semua jenis urutan bawaan lainnya), daftar dapat diindeks dan diiris:
>>> squares[0]  # indexing mengembalikan item
1
>>> squares[-1]
25
>>> squares[-3:]  # mengiris mengembalikan daftar baru
[9, 16, 25]

Semua operasi irisan mengembalikan daftar baru yang berisi elemen yang diminta. Ini berarti bahwa irisan berikut mengembalikan salinan daftar yang dangkal:
>>> squares[:]
[1, 4, 9, 16, 25]

Daftar juga mendukung operasi seperti penggabungan:
>>> squares + [36, 49, 64, 81, 100]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

Tidak seperti string, yang tidak dapat diubah, daftar adalah jenis yang dapat diubah, yaitu kontennya dapat diubah:
>>> cubes = [1, 8, 27, 65, 125]  # ada yang salah disini
>>> 4 ** 3  # pangkat tiga dari 4 adalah 64, bukan 65!
64
>>> cubes[3] = 64  # ganti nilai yang salah
>>> cubes
[1, 8, 27, 64, 125]

Anda juga dapat menambahkan item baru di akhir daftar, dengan menggunakan metode append() (kita akan melihat lebih banyak tentang metode nanti):
>>> cubes.append(216)  # tambahkan kubus 6
>>> cubes.append(7 ** 3)  # tambahkan kubus 7
>>> cubes
[1, 8, 27, 64, 125, 216, 343]

Penetapan irisan juga dimungkinkan, dan ini bahkan dapat mengubah ukuran daftar atau menghapusnya seluruhnya:
>>> letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> letters
['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> # ganti beberapa nilai
>>> letters[2:5] = ['C', 'D', 'E']
>>> letters
['a', 'b', 'C', 'D', 'E', 'f', 'g']
>>> # sekarang hapus
>>> letters[2:5] = []
>>> letters
['a', 'b', 'f', 'g']
>>> # hapus daftar dengan mengganti semua elemen dengan daftar kosong
>>> letters[:] = []
>>> letters
[]

Fungsi bawaan len() juga berlaku untuk daftar:
>>> letters = ['a', 'b', 'c', 'd']
>>> len(letters)
4

ini memungkinkan untuk membuat daftar bersarang (membuat daftar yang berisi daftar lain), misalnya:
>>> a = ['a', 'b', 'c']
>>> n = [1, 2, 3]
>>> x = [a, n]
>>> x
[['a', 'b', 'c'], [1, 2, 3]]
>>> x[0]
['a', 'b', 'c']
>>> x[0][1]
'b'

3.2. First Steps Towards Programming
Tentu saja, kita dapat menggunakan Python untuk tugas yang lebih rumit daripada menambahkan dua dan dua secara bersamaan. Misalnya, kita dapat menulis sub-urutan awal dari deret Fibonacci sebagai berikut:
>>> # deret fibonacci:
... # jumlah dua elemen mendefinisikan yang berikutnya
... a, b = 0, 1
>>> while a < 10:
...     print(a)
...     a, b = b, a+b
...
0
1
1
2
3
5
8

Contoh ini memperkenalkan beberapa fitur baru.
Baris pertama berisi beberapa penugasan: variabel a dan b secara bersamaan mendapatkan nilai baru 0 dan 1. Pada baris terakhir ini digunakan lagi, menunjukkan bahwa ekspresi di sisi kanan semuanya dievaluasi terlebih dahulu sebelum penugasan apa pun terjadi. Ekspresi sisi kanan dievaluasi dari kiri ke kanan.

Perulangan while dijalankan selama kondisi (di sini: a < 10) tetap benar. Dalam Python, seperti di C, semua nilai integer bukan nol adalah benar; nol salah. Kondisi juga dapat berupa string atau nilai daftar, bahkan urutan apa pun; apa pun dengan panjang bukan nol adalah benar, urutan kosong adalah salah. Tes yang digunakan dalam contoh adalah perbandingan sederhana. Operator pembanding standar ditulis sama seperti pada C: < (kurang dari), > (lebih besar dari), == (sama dengan), <= (kurang dari atau sama dengan), >= (lebih besar atau sama dengan) dan != (tidak sama dengan).

Tubuh loop diindentasi: lekukan adalah cara Python mengelompokkan pernyataan. Pada prompt interaktif, Anda harus mengetikkan tab atau spasi untuk setiap baris indentasi. Dalam praktiknya Anda akan menyiapkan input yang lebih rumit untuk Python dengan editor teks; semua editor teks yang layak memiliki fasilitas auto-indent. Ketika pernyataan majemuk dimasukkan secara interaktif, itu harus diikuti oleh baris kosong untuk menunjukkan penyelesaian (karena parser tidak dapat menebak kapan Anda telah mengetik baris terakhir). Perhatikan bahwa setiap baris dalam blok dasar harus diindentasi dengan jumlah yang sama.

Fungsi print() menulis nilai argumen yang diberikan. Ini berbeda dari hanya menulis ekspresi yang ingin Anda tulis (seperti yang kita lakukan sebelumnya dalam contoh kalkulator) dalam cara menangani banyak argumen, jumlah floating point, dan string. String dicetak tanpa tanda kutip, dan spasi disisipkan di antara item, sehingga Anda dapat memformat sesuatu dengan baik, seperti ini:
>>> i = 256*256
>>> print('The value of i is', i)
The value of i is 65536

Argumen kata kunci end dapat digunakan untuk menghindari baris baru setelah output, atau mengakhiri output dengan string yang berbeda:
>>> a, b = 0, 1
>>> while a < 1000:
...     print(a, end=',')
...     a, b = b, a+b
...
0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,

Catatan 
Karena ** memiliki prioritas lebih tinggi daripada -, -3**2 akan ditafsirkan sebagai -(3**2) dan dengan demikian menghasilkan -9. Untuk menghindari ini dan mendapatkan 9, Anda dapat menggunakan (-3)**2.

Tidak seperti bahasa lain, karakter khusus seperti \n memiliki arti yang sama dengan tanda kutip tunggal ('...') dan ganda ("..."). Satu-satunya perbedaan antara keduanya adalah bahwa dalam tanda kutip tunggal Anda tidak perlu melarikan diri " (tetapi Anda harus melarikan diri \') dan sebaliknya.