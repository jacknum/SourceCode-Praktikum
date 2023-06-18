def hitung_luas_persegi(sisi):
    hasil = sisi * sisi
    return hasil

def hitung_keliling_persegi(sisi):
    hasil = sisi * 4
    return hasil

sisi = (int(input("Masukkan Sisi: ")))
print("Luas persegi: %d" % 
      hitung_luas_persegi(sisi))
print("Keliling persegi: %d" % 
      hitung_keliling_persegi(sisi))

def keliling_luas_persegi(sisi):
    keliling = 4 * sisi
    luas = sisi * sisi
    print("Keliling persegi: ", keliling)
    print("Luas persegi: ", luas)

sisi = int(input("Masukkan sisi: "))
keliling_luas_persegi(sisi)