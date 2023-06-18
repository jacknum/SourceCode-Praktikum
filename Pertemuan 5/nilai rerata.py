mata_kuliah = (int(input("Masukkan total mata kuliah: ")))
print()
nilai = []

for i in range(int(mata_kuliah)):
    nilai1 = (int(input("Masukkan nilai mata kuliah ke - {} = ".format(i+1))))
    nilai.append(nilai1)

total = sum(nilai)
rata = total/len(nilai)

if 100 >= rata >= 90:
    predikat = 'A'
elif rata >= 70:
    predikat ='B'
elif rata >= 50:
    predikat ='C'
elif rata >= 30:
    predikat ='D'
else:
    predikat = 'E'

if any(nilai1 > 100 for nilai1 in nilai):
    print("Nilai yang dimasukkan tidak valid")
else:
    print("Hasil predikat {} dengan nilai :".format(predikat), rata)
    for i, n in enumerate(nilai):
        print("Mata kuliah ke-{} : {}".format(i+1, n))