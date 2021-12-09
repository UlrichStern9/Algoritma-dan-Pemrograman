"""
Nama: Muhammad Azka Aulia
NIM: 064001900026
"""

memenuhi = 0


def mulai():
    while True:
        masuk = input("Elkom?: ")
        if masuk == "1":
            elkom1()
        elif masuk == "2":
            elkom2()
        elif masuk == "3":
            elkom3()
        elif masuk == "4":
            elkom4()
        elif masuk == "e":
            break
        else:
            print("Pilih 1, 2, 3 atau 4, e untuk keluar\n")


def elkom1():
    def konversi(listku):
        return tuple(i for i in listku)

    print("List:", list, "\n" + "Hasil reverse list menjadi tuple:", konversi([3, 15, 4, 7, 10, 5]), "\n")


def elkom2():
    def rerata(tupleku):
        print("Tuple1:\n" + str(tupleku) + "\n")
        return [sum(i) / len(i) for i in zip(*tupleku)]

    print("Rerata nilai pada masing-masing tuple:\n" + str(
        rerata(((5, 77, 19, 32), (99, 21, 43, 39), (64, 37, 20, 26), (5, 7, 2, 10)))), "\n")


def elkom3():
    def perkalianlist(listku):
        hasil = 1
        for x in listku:
            hasil = hasil * x
        print("List:", listku)
        print("Hasil kali value list:", hasil, "\n")

    perkalianlist([-5, 7, -10])


def elkom4():
    global memenuhi

    def stringyangsama(listku):
        print("List string:", str(listku))
        global memenuhi
        for satuan in listku:
            pertama = satuan[0]
            terakhir = satuan[len(satuan) - 1]

            if pertama == terakhir:
                print("-", satuan)
                memenuhi += 1

    stringyangsama(['racecar', '2012', 'hujan', 'kasurusak', '747', 'string'])
    print("Terdapat {} string yang memenuhi kriteria".format(memenuhi), "\n")


if __name__ == "__main__":
    mulai()
