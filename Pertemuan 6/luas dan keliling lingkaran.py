#function
def luas_lingkaran(a):
    rumusl = 3.14 * a**2
    return rumusl

def keliling_lingkaran(a):
    rumusk = 2 * 3.14 * a
    return rumusk

jari = int(input("Masukkan jari-jari: "))
print("Luas lingkaran: ", luas_lingkaran(jari))
print("Keliling lingkaran: ", keliling_lingkaran(jari))

#procedure
def L_lingkaran(jari2):
    hasil = 3.14 * jari2**2
    print("Luas lingkaran: ", hasil)

def K_lingkaran(jari2):
    hasil1 = 2 * 3.14 * jari2**2
    print("Keliling lingkaran: ", hasil1)

jari2 = int(input("Masukkan jari-jari: "))
L_lingkaran(jari2)
K_lingkaran(jari2)