def add_mahasiswa():
    jumlah = int(input("Jumlah Mahasiswa: "))
    mahasiswa = []
    while(jumlah > 0):
        nama = input("Nama mahasiswa: ")
        mahasiswa.append(nama)
        jumlah = jumlah - 1

    while(True):
        panggil(mahasiswa)
        jumlah = jumlah - 1
        if(jumlah < 0):
            break

def remove_mahasiswa(array_mahasiswa):
    mahasiswa = array_mahasiswa
    print("Data mahasiswa ", array_mahasiswa)
    mahasiswa.remove(input("Hapus data mahasiswa: "))
    print("Data mahasiswa ", mahasiswa)
    panggil(mahasiswa)

def asc_mahasiswa(array_mahasiswa):
    mahasiswa = array_mahasiswa
    mahasiswa.sort()
    print(mahasiswa)
    panggil(mahasiswa)

def view_mahasiswa(array_mahasiswa):
    mahasiswa = array_mahasiswa
    for x in mahasiswa:
        print("Nama Mahasiswa: ", x)
    panggil(array_mahasiswa)

def panggil(array_mahasiswa):
    print("\n == Menu Data Mahasiswa ==")
    print("1. Tambah Data Mahasiswa")
    print("2. Hapus Data Mahasiswa")
    print("3. Urutkan Data Mahasiswa")
    print("4. Lihat Data Mahasiswa")
    print("5. Tutup")

    pilih = int(input("Pilih menu: "))
    if(pilih == 1):
        add_mahasiswa()
    elif(pilih == 2):
        remove_mahasiswa(array_mahasiswa)
    elif(pilih == 3):
        asc_mahasiswa(array_mahasiswa)
    elif(pilih == 4):
        view_mahasiswa(array_mahasiswa)
    else:
        print("Selesai")

add_mahasiswa()