def linear_search(keyword, data):
    for i in range(len(data)):
        if str(data[i]).lower() == keyword.lower():
            print(f"Plat dengan nomor {keyword} ditemukan {i}")
            return i
    print(f"Plat dengan nomor {keyword} tidak ditemukan")
    return -1

data = ['R 2477 SR', 'R 1234 DJ', 'R 7015 LP', 'R 0201 RR', 'R 3304 DA', 'R 2401 SK', 'R 2103 RT', 'R 1708 RI', 'R 1111 SR', 'R 4987 LH']
keyword = input("Masukkan Plat Nomor: ")
linear_search(keyword, data)




