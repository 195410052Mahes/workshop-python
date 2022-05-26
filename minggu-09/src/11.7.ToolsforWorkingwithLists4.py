from heapq import heapify, heappop, heappush
data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
heapify(data)                      # atur ulang daftar menjadi urutan tumpukan
heappush(data, -5)                 # tambahkan entri baru
[heappop(data) for i in range(3)]  # ambil tiga entri terkecil
# [-5, 0, 1] (Output)