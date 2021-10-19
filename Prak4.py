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
    while True:
        pilihan = int(input(
            "---PROGRAM KONVERSI BILANGAN---\n1 -> Desimal ke biner\n2 -> Biner ke desimal\n3 -> Keluar\nSilakan pilih menu: "))

        if pilihan == 1:
            bilangan = int(input("Masukkan bilangan desimal: "))

            hasil = ""
            while bilangan != 0:
                sisa = bilangan % 2
                bilangan = bilangan // 2
                hasil = str(sisa) + hasil
            print("Nilai binernya adalah: ", hasil, "\n")

        if pilihan == 2:
            biner = int(input("Masukkan bilangan biner: "))

            desimal = 0
            i = 1
            while biner != 0:
                sisa = biner % 10
                desimal = desimal + (sisa * i)
                i = i * 2
                biner = int(biner / 10)

            print("Nilai desimalnya adalah: ", desimal, "\n")

        if pilihan == 3:
            print("Terima kasih telah menggunakan program ini!")
            break

        else:
            print("Pilih 1, 2 atau 3")


def elkom2():
    masuk = list(map(int, input("Isi list angka (integer): ").strip().split()))

    genap = 0

    for angka in masuk:
        if angka % 2 == 0:
            genap += 1

    if genap > 0:
        print("List angka memiliki angka genap")
    else:
        print("List angka tidak memiliki angka genap")


if __name__ == "__main__":
    mulai()
