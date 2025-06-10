#Menentukan Nilai Mata Kuliah 

Nama = input("Silahkan masukkan nama Anda: ")

NIM = input("Silahkan masukkan NIM Anda: ")

Matakuliah = input("Silahkan masukkaan nama mata kuliah: ")

Nilai = float(input("Silahkan masukkan nilai Anda: "))

if Nilai >= 80: 
    print("Nilai adalah A, Anda dinyatakan lulus mata kuliah")
elif Nilai >= 75: 
    print("Nilai adalah A-, Anda dinyatakan lulus mata kuliah")
elif Nilai >= 70: 
    print("Nilai adalah B+, Anda dinyatakan lulus mata kuliah")
elif Nilai >= 65: 
    print("Nilai adalah B, Anda dinyatakan lulus mata kuliah")
elif Nilai >= 60: 
    print("Nilai adalah B-, Anda dinyatakan lulus mata kuliah")
elif Nilai >= 55: 
    print("Nilai adalah C+, Anda dinyatakan lulus mata kuliah")
elif Nilai >= 50: 
    print("Nilai adalah C, Anda dinyatakan lulus mata kuliah")
elif Nilai >= 45: 
    print("Nilai adalah D, Anda dinyatakan tidak lulus mata kuliah")
elif Nilai >= 0: 
    print("Nilai adalah E, Anda dinyatakan tidak lulus mata kuliah")
else: 
    print("Pilihan anda tidak tersedia")