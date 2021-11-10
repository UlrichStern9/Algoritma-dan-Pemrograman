"""
Nama: Muhammad Azka Aulia
NIM: 064001900026
"""


def faktorial(angka):
    if angka > 2:
        return angka * faktorial(angka - 1)
    return 2


masuk = int(input("PROGRAM MENCARI NILAI FAKTORIAL DARI SEBUAH ANGKA\nMasukkan angka: "))
print("Nilai faktorialnya adalah:", faktorial(masuk))
