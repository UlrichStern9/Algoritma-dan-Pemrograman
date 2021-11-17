"""
Nama: Muhammad Azka Aulia
NIM: 064001900026
"""

masuk = input("PROGRAM MEMUNCULKAN KARAKTER INDEKS GANJIL\nMasukkan sebuah kata: ")


def indeks_ganjil(huruf):
    list_huruf = []
    for index in range(1, len(huruf), 2):
        list_huruf.append(huruf[index])
    return "".join(list_huruf)


print("Karakter indeks ganjil:", indeks_ganjil(masuk))
