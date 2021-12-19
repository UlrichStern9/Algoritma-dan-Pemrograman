"""
Nama: Muhammad Azka Aulia
NIM: 064001900026
"""

# Deklarasi variabel ongkos_tujuan, ongkos_berat, ongkir sebagai variabel global
ongkos_tujuan, ongkos_berat, ongkir = 0, 0, 0

# Deklarasi list daftar tujuan dan kode tujuan
daftar_tujuan = ["jakarta", "bogor", "depok", "tangerang", "bekasi", "bandung", "semarang", "surabaya", "yogyakarta",
                 "malang", "padang", "manado", "manokwari", "denpasar", "pontianak"]

kode_tujuan = ["JKT", "BGR", "DPK", "TGR", "BKS", "BDG", "SMG", "SBY",
               "YK", "MN", "PDG", "MND", "MKW", "DNP", "PNK"]


# Fungsi untuk mengambil data tujuan yang dimasukkan pengguna
def input_tujuan():
    inp_tujuan = str(input("Tujuan? (tekan q untuk keluar): "))
    return inp_tujuan.strip().lower()


# Fungsi untuk menyeleksi dan menyingkat nama kota menjadi kode kota
def seleksi_tujuan(tujuan):
    seleksi = {
        "jakarta": kode_tujuan[0],
        "bogor": kode_tujuan[1],
        "depok": kode_tujuan[2],
        "tangerang": kode_tujuan[3],
        "bekasi": kode_tujuan[4],
        "bandung": kode_tujuan[5],
        "semarang": kode_tujuan[6],
        "surabaya": kode_tujuan[7],
        "yogyakarta": kode_tujuan[8],
        "malang": kode_tujuan[9],
        "padang": kode_tujuan[10],
        "manado": kode_tujuan[11],
        "manokwari": kode_tujuan[12],
        "denpasar": kode_tujuan[13],
        "pontianak": kode_tujuan[14],
    }

    return seleksi.get(tujuan, "error")


# Fungsi untuk menangani input yang benar dan lanjut ke tahap selanjutnya
def tangani_input_benar(tujuan):
    while tujuan in daftar_tujuan and tujuan != "q":
        inp_berat = str(input("Berat Barang:  "))

        if inp_berat.isdigit() and inp_berat > "0":
            berat = int(inp_berat)

            ongkir_tujuan(tujuan)

            ongkir_berat(berat)

            rincian_biaya(seleksi_tujuan(tujuan), berat, ppn())

            tujuan = input_tujuan()

        else:
            print("Berat hanya boleh berisi angka dan harus lebih dari 0.\n")
            continue

    tangani_input_salah(tujuan)


# Fungsi untuk menghitung ongkir berdasarkan kota tujuannya
def ongkir_tujuan(tujuan):
    global ongkos_tujuan
    if tujuan == "jakarta" or tujuan == "bogor" or tujuan == "depok" \
            or tujuan == "tangerang" or tujuan == "bekasi":
        ongkos_tujuan = 10000

    elif tujuan == "bandung" or tujuan == "semarang" \
            or tujuan == "surabaya" or tujuan == "yogyakarta" or tujuan == "malang":
        ongkos_tujuan = 25000

    elif tujuan == "padang" or tujuan == "manado" or tujuan == "manokwari" or tujuan == "denpasar" \
            or tujuan == "pontianak":
        ongkos_tujuan = 50000


# Fungsi untuk menghitung ongkir berdasarkan beratnya
def ongkir_berat(berat):
    global ongkos_berat, ongkir
    ongkos_berat = 15000
    if berat <= 20:
        ongkir = ongkos_tujuan + ongkos_berat
    else:
        ongkos_berat = ongkos_berat + ((berat - 20) * 1500)
        ongkir = ongkos_tujuan + ongkos_berat


# Fungsi untuk menghitung Pajak Pertambahan Nilai
def ppn():
    return round(ongkir * 10 // 100)


# Fungsi untuk menangani input yang salah dan memberi peringatan
def tangani_input_salah(tujuan):
    if tujuan not in daftar_tujuan and tujuan != "q":
        if tujuan.isdigit():
            print("Tujuan tidak boleh berisi angka.\n")
        else:
            print("Tujuan Anda belum masuk jangkauan ekspedisi kami atau tujuan tidak valid.\n")
        mulai()

    else:
        print("Terima kasih telah menggunakan program kami.\n")


# Fungsi untuk menampilkan rincian biaya dari ongkos kirimnya
def rincian_biaya(tujuan, berat, ppn):
    print("---------------------Rincian Biaya-----------------------")
    print("1. Tujuan\t:", tujuan, "\t\t\tRp. ", str(f'{ongkos_tujuan:,}').replace(',', '.') + ", 00")
    print("2. Berat Barang\t:", berat, "Kg\t\t\tRp. ", str(f'{ongkos_berat:,}').replace(',', '.') + ", 00")
    print("3. PPN(10%)\t:\t\t\tRp. ", str(f'{ppn:,}').replace(',', '.') + ", 00")
    print("4. Biaya Total\t:\t\t\tRp. ", str(f'{ongkir + ppn:,}').replace(',', '.') + ", 00")
    print("---------------------------------------------------------\n")


# Fungsi untuk memulai programnya
def mulai():
    print("PT CepatSampai")
    tujuan = input_tujuan()
    tangani_input_benar(tujuan)


# Fungsi main
if __name__ == "__main__":
    mulai()
