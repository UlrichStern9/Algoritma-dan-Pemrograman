"""
Nama: Muhammad Azka Aulia
NIM: 064001900026
"""

def mulai():
    while True:
        masuk = input("Elkom?: ")
        if masuk == "1":
            elkom1()
        elif masuk == "2":
            elkom2()
        elif masuk == "e":
            break
        else:
            print("Pilih 1 atau 2, e untuk keluar\n")


def elkom1():
    from math import sqrt

    sisi = input("Sisi mana yang Anda ingin hitung? (a,b,c): ")

    if sisi == "c":
        a = int(input("Masukkan panjang a: "))
        b = int(input("Masukkan panjang b: "))
        c = sqrt(a * a + b * b)
        print("Panjang sisi c adalah:", round(c))

    elif sisi == "a":
        b = int(input("Masukkan panjang b: "))
        c = int(input("Masukkan panjang c: "))
        if (c < b):
            print("Panjang c tidak valid!")
            c = int(input("Masukkan panjang c: "))

        a = sqrt(c * c - b * b)
        print("Panjang sisi a adalah:", round(a))

    elif sisi == "b":
        a = int(input("Masukkan panjang a: "))
        c = int(input("Masukkan panjang c: "))
        if (c < a):
            print("Panjang c tidak valid!")
            c = int(input("Masukkan panjang c: "))

        b = sqrt(c * c - a * a)
        print("Panjang sisi b adalah:", round(b))


def elkom2():
    pertama = int(input("Masukkan angka pertama: "))
    kedua = int(input("Masukkan angka kedua: "))
    ketiga = int(input("Masukkan angka ketiga: "))

    if (pertama > kedua) and (pertama > ketiga):
        terbesar = pertama

    elif (kedua > pertama) and (kedua > ketiga):
        terbesar = kedua

    else:
        terbesar = ketiga

    print("\nAngka terbesar adalah:", terbesar)


if __name__ == "__main__":
    mulai()
