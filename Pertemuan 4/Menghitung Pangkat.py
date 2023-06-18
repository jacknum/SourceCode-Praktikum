print("PROGRAM SEDERHANA MENGHITUNG PANGKAT =====")
bilangan = int(input("Masukkan bilangan = "))
pencacah = int(input("Masukkan pencacah = "))

hasil_pangkat = 1
for i in range(pencacah):
    hasil_pangkat *= bilangan

print("Hasil pangkat =", hasil_pangkat)
