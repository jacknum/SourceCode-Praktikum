# # if satu kondisi
nilai = int(input("Masukkan Bilangan Bulat: "))
if(nilai > 0):
    print("Bilangan", nilai, "merupakan bilangan positif")
# if dua kondisi menggunakan else
elif(nilai < 0): 
    print("Bilangan", nilai, "merupakan bilangan negatif")
else:
    print("Bilangan nol")