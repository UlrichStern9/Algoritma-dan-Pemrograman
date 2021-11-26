"""
Nama: Muhammad Azka Aulia
NIM: 064001900026
"""


def mulai():
    while True:
        masuk = input("Elkom?: ")
        if masuk == "1":
            elkom1()
        elif masuk == "3":
            elkom3()
        elif masuk == "e":
            break
        else:
            print("Pilih 1, 2 atau 3, e untuk keluar\n")


def elkom1():
    def konversi(list):
        return tuple(i for i in list)

    print("List:", list, "\n" + "Hasil reverse list menjadi tuple:", konversi([3, 15, 4, 7, 10, 5]), "\n")


def elkom3():
    def perkalianlist(listku):
        hasil = 1
        for x in listku:
            hasil = hasil * x
        print("List:", listku)
        print("Hasil kali value list:", hasil, "\n")

    perkalianlist([-5, 7, -10])


if __name__ == "__main__":
    mulai()
