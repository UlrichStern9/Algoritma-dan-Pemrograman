"""
Nama: Muhammad Azka Aulia
NIM: 064001900026
"""

list_nama = []
list_nilai = []


def buka_file():
    while True:
        nama_file = input("Masukkan nama file: ")
        try:
            file = open(nama_file)
            for row in range(5):
                temp_nilai = []
                data_nilai = file.readline()
                temp_nilai.append(data_nilai.split())
                nilai = temp_nilai.pop()
                list_nama.append(nilai.pop(0))
                list_nilai.append(nilai)
                konversi_int = [int(item) for item in list_nilai[row]]
                list_nilai[row] = konversi_int
            print("")
            break
        except FileNotFoundError:
            print("File tidak ditemukan\n")


def baca_data():
    print("[1. BACA DATA]\n NAMA | PRAK 1 | PRAK 2 | PRAK 3\n--------------------------------")
    for nama, nilai in zip(list_nama, list_nilai):
        prak1, prak2, prak3 = nilai
        print(nama, "\t", prak1, "\t", prak2, "\t", prak3)
    print("")


def cari_rerata_prak_mhs():
    print("[2. MENCARI RATA-RATA NILAI PRAK TIAP MAHASISWA]")
    nama_mhs = input("Masukkan nama mahasiswa: ").capitalize()
    if nama_mhs in list_nama:
        indeks = list_nama.index(nama_mhs)
        print(" NAMA | PRAK 1 | PRAK 2 | PRAK 3\n--------------------------------")
        prak1, prak2, prak3 = list_nilai[indeks]
        print(nama_mhs, "\t", prak1, "\t", prak2, "\t", prak3)
        print("\nRerata nilai praktikum {} =".format(nama_mhs), sum(list_nilai[indeks]) / len(list_nilai[indeks]), "\n")


def mulai():
    buka_file()

    while True:
        pilihan = input("MENU\n"
                        "1. Baca Data\n"
                        "2. Mencari Rata-Rata Nilai Praktikum Mahasiswa\n"
                        "5. Exit\n"
                        "Pilih menu yang tersedia: ")
        print("")

        if pilihan == "1":
            baca_data()

        elif pilihan == "2":
            cari_rerata_prak_mhs()

        elif pilihan == "5":
            print("[5. EXIT]\nTERIMA KASIH!")
            break
        else:
            print("Pilih 1, 2, atau 5 untuk keluar\n")


if __name__ == "__main__":
    mulai()
