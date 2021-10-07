def masuk():
    inp = input(str("Masukkan sebuah tanggal (dd/mm/yy): "))
    inp_splitted = inp.split("/")
    bulan = int(inp_splitted[1])
    keluar(bulan, inp)


def keluar(bulan, inp):
    bulan = seleksi(bulan)
    tanggal = inp.replace(inp[3:5], bulan, 1).replace(inp[2], "-")
    print("Tanggal dalam format lain:", tanggal)


def seleksi(bulan):
    nambulan = "JanFebMarAprMeiJunJulAgtSepOktNovDes"
    switcher = {
        1: nambulan[0:3],
        2: nambulan[3:6],
        3: nambulan[6:9],
        4: nambulan[9:12],
        5: nambulan[12:15],
        6: nambulan[15:18],
        7: nambulan[18:21],
        8: nambulan[21:24],
        9: nambulan[24:27],
        10: nambulan[27:30],
        11: nambulan[30:33],
        12: nambulan[33:36],
    }

    return switcher.get(bulan, "error")


if __name__ == "__main__":
    masuk()
