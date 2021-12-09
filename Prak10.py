"""
Nama: Muhammad Azka Aulia
NIM: 064001900026
"""

list_nama = []
list_nilai = []


def input_data():
    print("[1. INPUT DATA]")
    praktikum = []
    list_nama.append(input("Masukkan nama mahasiswa: "))

    for i in range(3):
        praktikum.append(int(input("Masukkan nilai praktikum {}: ".format(i + 1))))

    list_nilai.append(praktikum)
    print("")


def view_data():
    print("[2. VIEW DATA]\n NAMA | PRAK 1 | PRAK 2 | PRAK 3\n--------------------------------")
    for nama, nilai in zip(list_nama, list_nilai):
        prak1, prak2, prak3 = nilai
        print(nama, "\t", prak1, "\t", prak2, "\t", prak3)
    print("")


def hitung_rerata():
    nm = len(list_nilai)
    temp_rerata = [0] * nm
    for i in range(nm):
        nilai = list_nilai[i]
        hasil = 0
        np = len(nilai)
        for j in range(np):
            hasil += nilai[j]
        temp_rerata[i] = hasil / np

    for nama, rata2 in zip(list_nama, temp_rerata):
        print(nama, "=", rata2)
    print("")


while True:
    pilihan = input(
        "PROGRAM LIST\n1. Input Data\n2. View Data\n3. Hitung Nilai Rata-Rata Praktikum Tiap Mahasiswa\nPilih menu "
        "yang "
        "tersedia: ")
    print("")

    if pilihan == "1":
        input_data()
    elif pilihan == "2":
        view_data()
    elif pilihan == "3":
        hitung_rerata()
    elif pilihan == "7":
        print("[7. EXIT]\nTERIMA KASIH!")
        break
    else:
        print("Pilih 1, 2, 3, 7 untuk keluar\n")
