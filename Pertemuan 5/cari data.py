kata = int(input("masukkan total kata: "))
kata1 = []

for i in range(kata):
    kata2 = (str(input("Masukkan Kata: ")))
    kata1.append(kata2)

cari = (input("Masukkan Kata yang ingin dicari: "))
if cari in kata1:
    indeks = kata1.index(cari)
    print(cari, "Kata ditemukan pada indeks ke -", format(indeks))
else:
    print("Kata yang anda cari tidak ditemukan")