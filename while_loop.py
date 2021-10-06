"""
Nama: Muhammad Azka Aulia
NIM: 064001900026
"""

masuk = [int(input("Masukkan angka awal: ")), int(input("Masukkan angka akhir: "))]

while masuk[0] and masuk[0] <= masuk[1]:
    print(masuk[0], masuk[1])
    masuk[0] += 1
    masuk[1] -= 1
