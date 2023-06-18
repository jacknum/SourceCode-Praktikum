print("PROGRAM MENCARI KPK DUA BILANGAN")
bil1 = int(input("Masukkan bilangan pertama: "))
bil2 = int(input("Masukkan bilangan kedua: "))

# mencari kelipatan bil1 dan bil2 secara berurutan
i = 1
while True:
    if i % bil1 == 0 and i % bil2 == 0:
        kpk = i
        break
    i += 1

print("KPK dari", bil1, "dan", bil2, "adalah", kpk)


