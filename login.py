import csv

file_path = 'data_Akun.csv'

def registrasi(username, password): 
    with open(file_path, 'a') as file:
        menambah_data = csv.DictWriter(file, fieldnames=['Username', 'Password'])
        menambah_data.writerow({
            'Username': username,
            'Password': password
        })
def login(username, password):
    with open(file_path, ) as file:
        membaca_data = csv.reader(file)
        hasil = False

        for i in membaca_data:
            if (username in i) and (password in i):
                hasil = True
            if hasil:
                break
        return hasil
    
def dashboard(username):
    print(f"\nSelamat datang {username}")
    print('-' * 21)
    print('| ','Easy@ Dashboard', ' |')
    print('-' * 21)

    while True:
        print("Menu: ")
        print("1. Hitung BMI (Body Mass Index)")
        print("2. Rekomendasi Diet")
        print("3. Resep-resep")
        print("4. Calory Tracking")
        print("5. Profile User") # optional
        print("0. Keluar")

        menu = int(input("Pilih dari (0-5): "))

        if menu == 0:
            print("\nSelamat Tinggal! Semoga Harimu Menyenangkan! ^_^ ")
            break
        elif menu == 1:
            pass # file bmi.py
        elif menu == 2:
            pass # file dietrec.py
        elif menu == 3:
            pass # file reseppage.py
        elif menu == 4:
            pass # file calorytrack.py
        elif menu == 5: #optional
            pass # optional
        else:
            print("\nInvalid! Silahkan memasukkan angka dari 0-5\n")
    
def registrasi_login():
    print("Selamat Datang di Easy@!: ")
    while True:
        print("1. Registrasi")
        print("2. Login")
        print("3. Keluar")

        tipe = int(input("Pilih (1, 2, atau 3): "))

        if tipe == 1:
            username_input = input("Buat Username: ")
            password_input = input("Buat Password: ")
            registrasi(username_input, password_input)

        elif tipe == 2:
            x = 1
            while x != 4:
                username_input = input("Username: ")
                password_input = input("Password: ")
                cek_login = login(username_input, password_input)
                if cek_login:
                    user = username_input
                    break
                else:
                    print("Username atau password kamu salah, silahkan masukkan kembali!")
                    x += 1
            if x == 4:
                print("Kamu salah Username atau Password 3 kali, jika kamu belum memiliki akun \nSilahkan registrasi terlebih dahulu")
            if cek_login:
                    break        
        elif tipe == 3:
            print("Selamat Tinggal! Semoga Harimu Menyenangkan! ^_^ ")
            break
        else:
            print("Invalid! \nDimohon untuk memasukkan angka 1, 2 atau 3")

    if cek_login:
        dashboard(user)

import csv

file_path = 'data_Akun.csv'

def registrasi(username, password): 
    with open(file_path, 'a') as file:
        menambah_data = csv.DictWriter(file, fieldnames=['Username', 'Password'])
        menambah_data.writerow({
            'Username': username,
            'Password': password
        })
def login(username, password):
    with open(file_path, ) as file:
        membaca_data = csv.reader(file)
        hasil = False

        for i in membaca_data:
            if (username in i) and (password in i):
                hasil = True
            if hasil:
                break
        return hasil
    
def dashboard(username):
    print(f"\nSelamat datang {username}")
    print('-' * 21)
    print('| ','Easy@ Dashboard', ' |')
    print('-' * 21)

    while True:
        print("Menu: ")
        print("1. Hitung BMI (Body Mass Index)")
        print("2. Rekomendasi Diet")
        print("3. Resep-resep")
        print("4. Calory Tracking")
        print("5. Profile User") # optional
        print("0. Keluar")

        menu = int(input("Pilih dari (0-5): "))

        if menu == 0:
            print("\nSelamat Tinggal! Semoga Harimu Menyenangkan! ^_^ ")
            break
        elif menu == 1:
            pass # file bmi.py
        elif menu == 2:
            pass # file dietrec.py
        elif menu == 3:
            pass # file reseppage.py
        elif menu == 4:
            pass # file calorytrack.py
        elif menu == 5: #optional
            pass # optional
        else:
            print("\nInvalid! Silahkan memasukkan angka dari 0-5\n")
    
def registrasi_login():
    print("Selamat Datang di Easy@!: ")
    while True:
        print("1. Registrasi")
        print("2. Login")
        print("3. Keluar")

        tipe = int(input("Pilih (1, 2, atau 3): "))

        if tipe == 1:
            username_input = input("Buat Username: ")
            password_input = input("Buat Password: ")
            registrasi(username_input, password_input)

        elif tipe == 2:
            x = 1
            while x != 4:
                username_input = input("Username: ")
                password_input = input("Password: ")
                cek_login = login(username_input, password_input)
                if cek_login:
                    user = username_input
                    break
                else:
                    print("Username atau password kamu salah, silahkan masukkan kembali!")
                    x += 1
            if x == 4:
                print("Kamu salah Username atau Password 3 kali, jika kamu belum memiliki akun \nSilahkan registrasi terlebih dahulu")
            if cek_login:
                    break        
        elif tipe == 3:
            print("Selamat Tinggal! Semoga Harimu Menyenangkan! ^_^ ")
            break
        else:
            print("Invalid! \nDimohon untuk memasukkan angka 1, 2 atau 3")

    if cek_login:
        dashboard(user)

registrasi_login()