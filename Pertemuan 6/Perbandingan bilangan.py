def perbandingan(bilangan1, bilangan2):
    if bilangan1 > bilangan2:
        print("Bilangan", bilangan1,"Lebih besar")
    elif bilangan1 == bilangan2:
        print("Bilangan sama")
    else:
        print("Bilangan", bilangan2,"Lebih besar")

bilangan1 = (int(input("Masukkan bilangan ke 1: ")))
bilangan2 = (int(input("Masukkan bilangan ke 2: ")))

perbandingan(bilangan1, bilangan2)