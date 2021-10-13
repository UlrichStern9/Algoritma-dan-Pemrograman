while True:
    pilihan = int(input(
        "---PROGRAM KONVERSI BILANGAN---\n1 -> Desimal ke biner\n2 -> Biner ke desimal\n3 -> Keluar\nSilakan pilih menu: "))

    if pilihan == 1:
        bilangan = int(input("Masukkan bilangan desimal: "))

        hasil = ""
        while bilangan != 0:
            sisa = bilangan % 2
            bilangan = bilangan // 2
            hasil = str(sisa) + hasil
        print("Nilai binernya adalah: ", hasil, "\n")

    if pilihan == 2:
        biner = int(input("Masukkan bilangan biner: "))

        desimal = 0
        i = 1
        while biner != 0:
            sisa = biner % 10
            desimal = desimal + (sisa * i)
            i = i * 2
            biner = int(biner / 10)

        print("Nilai desimalnya adalah: ", desimal, "\n")

    if pilihan == 3:
        break

    else:
        print("Pilih 1, 2 atau 3")
