# Visualisasi Data dengan Python
Ketika mempelajari data science, pastinya akan berurusan dengan data yang banyak. Tentunya akan kesusahan mendapatkan informasi jika melihat data atau tabel yang sangat panjang. Daripada melihat data baris per baris, maka dari itu bisa dilakukan dengan merepresentasikan data tersebut dengan grafik. Itulah yang dinamakan visualisasi data, menampilkan data-data kita dengan cara yang lebih menarik dan mudah dimengerti, seperti table, chart, ataupun bentuk lainnya sesuai keperluan.

---

## Membaca data dengan Pandas
Sebelum memvisualisasikan data dengan grafik, maka perlu membaca atau mengimport dataset terlebih dahulu. Langkah ini sangat simpel, namun sangat penting karena data yang akan divisualisasikan berasal dari langkah ini. Hal ini dapat dilakukan dengan mudah menggunakan library pandas (library untuk manipulasi data dan analisis) dengan mengetikkan kode berikut pada IDE.

```python
 import pandas as pd
 df = pd.read_csv('folder-project-kita/nama-dataset.csv', encoding='utf-8')
 # Mengubah Date dari format text ke format tanggal
 df['Date'] = pd.to_datetime(df['Date'])

 # (Output)
 '''
 Date	Abap	Ada	C/C++	C#	Cobol	Dart	Delphi/Pascal	Go	Groovy	...	PHP	Python	R	Ruby	Rust	Scala	Swift	TypeScript	VBA	Visual Basic
 0	2004-07-01	0.34	0.36	10.08	4.71	0.43	0.00	2.82	0.00	0.03	...	18.75	2. 53	0.39	0.33	0.08	0.03	0.00	0.00	1.44	8.56
 1	2004-08-01	0.36	0.36	9.81	4.99	0.46	0.00	2.67	0.00	0.07	...	19.26	2. 64	0.41	0.40	0.09	0.03	0.00	0.00	1.46	8.57
 2	2004-09-01	0.41	0.41	9.63	5.06	0.51	0.00	2.65	0.00	0.08	...	19.49	2. 72	0.40	0.41	0.10	0.03	0.00	0.00	1.55	8.41
 3	2004-10-01	0.40	0.38	9.50	5.31	0.53	0.00	2.77	0.00	0.09	...	19.34	2. 92	0.42	0.46	0.11	0.04	0.00	0.00	1.61	8.49
 4	2004-11-01	0.38	0.38	9.52	5.24	0.55	0.00	2.76	0.00	0.07	...	19.43	2. 84	0.41	0.45	0.13	0.04	0.00	0.00	1.50	8.24
 ...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...
 206	2021-09-01	0.50	0.55	6.68	7.17	0.35	0.58	0.00	1.57	0.47	...	6.37	30. 11	3.93	1.01	0.77	0.49	1.64	1.59	1.27	0.72
 207	2021-10-01	0.53	0.57	6.99	7.38	0.33	0.55	0.00	1.54	0.52	...	6.28	30. 14	3.73	0.98	0.74	0.49	1.61	1.59	1.28	0.75
 208	2021-11-01	0.61	0.70	6.99	7.31	0.35	0.61	0.00	1.42	0.52	...	6.19	30. 05	3.80	1.00	0.82	0.54	1.70	1.63	1.37	0.76
 209	2021-12-01	0.70	0.67	7.01	7.26	0.33	0.65	0.00	1.35	0.49	...	6.24	29. 60	4.11	1.03	0.84	0.55	1.64	1.66	1.25	0.71
 210	2022-01-01	0.66	0.75	7.40	7.27	0.30	0.72	0.00	1.19	0.48	...	6.06	28. 74	4.19	1.07	0.98	0.48	1.91	1.74	1.14	0.64
 211 rows × 29 columns
 '''
 ```

dengan kode di atas, kita sudah mengimport dataset kita ke dalam varabel df.

---
## Visualisasi menggunakan Matplotlib
Dengan banyaknya library yang ada sekarang, visualisasi data menjadi mudah. Library yang digunakan yaitu Matplotlib, salah satu library visualisasi yang paling sering digunakan. Kita dapat membuat grafik dengan sangat mudah menggunakan Matplotlib. Kita hanya perlu megimport pyplot dari matplotlib, dan memanggil fungsi ``plt.plot``. ``plt.plot`` membutuhkan minimal 2 input, yaitu axis nya, input pertama merupakan axis horizontal, dan input kedua vertikal. Axis inilah yang akan digunakan untuk memetakan data kita menjadi grafik. Kita dapat menentukan axis yang mau kita gunakan dengan melihat judul kolom-kolom data kita, dan memangginal dengan ``df['judu kolom']``.

```python
 import matplotlib.pyplot as plt
 plt.plot(df['Date'], df['Python'])

 # (Output)
 '''
 [<matplotlib.lines.Line2D at 0x176a6a56f10>]

 '''
 ```

Dengan grafik ini, kita bisa melihat perkembangan popularitas python dari tahun ke tahun. Selanjutnya yang dilakukan membandingkan beberapa bahasa dalam 1 grafik, dan menambahkan informasi untuk membantu memahami grafik.

```python
 # Merepresentasikan data menjadi garis linear dalam grafik
 # Label berfungsi agar dapat dikenali legends
 plt.plot(df['Date'], df['Python'], label='Python')
 plt.plot(df['Date'], df['JavaScript'], label='JavaScript')
 plt.plot(df['Date'], df['Kotlin'], label='Kotlin')
 plt.plot(df['Date'], df['Swift'], label='Swift')

 plt.xlabel('Tahun') # Informasi teks untuk axis horizontal
 plt.ylabel('Popularitas (%)') # Informasi teks untuk axis vertikal
 plt.title('Perkembangan popularitas bahasa pemrograman') # Judul
 plt.grid(True) # Garis background untuk mempermudah pembacaan
 plt.legend() # Informasi warna garis

 # (Output)
 '''
 <matplotlib.legend.Legend at 0x176a9e2d4c0>

 '''
 ```

Selanjutnya yang dilakukan adalah menampilkan grafik lain dalam bentuk Histogram
```python
 plt.hist(df['Python'])
 
 # (Output)
 '''
 (array([51., 51., 32., 14.,  8.,  7.,  6.,  7., 11., 24.]),
 array([ 2.53 ,  5.488,  8.446, 11.404, 14.362, 17.32 , 20.278, 23.236,
        26.194, 29.152, 32.11 ]),
 <BarContainer object of 10 artists>)

 '''
 ```

---
## Kesimpulan
Ketika mempelajari data science tentunya akan ditemukan data yang sangat banyak, sehingga kita akan kesulitan mendapatkan informasi jika kita melihat data yang banyak. Sehingga kita harus bisa merepresentasikan data tersebut dengan mudah yaitu dengan grafik, inilah yang dinamakan visualisasi data, menampilkan data yang sangat banyak dengan cara yang lebih menarik dan mudah dimengerti, seperti tabel, chart, ataupun bentuk lain sesuai keperluan. Salah satu cara untuk memvisualisasi data tersebut yaitu dengan Python. Python adalah suatu bahasa pemrograman untuk tujuan umum untuk mempermudah penafsiran dan dibuat oleh Guido van Rossum dan pertama kali dirilis pada tahun 1991. Python salah satu bahasa pemrograman yang cocok digunakan dalam jenis kepentingan website, pengembangan aplikasi, dan masih banyak kegunaan lainnya.