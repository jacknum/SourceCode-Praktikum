#function
def hitung_luas_persegi(sisi):
    hasil = sisi * sisi
    return hasil

print("Luas persegi: %d" % hitung_luas_persegi(10))

#prosedur
def hitung_luas_segitiga(alas, tinggi):
    hasil = (alas * tinggi)/2
    print("Luas segitiga: %d" % hasil)

hitung_luas_segitiga(10, 5)