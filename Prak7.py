"""
Nama: Muhammad Azka Aulia
NIM: 064001900026
"""
vokal = 0
konsonan = 0


def mulai():
    while True:
        masuk = input("Elkom?: ")
        if masuk == "1":
            elkom1()
        elif masuk == "2":
            elkom2()
        elif masuk == "3":
            elkom3()
        elif masuk == "e":
            break
        else:
            print("Pilih 1, 2 atau 3, e untuk keluar\n")


def elkom1():
    def faktorial(angka):
        if angka > 2:
            return angka * faktorial(angka - 1)
        return 2

    masuk = int(input("PROGRAM MENCARI NILAI FAKTORIAL DARI SEBUAH ANGKA\nMasukkan angka: "))
    print("Nilai faktorialnya adalah:", faktorial(masuk), "\n")


def elkom2():
    global vokal, konsonan
    daftar_vokal = ["a", "i", "u", "e", "o"]

    print("PROGRAM MENGHITUNG HURUF VOKAL DAN KONSONAN DARI KALIMAT")

    masuk = str(input("Masukkan kalimat: ")).lower()

    def hitung(angka):
        global vokal, konsonan
        for huruf in angka:
            if huruf in daftar_vokal:
                vokal += 1
            else:
                konsonan += 1

    hitung(masuk)

    print("Jumlah huruf vokal adalah ", vokal)
    print("Jumlah huruf konsonan adalah ", konsonan, "\n")


def elkom3():
    print("PROGRAM PENGECEKAN BILANGAN")

    while True:
        masuk = input("Masukkan bilangan, kosongkan jika ingin keluar: ")

        if masuk == "":
            print("")
            break

        def pangkatkan(angka):
            return angka ** 3

        def cek_modulo(angka):
            if angka % 3 == 0:
                return True
            else:
                return False

        hasil = cek_modulo(int(masuk))

        if hasil is True:
            print("Hasil:", pangkatkan(int(masuk)), "\n")
        else:
            print("Hasil:", hasil, "\n")


if __name__ == "__main__":
    mulai()
