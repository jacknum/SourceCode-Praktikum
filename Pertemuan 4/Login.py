login = 0
while True:
    username = input("Masukkan Username ")
    password = input("Masukkan Password ")

    if login == 3:
        print("Njajale wis entong, ngesuk maning")
        break
    if username == "JackNoem" and password == "bambang":
        print("Irasshaimase ", username, "!")
        break
    else:
        print("Login gagal, Silahkan njajal maning")
        login += 1



