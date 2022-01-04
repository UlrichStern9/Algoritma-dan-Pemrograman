"""
Nama: Muhammad Azka Aulia
NIM: 064001900026
"""

nama_file = ""
temp_update = ""
indeks = 0


def cek_file():
    global nama_file
    while True:
        nama_file = input("Masukkan nama file: ")
        try:
            open(nama_file)
            print("")
            break
        except FileNotFoundError:
            print("File tidak ditemukan\n")


def lihat_nilai():
    print("[1. LIHAT NILAI]")
    data_nilai = []
    baca_data1 = open(nama_file).readlines()
    nama = input("Masukkan nama mahasiswa: ").capitalize()
    for nilai in range(len(baca_data1)):
        data_nilai.append(baca_data1[nilai].split())
        if nama in data_nilai[nilai][0]:
            prak1, prak2, prak3 = int(data_nilai[nilai][1]), int(data_nilai[nilai][2]), int(data_nilai[nilai][3])
            print(" NAMA | RERATA | PRAK 1 | PRAK 2 | PRAK 3\n------------------------------------------")
            print("{} \t {} \t   {} \t    {} \t     {}\n".format(nama, round((prak1 + prak2 + prak3) / 3),prak1, prak2, prak3))
            break


def update_nilai():
    global temp_update, indeks
    print("[2. UPDATE NILAI]")
    data_nilai = []
    baca_data3 = open(nama_file).readlines()
    nama = input("Masukkan nama mahasiswa: ").capitalize()
    for nilai in range(len(baca_data3)):
        data_nilai.append(baca_data3[nilai].split())
        if nama in data_nilai[nilai][0]:
            indeks = nilai
            prak_ke = int(input("Ingin update nilai praktikum ke-: "))
            if 0 < prak_ke < 4:
                nilai_baru = input("Nilai baru: ")
                data_nilai[nilai][prak_ke] = nilai_baru
                prak1, prak2, prak3 = data_nilai[nilai][1], data_nilai[nilai][2], data_nilai[nilai][3]
                temp_update = "{} \t  {} \t   {} \t   {}\n".format(nama, prak1, prak2, prak3)
                print("DATA BERHASIL DI-UPDATE")
                print("")
                break


def hapus_data():
    global temp_update, indeks
    print("[3. HAPUS DATA]")

    pilihan = input("A. Hapus nilai praktikum mahasiswa\n"
                    "B. Hapus semua data dalam file\n"
                    "Pilih menu yang tersedia: ").upper()

    if pilihan == "A":
        print("\n[A. HAPUS NILAI PRAK MAHASISWA]")
        data_nilai = []
        baca_data3 = open(nama_file).readlines()
        nama = input("Masukkan nama mahasiswa: ").capitalize()
        for nilai in range(len(baca_data3)):
            data_nilai.append(baca_data3[nilai].split())
            if nama in data_nilai[nilai][0]:
                indeks = nilai
                prak_ke = int(input("Ingin hapus nilai praktikum ke-: "))
                if 0 < prak_ke < 4:
                    nilai_baru = "00"
                    data_nilai[nilai][prak_ke] = nilai_baru
                    prak1, prak2, prak3 = data_nilai[nilai][1], data_nilai[nilai][2], data_nilai[nilai][3]
                    temp_update = "{} \t  {} \t   {} \t   {}\n".format(nama, prak1, prak2, prak3)
                    print("DATA BERHASIL DIHAPUS")
                    print("")
                    break

    elif pilihan == "B":
        print("[B. HAPUS SEMUA DATA DALAM FILE]")
        with open(nama_file, 'r+') as f:
            f.truncate(0)
        print("ISI FILE BERHASIL DIHAPUS")
        print("")

    else:
        print("\nPilih A atau B\n")


def lihat_semua():
    print("[4. LIHAT SEMUA]\n NAMA | RERATA | PRAK 1 | PRAK 2 | PRAK 3\n------------------------------------------")
    rerata_prak1 = []
    rerata_prak2 = []
    rerata_prak3 = []
    baca_data1 = open(nama_file).readlines()
    for nilai in range(len(baca_data1)):
        data_nilai = baca_data1[nilai].split()
        nama = data_nilai[0]
        prak1 = int(data_nilai[1])
        prak2 = int(data_nilai[2])
        prak3 = int(data_nilai[3])
        rerata_mhs = (prak1 + prak2 + prak3) / 3
        rerata_prak1.append(prak1)
        rerata_prak2.append(prak2)
        rerata_prak3.append(prak3)
        print("{} \t  {} \t   {} \t    {} \t     {}".format(nama, round(rerata_mhs), prak1, prak2, prak3))
    print("------------------------------------------")
    print("RERATA PRAKTIKUM: {} \t   {}\t    {}\n".format(sum(rerata_prak1) / len(rerata_prak1),
                                                         sum(rerata_prak2) / len(rerata_prak2),
                                                         sum(rerata_prak3) / len(rerata_prak3)))


def simpan_ke_file(f=None):
    print("[5. SIMPAN KE FILE]")
    baca_data5 = open(nama_file, "r")
    data_nilai = baca_data5.readlines()
    data_nilai[indeks] = temp_update

    baca_data5 = open(nama_file, "w")
    baca_data5.writelines(data_nilai)
    baca_data5.close()
    print("PERUBAHAN BERHASIL DISIMPAN\n")


def mulai():
    cek_file()

    while True:
        pilihan = input("------------------[MENU]------------------\n"
                        "| 1. Lihat Nilai\n"
                        "| 2. Update Nilai\n"
                        "| 3. Hapus Data\n"
                        "| 4. Lihat Semua\n"
                        "| 5. Simpan ke file\n"
                        "| 6. Keluar\n"
                        "------------------------------------------\n"
                        "Pilih menu yang tersedia: ")
        print("")

        if pilihan == "1":
            lihat_nilai()

        elif pilihan == "2":
            update_nilai()

        elif pilihan == "3":
            hapus_data()

        elif pilihan == "4":
            lihat_semua()

        elif pilihan == "5":
            simpan_ke_file()

        elif pilihan == "6":
            print("Anda telah keluar dari program")
            break
        else:
            print("Pilih 1, 2, 3, 4, 5 atau 6 untuk keluar\n")


if __name__ == "__main__":
    mulai()
