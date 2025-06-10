#Menghitung Biaya Parkir Motor dan Mobil 

x1 = 3
x2 = 5
y1 = 2
y2 = 3
z1 = 16000
z2 = 25000 

#Mengeliminasi harga untuk mendapatkan biaya parkir motor 
x1, y1, z1 = x1 * 3, y1 * 3, z1 * 3 
x2, y2, z2 = x2 * 2, y2 * 2, z2 * 2

harga_motor = (z1 - z2) / (x1 - x2)

harga_mobil = (16000 - 3 * harga_motor) / 2 

print("Harga parkir satu motor adalah Rp.", harga_motor)
print("Harga parkir satu mobil adalah Rp.", harga_mobil)

motor = int(input("Masukkan jumlah motor yang parkir:"))
mobil = int(input("Masukkan jumlah mobil yang parkir:"))

biaya_motor = motor * harga_motor 
biaya_mobil = mobil * harga_mobil 
total = motor * harga_motor + mobil * harga_mobil 

print("Total biaya parkir motor adalah Rp.", biaya_motor)
print("Total biaya parkir mobil adalah Rp.", biaya_mobil)
print("Total biaya parkir adalah Rp.", total)