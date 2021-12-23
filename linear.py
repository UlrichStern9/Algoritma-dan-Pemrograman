"""
Nama: Muhammad Azka Aulia
NIM: 064001900026
"""

while True:
    print("LINEAR SEARCH")
    panjang = int(input("Masukkan Jumlah Angka Pada List : "))
    list_linear = []
    for i in range(panjang):
        list_linear.append(int(input("Angka Ke-{}: ".format(i + 1))))
    print("\nList Angka -> ", list_linear)


    def linearsearch(list_linear, x):
        for i in range(len(list_linear)):
            if list_linear[i] == x:
                return "Ditemukan\n"
        return "Tidak Ditemukan\n"


    x = int(input("Masukkan angka yang dicari : "))
    print("Hasil Linear Search -> " + str(linearsearch(list_linear, x)))
