data = [
    {"nama": "Vinicius Junior", "umur": 24, "kontrak": 3 ,"nilai_pasar": "3.476,33", "nomor": 7},
    {"nama": "Rodrygo", "umur": 24, "kontrak": 4,"nilai_pasar": "1.738,16", "nomor": 11},
    {"nama": "Arda Guler", "umur": 19, "kontrak": 5 ,"nilai_pasar": "782,17", "nomor": 15},
    {"nama": "Brahim Diaz", "umur": 25, "kontrak": 3 ,"nilai_pasar": "608,36", "nomor": 10},
    {"nama": "Kylian Mbappe", "umur": 26, "kontrak": 5 ,"nilai_pasar": "2.781,06" , "nomor":9}
]

while True:
    print("===Menu===")
    print("1.Tampilkan Data Pemain")
    print("2. Menghapus Data")
    print("3. Menambah Data")
    print("4. Mengganti Data")
    print("5. Berhenti")

    pilihan = int(input("Silahkan masukkan pilihan: "))
    if pilihan ==1:
        print("===Daftar pemain penyerang Real Madrid FC===")
        for i in data:
            print(f"Nama: {i['nama']}, Umur: {i['umur']} Tahun, Kontrak: {i['kontrak']} Tahun, Nilai Pasar: Rp {i['nilai_pasar']} M, Nomor Pemain: {i['nomor']}")
    elif pilihan ==2:
            print("===Daftar pemain penyerang Real Madrid FC===")
            for i in data:
                 print(f"Nama: {i['nama']}, Umur: {i['umur']} Tahun, Kontrak: {i['kontrak']} Tahun, Nilai Pasar: Rp {i['nilai_pasar']} M, Nomor Pemain: {i['nomor']}")
            nomor = int(input("Silahkan masukkan nomor pemain yang ingin dihapus: "))
            ditemukan = False
            for pemain in data:
                if pemain["nomor"] == nomor:
                    data.remove(pemain)
                    print("===Data telah berhasil dihapus===")
                    ditemukan = True
                    break

            if not ditemukan:
                print("===Data tidak ditemukan===")
    elif pilihan ==3:
            nama1 = input("Silahkan masukkan nama pemain: ")
            umur1 = input("Silahkan masukkan umur pemain: ")
            kontrak1 = input("Silahkan masukkan tahun kontrak: ")
            nilai_pasar1 = input("Silahkan masukkan harga nilai pasar: Rp ")
            nomor1 = int(input("Silahkan masukkan nomor pemain: "))
            data.append({"nama": nama1, "umur": umur1, "kontrak": kontrak1,"nilai_pasar": nilai_pasar1, "nomor": nomor1} )
            print("===Data telah berhasil ditambahkan===")
    elif pilihan ==4:
        print("===Daftar pemain penyerang Real Madrid FC===")
        for i in data:
             print(f"Nama: {i['nama']}, Umur: {i['umur']} Tahun, kontrak: {i['kontrak']} Tahun, Nilai Pasar:Rp {i['nilai_pasar']} M, Nomor Pemain: {i['nomor']}")
        nomor = int(input("Silahkan masukkan nomor pemain yang ingin diubah: "))
        ditemukan = False
        for pemain in data:
            if pemain["nomor"] == nomor:
                umur_baru = int(input("Masukkan umur baru: "))
                kontrak_baru = int(input("Masukkan durasi kontrak baru:  "))
                nilai_pasar_baru = input("Masukkan nilai pasar baru: Rp ")
            
                pemain["umur"] = umur_baru
                pemain["kontrak"] = kontrak_baru
                pemain["nilai_pasar"] = nilai_pasar_baru
                print("===Data telah berhasil diubah===")
                ditemukan = True
                break

        if not ditemukan:
            print("===Data tidak ditemukan===")
    elif pilihan ==5:
        print("===Terimakasih telah menggunakan program ini===")
        break 
    else:
        print("Pilihan tidak valid. Silahkan coba lagi!")