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
    a1 = int(input("Masukkan titik koordinat A1: "))
    a2 = int(input("Masukkan titik koordinat A2: "))
    b1 = int(input("\nMasukkan titik koordinat B1: "))
    b2 = int(input("Masukkan titik koordinat B2: "))
    jarak = ((((a2 - a1) ** 2) + ((b2 - b1) ** 2)) ** 0.5)
    print("\nJarak dari titik", (a1, a2), "dan", (b1, b2), "adalah: ", jarak, "\n")

def elkom3():
    kecil = str(input("Please enter a 4-characters string: "))
    besar = ""

    for i in kecil:
        if 97 <= ord(i) <= 122:
            besar = besar + chr(ord(i) - 32)

    print("The string capitalizaiton is: ", besar, "\n")

if __name__ == "__main__":
    mulai()
