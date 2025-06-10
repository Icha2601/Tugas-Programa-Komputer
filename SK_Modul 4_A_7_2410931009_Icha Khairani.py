#Program Basis Data Band Musik 
data = [
    {"nama" : "Blackpink", "jumlah_personil" : 4, "biaya" : "Rp.2000000"},
    {"nama" : "Twice", "jumlah_personil" : 9, "biaya" : "Rp.2500000"}, 
    {"nama" : "Aespa", "jumlah_personil" : 4, "biaya" : "Rp.1500000"}, 
    {"nama" : "Gfriend", "jumlah_personil" : 6, "biaya" : "Rp.2750000"}, 
    {"nama" : "Apink", "jumlah_personil" : 5, "biaya" : "Rp.1250000"}
] 

# Fungsi untuk menampilkan data band 
while True: 
    print("\n===Menu===")
    print("1. Tampilkan Data Band")
    print("2. Tambah Data Band")
    print("3. Hapus Data Band")
    print("4. Ubah Data Band")
    print("5. Keluar")

    menu = int(input("Masukkan pilihan menu(1-5): "))

    if menu == 1:
        for i in data:
            print(f"Nama Band: {i['nama']}, Jumlah Personil: {i["jumlah_personil"]}, Jumlah Biaya Penampilan: {i["biaya"]}")
    elif menu == 2: 
         nama = input("Masukkan Nama Band: ")
         jumlah_personil = int(input("Masukkan Jumlah Personil: "))
         Jumlah_Biaya_Penampilan = input("Masukkan Jumlah Biaya Penampilan:Rp. ")
         data.append({"nama": nama, "jumlah_personil": jumlah_personil, "biaya": Jumlah_Biaya_Penampilan})
         print("===Data band telah berhasil ditambahkan===")
    elif menu == 3:
        print("\n===Menu===")
        for i in data:
            print(f"Nama Band: {i['nama']}, Jumlah Personil: {i["jumlah_personil"]}, Jumlah Biaya Penampilan: {i["biaya"]}")
        urutan = int(input("Masukkan nomor urutan band yang ingin dihapus: "))-1
        if 0 <= urutan < len(data):
            data.pop(urutan)
            print("===Data band telah berhasil dihapus===")
        else:
            print("===Data band tidak ditemukan. Silahkan coba lagi===")
    elif menu == 4:
       print("\n===Menu===")
       for i in data:
            print(f"Nama Band: {i['nama']}, Jumlah Personil: {i["jumlah_personil"]}, Jumlah Biaya Penampilan: {i["biaya"]}") 
       urutan = int(input("Masukkan nomor urutan band yang ingin diubah: "))-1
       if 0 <= urutan < len(data):
            jumlah_personil = int(input("Masukkan Jumlah Personil Baru: "))
            jumlah_biaya_penampilan = input("Masukkan Jumlah Biaya Penampilan Baru:Rp.  ")
            data[urutan]['jumlah_personil'] = jumlah_personil 
            data[urutan]['biaya'] = jumlah_biaya_penampilan 
            print("===Data band telah berhasil diubah===")
       else:
           print("===Data band tidak ditemukan. Silahkan coba lagi===")

    elif menu == 5: 
        print("===Terima kasih telah menggunakan program ini===")
        break 
    else: 
        print("Pilihan menu tidak valid. Silahkan coba lagi ")
