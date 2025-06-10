#Program Pemesanan Tiket Pesawat 

print("===Selamat Datang di Pemesanan Tiket Pesawat===")
Nama = input("Masukkan Nama Anda :")
Kota_Asal = input("Masukkan Kota Asal Anda :")
x = 1002600
y = 2142900
z = 665400
print("===============================================")
print("Silahkan Pilih Tujuan Anda")
print("1. Padang - Medan = Rp", x)
print("2. Padang -Jakarta = Rp", y)
print("3. Padang - Batam = Rp", z)

tujuan = int(input("Masukkan Kota Tujuan Anda :"))
if tujuan == 1: 
    print("Silahkan Pilih Tipe Keberangkatan Anda")
    print("1. Perjalanan Untuk Sekali Penerbangan")
    print("2. Perjalanan Pulang Pergi(PP) Diskon 20%")
    tipe_keberangkatan = int(input("Masukkan Tipe Keberangkatan Anda :"))
    if tipe_keberangkatan == 1:
        harga_tiket = x
        print("Harga Tiket Anda Adalah : Rp", harga_tiket)
    elif tipe_keberangkatan == 2:
        harga_tiket1 = (2*x - 20 / 100 * 2*x)
        print("Harga Tiket Anda Adalah : Rp", harga_tiket1)
    else: 
        print("Pilihan Anda Tidak Tersedia")

elif tujuan == 2:
    print("Silahkan Pilih Tipe Keberangkatan Anda")
    print("1. Perjalanan Untuk Sekali Penerbangan")
    print("2. Perjalanan Pulang Pergi(PP) Diskon 20%")
    tipe_keberangkatan = int(input("Masukkan Tipe Keberangkatan Anda :"))
    if tipe_keberangkatan == 1:
        harga_tiket = y
        print("Harga Tiket Anda Adalah : Rp", harga_tiket)
    elif tipe_keberangkatan == 2:
        harga_tiket2 = (2*y - 20 / 100 * 2*y)
        print("Harga Tiket Anda Adalah : Rp", harga_tiket2)
    else: 
        print("Pilihan Anda Tidak Tersedia")

elif tujuan == 3:
    print("Silahkan Pilih Tipe Keberangkatan Anda")
    print("1. Perjalanan Untuk Sekali Penerbangan")
    print("2. Perjalanan Pulang Pergi(PP) Diskon 20%")
    tipe_keberangkatan = int(input("Masukkan Tipe Keberangkatan Anda :"))
    if tipe_keberangkatan == 1:
        harga_tiket = z
        print("Harga Tiket Anda Adalah : Rp", harga_tiket)
    elif tipe_keberangkatan == 2:
        harga_tiket3 = (2*z - 20 / 100 * 2*z)
        print("Harga Tiket Anda Adalah : Rp", harga_tiket3)
    else: 
        print("Pilihan Anda Tidak Tersedia")

else: 
    print("Pilihan Anda Tidak Tersedia")
print("Terimakasih telah menggunakan layanan pemesanan tiket pesawat ini, Hati-hati di Jalan")

print("===============================================")
