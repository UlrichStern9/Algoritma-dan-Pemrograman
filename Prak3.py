"""
Nama: Muhammad Azka Aulia
NIM: 064001900026
"""


def mulai():
    while True:
        masuk = input("\nElkom?: ")
        if masuk == "1":
            elkom1()
        elif masuk == "2":
            elkom2()
        elif masuk == "e":
            break
        else:
            print("Pilih 1 atau 2, e untuk keluar\n")


def elkom1():
    masuk = [int(input("Masukkan angka awal: ")), int(input("Masukkan angka akhir: "))]
    while masuk[0] and masuk[0] <= masuk[1]:
        print(masuk[0], masuk[1])
        masuk[0] += 1
        masuk[1] -= 1


def elkom2():
    total = int(input("Masukkan total harga belanjaan Anda: Rp. "))
    bayar = int(input("Masukkan jumlah uang Anda: Rp. "))
    kembalian = bayar - total
    uang_pecahan = [100000, 50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100]
    sisa = kembalian
    print("\nKembalian Anda sejumlah: Rp.", kembalian, "\nPecahan uang yang dibutuhkan: ")
    for pecahan in uang_pecahan:
        if sisa < pecahan:
            continue
        banyak_pecahan = int(sisa / pecahan)
        sisa = sisa - (pecahan * banyak_pecahan)
        print("Uang kertas Rp. {} sebanyak {} lembar".format(pecahan, banyak_pecahan))



if __name__ == "__main__":
    mulai()
