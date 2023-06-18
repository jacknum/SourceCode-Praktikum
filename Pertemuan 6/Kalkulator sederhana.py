def tambah(a, b):
    return a + b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b == 0:
        return "Error: Tidak bisa membagi dengan 0!"
    else:
        return a / b

def kurang(a, b):
    return a - b

def pangkat(a, b):
    return a ** b

def kalkulator():
        print("--Kalkulator Sederhana--")
        print("Pilih operasi:")
        print("1. Penjumlahan")
        print("2. Perkalian")
        print("3. Pembagian")
        print("4. Pengurangan")
        print("5. Pangkat")
        pilihan = input("Masukkan pilihan (1/2/3/4/5/6): ")

        if pilihan in ['1', '2', '3', '4', '5']:
            bil1 = float(input("Masukkan bilangan pertama: "))
            bil2 = float(input("Masukkan bilangan kedua: "))

            if pilihan == '1':
                print("Hasil penjumlahan:", tambah(bil1, bil2))
            elif pilihan == '2':
                print("Hasil perkalian:", kali(bil1, bil2))
            elif pilihan == '3':
                print("Hasil pembagian:", bagi(bil1, bil2))
            elif pilihan == '4':
                print("Hasil pengurangan:", kurang(bil1, bil2))
            else:
                print("Hasil pangkat:", pangkat(bil1, bil2))
        else:
            print("Pilihan tidak valid.")

kalkulator()