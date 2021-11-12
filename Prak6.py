"""
Nama: Muhammad Azka Aulia
NIM: 064001900026
"""

PI = 3.141592653589793238


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
    print("MENGHITUNG KECEPATAN AKHIR GLBB (diketahui jarak tempuh)")
    v0 = int(input("Masukkan v0: "))
    a = int(input("Masukkan a: "))
    s = int(input("Masukkan s: "))

    def vt(kec_awal, percepatan, jarak):
        return (kec_awal ** 2 + (2 * percepatan * jarak)) ** (1 / 2)

    vt = vt(v0, a, s)

    print("Jarak tempuh jika kecepatan awal:", v0, "percepatan:", a, "dan jarak tempuh:", s, "adalah:", vt)


def elkom2():
    def kubus():
        masuk = int(input("Masukkan nilai rusuk: "))
        print("Luas permukaan kubus dengan rusuk", masuk, "adalah", hitung_kubus(masuk), "\n")

    def hitung_kubus(rusuk):
        return rusuk ** 2 * 6

    def balok():
        masuk1, masuk2, masuk3 = int(input("Masukkan nilai panjang: ")), int(input("Masukkan nilai lebar: ")), int(
            input("Masukkan nilai tinggi: "))
        print("Luas permukaan balok dengan panjang {}, lebar {} dan tinggi {} " "adalah".format(masuk1, masuk2, masuk3),
              hitung_balok(masuk1, masuk2, masuk3), "\n")

    def hitung_balok(panjang, lebar, tinggi):
        return panjang * tinggi * 2 + panjang * lebar * 2 + tinggi * lebar * 2

    def tabung():
        masuk1, masuk2 = int(input("Masukkan nilai jari-jari: ")), int(input("Masukkan nilai tinggi: "))
        print("Luas permukaan tabung dengan jari-jari {} dan tinggi {} " "adalah".format(masuk1, masuk2),
              hitung_tabung(masuk1, masuk2, PI), "\n")

    def hitung_tabung(jari2, tinggi, pi):
        return 2 * pi * jari2 * (tinggi + jari2)

    def kerucut():
        masuk1, masuk2 = int(input("Masukkan nilai jari-jari: ")), int(input("Masukkan nilai garis lukis: "))
        print("Luas permukaan kerucut dengan jari-jari {} dan garis lukis {} " "adalah".format(masuk1, masuk2),
              hitung_kerucut(masuk1, masuk2, PI), "\n")

    def hitung_kerucut(jari2, garis_lukis, pi):
        return pi * jari2 ** 2 + pi * jari2 * garis_lukis

    def bola():
        masuk1 = int(input("Masukkan nilai jari-jari: "))
        print("Luas permukaan bola dengan jari-jari {} " "adalah".format(masuk1), hitung_bola(masuk1, PI), "\n")

    def hitung_bola(jari2, pi):
        return 4 * pi * (jari2 * jari2)

    while True:
        print("KALKULATOR LUAS PERMUKAAN BANGUN RUANG\n1. Kubus\n2. Balok\n3. Tabung\n4. Kerucut\n5. Bola\n6. Exit")
        pilihan = input("Pilih menu yang tersedia: ")
        if pilihan == "1":
            kubus()
        elif pilihan == "2":
            balok()
        elif pilihan == "3":
            tabung()
        elif pilihan == "4":
            kerucut()
        elif pilihan == "5":
            bola()
        elif pilihan == "6":
            print("TERIMA KASIH!")
            break
        else:
            print("Pilih 1, 2, 3, 4 atau 5, e untuk keluar\n")


if __name__ == "__main__":
    mulai()
