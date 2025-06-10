#Program Login dan Menentukan Nilai Mata Kuliah

print("===Program Login dan Menentukan Nilai Mata Kuliah===")

#Data Login
username_awal = "IchaK26"
password_awal = "931009"
kesempatan_1 = 3

for kesempatan in range(1, kesempatan_1+1):
    username = input("Username:")
    password = input("Password:")

    if username == username_awal and password == password_awal:
        print(f"Selamat Datang {username_awal}")
        break
    
    else:
        print(f"Username atau Password Anda Salah, Silahkan Coba Lagi. Kesempatan Anda Tinggal {kesempatan_1-kesempatan}x")
        if kesempatan == 3:
            print("Maaf Tidak Bisa Login, Coba Lagi Nanti")
        continue
        

#Data Nilai Mata Kuliah 
print("===Program Menentukan Nilai Mata Kuliah===")
while True:
    print("Silahkan Masukkan Data Anda")
    nama = input("Masukkan Nama Anda:")
    nim = input("Masukkan NIM Anda:")
    matakuliah = input("Masukkan Nama Mata Kuliah:")
    while True:
        nilai = float(input("Masukkan Nilai Anda:"))
        if 0 <= nilai <= 100:
            break 
        else:
            print("Nilai yang Anda Masukkan Salah, Silahkan Coba Lagi!")
            continue 
    if nilai >= 80:
        print(f"Nilai adalah A, Anda dinyatakan lulus mata kuliah {matakuliah} ")
    elif nilai >= 75:
        print(f"Nilai adalah A-, Anda dinyatakan lulus mata kuliah {matakuliah}")
    elif nilai >= 70:
        print(f"Nilai adalah B+, Anda dinyatakan Lulus mata kuliah {matakuliah} ")
    elif nilai >= 65:
        print(f"Nilai adalah B, Anda dinyatakan lulus mata kuliah {matakuliah}")
    elif nilai >= 60:
        print(f"Nilai adalah B-, Anda dinyatakan lulus mata kuliah {matakuliah}")
    elif nilai >= 55:
        print(f"Nilai adalah C+, Anda dinyatakan lulus mata kuliah {matakuliah} ")
    elif nilai >= 50:
        print(f"Nilai adalah C, Anda dinyatakan lulus mata kuliah {matakuliah}")
    elif nilai >= 45:
        print(f"Nilai adalah D, Anda dinyatakan tidak lulus mata kuliah {matakuliah}")
    elif nilai >= 0:
        print(f"Nilai adalah E, Anda dinyatakan tidak lulus mata kuliah {matakuliah}")
    else:
        print("Pilihan Anda Tidak Tersedia")

    next = input("Apakah Anda Ingin Menginput Nilai lainnya? (y/n)")
    if next == "y":
        continue
    elif next == "n":
        exit()
    else:
        print("Pilihan Anda Tidak Tersedia")
    