"""
Nama: Muhammad Azka Aulia
NIM: 064001900026

Jalankan file-nya, kemudian pilih sesuai elemen kompetensinya.
Terima kasih.
"""


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
    print("MENGHITUNG KECEPATAN AKHIR GLBB (diketahui jarak tempuh)")
    v0 = int(input("Masukkan v0: "))
    a = int(input("Masukkan a: "))
    s = int(input("Masukkan s: "))

    def vt(kec_awal, percepatan, jarak):
        return (kec_awal ** 2 + (2 * percepatan * jarak)) ** (1 / 2)

    vt = vt(v0, a, s)

    print("Jarak tempuh jika kecepatan awal:", v0, "percepatan:", a, "dan jarak tempuh:", s, "adalah:", vt)


def elkom2():
    daftar_vokal = ["a", "i", "u", "e", "o"]

    print("PROGRAM MENGHITUNG HURUF VOKAL DAN KONSONAN DARI KALIMAT")

    masuk = str(input("Masukkan kalimat: ")).lower()

    vokal = 0
    konsonan = 0

    def hitung(masuk):
        global vokal, konsonan
        for huruf in masuk:
            if huruf in daftar_vokal:
                vokal += 1
            else:
                konsonan += 1

    hitung(masuk)

    print("Jumlah huruf vokal adalah ", vokal)
    print("Jumlah huruf konsonan adalah ", konsonan)


def elkom3():
    print("PROGRAM PENGECEKAN BILANGAN")

    masuk = int(input("Masukkan bilangan: "))

    def pangkatkan(angka):
        return angka ** 3

    def cek_modulo(angka):
        if angka % 3 == 0:
            return True
        else:
            return False

    hasil = cek_modulo(masuk)

    if hasil is True:
        print("Hasil:", pangkatkan(masuk))
    else:
        print("Hasil:", hasil)


if __name__ == "__main__":
    mulai()
