from math import sqrt

sisi = input("Sisi mana yang Anda ingin hitung? (a,b,c): ")

if sisi == "c":
    a = int(input("Masukkan panjang a: "))
    b = int(input("Masukkan panjang b: "))
    c = sqrt(a * a + b * b)
    print("Panjang sisi c adalah:", round(c))

elif sisi == "a":
    b = int(input("Masukkan panjang b: "))
    c = int(input("Masukkan panjang c: "))
    if (c < b):
        print("Panjang c tidak valid!")
        c = int(input("Masukkan panjang c: "))

    a = sqrt(c * c - b * b)
    print("Panjang sisi a adalah:", round(a))

elif sisi == "b":
    a = int(input("Masukkan panjang a: "))
    c = int(input("Masukkan panjang c: "))
    if (c < a):
        print("Panjang c tidak valid!")
        c = int(input("Masukkan panjang c: "))

    b = sqrt(c * c - a * a)
    print("Panjang sisi b adalah:", round(b))


