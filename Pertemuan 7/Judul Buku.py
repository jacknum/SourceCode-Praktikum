def insertion_ascending(array):
        for i in range (1, len(array)):
            item = array [i]
            j = i - 1 

            while j >= 0 and array[j] > item:
                array[j + 1] = array[j]
                j -= 1

            array[j + 1] = item 
            

def insertion_descending(array):
        for i in range (1, len(array)):
            item = array [i]
            j = i - 1 

            while j >= 0 and array[j] < item:
                array[j + 1] = array[j]
                j -= 1

            array[j + 1] = item 
            
        
def judul_buku(array):
    jumlah_buku = int(input("Masukkan Total Buku : "))
    n = 1
    while jumlah_buku > 0:
        nama_buku = input(f"Masukkan judul buku ke- {n} : ")
        array.append(nama_buku)
        n += 1
        jumlah_buku -= 1

def panggil(buku):
    print("\n == Urutkan ==")
    print("1. Ascending")
    print("2. Descending")
    
    pilih = input("Masukkan pilihan: ")
    
    if pilih == '1':
        insertion_ascending(buku)
        print("\nSorting secara Ascending:")
        
    elif pilih == '2':
        insertion_descending(buku)
        print("\nSorting secara Descending:")
        
    else:
        print("Tidak Ada")

def hasil(array):
    print(" ")
    for i, n in enumerate(array):
        print(f"Judul buku ke- {i+1} : {n}")

data_buku = []
judul_buku(data_buku)
panggil(data_buku)
hasil(data_buku)