"""
Nama: Muhammad Azka Aulia
NIM: 064001900026
"""
global ongkos_tujuan, ongkos_berat, ongkir
daftar_tujuan = ["jakarta", "bogor", "depok", "tangerang", "bekasi", "bandung", "semarang", "surabaya", "yogyakarta",
                 "malang", "padang", "manado", "manokwari", "denpasar", "pontianak"]

dft_tjn = ["JKT", "BGR", "DPK", "TGR", "BKS", "BDG", "SMG", "SBY",
           "YK", "MN", "PDG", "MND", "MKW", "DNP", "PNK"]

print("PT CepatSampai")


def fun_tujuan():
    inp_tujuan = str(input("Tujuan? (tekan q untuk keluar): "))
    return inp_tujuan.strip().lower()


def penyeleksi(tujuan):
    seleksi = {
        "jakarta": dft_tjn[0],
        "bogor": dft_tjn[1],
        "depok": dft_tjn[2],
        "tangerang": dft_tjn[3],
        "bekasi": dft_tjn[4],
        "bandung": dft_tjn[5],
        "semarang": dft_tjn[6],
        "surabaya": dft_tjn[7],
        "yogyakarta": dft_tjn[8],
        "malang": dft_tjn[9],
        "padang": dft_tjn[10],
        "manado": dft_tjn[11],
        "manokwari": dft_tjn[12],
        "denpasar": dft_tjn[13],
        "pontianak": dft_tjn[14],
    }

    return seleksi.get(tujuan, "error")


def mulai():
    global ongkos_tujuan, ongkos_berat, ongkir
    tujuan = fun_tujuan()

    while tujuan in daftar_tujuan and tujuan != "q":
        inp_berat = str(input("Berat Barang:  "))
        if inp_berat.isdigit() and inp_berat > "0":
            berat = int(inp_berat)
            if tujuan == "jakarta" or tujuan == "bogor" or tujuan == "depok" \
                    or tujuan == "tangerang" or tujuan == "bekasi":
                ongkos_tujuan = 10000
                if berat <= 20:
                    ongkos_berat = 15000
                    ongkir = ongkos_tujuan + ongkos_berat
                else:
                    ongkos_berat = (berat - 20) * 1500
                    ongkir = ongkos_tujuan + ongkos_berat

            elif tujuan == "bandung" or tujuan == "semarang" \
                    or tujuan == "surabaya" or tujuan == "yogyakarta" or tujuan == "malang":
                ongkos_tujuan = 25000
                if berat <= 20:
                    ongkos_berat = 15000
                    ongkir = ongkos_tujuan + ongkos_berat
                else:
                    ongkos_berat = (berat - 20) * 1500
                    ongkir = ongkos_tujuan + ongkos_berat

            elif tujuan == "padang" or tujuan == "manado" or tujuan == "manokwari" or tujuan == "denpasar" \
                    or tujuan == "pontianak":
                ongkos_tujuan = 50000
                if berat <= 20:
                    ongkos_berat = 15000
                    ongkir = ongkos_tujuan + ongkos_berat
                else:
                    ongkos_berat = (berat - 20) * 1500
                    ongkir = ongkos_tujuan + ongkos_berat

            ppn = round(ongkir * 10 // 100)
            tujuan = penyeleksi(tujuan)

            print("---------------------Rincian Biaya-----------------------")
            print("1. Tujuan\t:", tujuan, "\t\t\tRp. ", str(f'{ongkos_tujuan:,}').replace(',', '.') + ", 00")
            print("2. Berat Barang\t:", berat, "Kg\t\t\tRp. ", str(f'{ongkos_berat:,}').replace(',', '.') + ", 00")
            print("3. PPN(10%)\t:\t\t\tRp. ", str(f'{ppn:,}').replace(',', '.') + ", 00")
            print("4. Biaya Total\t:\t\t\tRp. ", str(f'{ongkir + ppn:,}').replace(',', '.') + ", 00")
            print("---------------------------------------------------------\n")

            tujuan = fun_tujuan()

        else:
            print("Berat hanya boleh berisi angka dan harus lebih dari 0.\n")
            continue

    if tujuan not in daftar_tujuan and tujuan != "q":
        if tujuan.isdigit():
            print("Tujuan tidak boleh berisi angka.\n")
        else:
            print("Tujuan Anda belum masuk jangkauan ekspedisi kami atau tujuan tidak valid.\n")
        mulai()

    else:
        print("Terima kasih telah menggunakan program kami.\n")


if __name__ == "__main__":
    mulai()
