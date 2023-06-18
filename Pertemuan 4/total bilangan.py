print("Project PROGRAM SEDERHANA MENGHITUNG JUMLAH TOTAL BILANGAN")
bilangan = int(input("Masukkan bilangan = "))

total = 0
for i in range(bilangan, 0, -1):
    total += i
    if i == 1:
        print(i, end=" = ")
    else:
        print(i, end=" + ")

print(total)
