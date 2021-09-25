"""
Nama: Muhammad Azka Aulia
NIM: 064001900026

Jalankan file-nya, kemudian pilih sesuai elemen kompetensinya.
Terima kasih.
"""


def mulai():
    while True:
        masuk = int(input("Elkom?: "))
        if masuk == 1:
            elkom1()
        elif masuk == 2:
            elkom2()
        elif masuk == 3:
            elkom3()
        else:
            print("Pilih 1, 2 atau 3\n")


def elkom1():
    print("        @            @@@@@@@@@@        @    @             @    ")
    print("       @ @                   @         @   @             @ @     ")
    print("      @   @                 @          @  @             @   @        ")
    print("     @     @               @           @ @             @     @    ")
    print("    @       @             @            @@             @       @   ")
    print("   @@@@@@@@@@@           @             @ @           @@@@@@@@@@@     ")
    print("  @           @         @              @  @         @           @   ")
    print(" @             @       @               @   @       @             @    ")
    print("@               @     @@@@@@@@@@       @    @     @               @    ")

    print('Ayah minggu lalu berkata, "Ayah besok akan pergi dinas"')
    print("I'm sitting on the bench\n")


def elkom2():
    import math

    a = input("Masukkan titik koordinat A: ").split()
    b = input("Masukkan titik koordinat B: ").split()
    a0 = int(a[0])
    a1 = int(a[1])
    b0 = int(b[0])
    b1 = int(b[1])
    jarak = math.sqrt(((a0 - b0) ** 2) + ((a1 - b1) ** 2))

    print("\nJarak dari titik a(" + str(a0) + "," + str(a1) + ")", "dan b(" + str(b0) + "," + str(b1) + ")", "adalah:",
          round(int(jarak)) , "\n")


def elkom3():
    kecil = str(input("Please enter a 4-characters string: "))
    besar = ""

    for i in kecil:
        if 97 <= ord(i) <= 122:
            besar = besar + chr(ord(i) - 32)

    print("The string capitalizaiton is: ", besar, "\n")


if __name__ == "__main__":
    mulai()
