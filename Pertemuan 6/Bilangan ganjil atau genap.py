#procedure
def bilangan(a):
    if a % 2 == 0:
        print(a, "bilangan genap")
    else:
        print(a, "bilangan ganjil")

bil = int(input("Masukkan bilangan: "))
bilangan(bil)

#function
def bilangan(a):
    if a % 2 == 0:
        return "genap"
    else:
        return "ganjil"

bil1 = int(input("Masukkan bilangan: "))
hasil = bilangan(bil1)
print(bil1, "adalah bilangan", bilangan(bil1))