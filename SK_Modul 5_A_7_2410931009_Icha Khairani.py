#Program Menentukan Peserta yang Lolos Seleksi UTBK Teknik Industri Universitas Andalas 2023

class Data_Peserta_UTBK:
    def __init__ (self, nama, nomor_peserta, skor_UTBK):
        self.nama = nama
        self.nomor_peserta = nomor_peserta
        self.skor_UTBK = skor_UTBK
    def lulus(self, passing_grade = 620):
        if self.skor_UTBK >= passing_grade:
            return True
        else:
            return False 
        
class Seleksi_UTBK:
    def __init__(self):
        self.pesertaUTBK_list = []
    def tambah_peserta(self):
        nama = input("Silahkan masukkan nama peserta: ")
        nomor_peserta = input("Silahkan masukkan nomor peserta: ")
        skor_UTBK = int(input("Silahkan masukkan skor UTBK peserta: "))
        peserta = Data_Peserta_UTBK(nama, nomor_peserta, skor_UTBK)
        self.pesertaUTBK_list.append(peserta)
        print("Data peserta UTBK telah berhasil ditambahkan ")
    def hapus_peserta(self):
        nomor_peserta_hapus = input("Silahkan masukkan nomor peserta yang ingin dihapus: ")
        for i in self.pesertaUTBK_list:
            if i.nomor_peserta == nomor_peserta_hapus:
                self.pesertaUTBK_list.remove(i)
                print(f"Data peserta UTBK dengan nomor peserta {nomor_peserta_hapus} telah berhasil dihapus")
                return
        print(f"Data peserta UTBK dengan nomor peserta {nomor_peserta_hapus} tidak ditemukan")
    def ubah_peserta(self):
        nomor_peserta_ubah = input("Silahkan masukkan nomor peserta yang ingin diubah: ")
        for i in self.pesertaUTBK_list:
            if i.nomor_peserta == nomor_peserta_ubah:
                print(f"Data peserta dengan nomor {nomor_peserta_ubah} telah ditemukan. Silahkan ubah data peserta")
                i.nama = input("Silahkan masukkan nama peserta baru: ")
                i.nomor_peserta = input("Silahkan masukkan nomor peserta baru: ")
                i.skor_UTBK = int(input("Silahkan masukkan skor UTBK baru: "))
                print("Data peserta UTBK telah berhasil diubah/n")
                return
        print(f"Data peserta UTBK dengan nomor peserta {nomor_peserta_ubah} tidak ditemukan")
    def tampilkan_peserta_lolos(self):
        print("\nDaftar Peserta Lolos Seleksi UTBK Teknik Industri Universitas Andalas 2023")
        print("--------------------------------------------------------------------")
        jumlah_peserta_lolos = 0
        for i in self.pesertaUTBK_list:
            if i.lulus():
                print(f"Nama       : {i.nama}")
                print(f"No Peserta : {i.nomor_peserta}")
                print(f"Skor UTBK  : {i.skor_UTBK}")
                print("--------------------------------------------------------------------")
                jumlah_peserta_lolos += 1
        print(f"\nJumlah peserta yang lolos seleksi UTBK adalah {jumlah_peserta_lolos}")
        print("Peserta yang datanya tidak muncul dinyatakan TIDAK LULUS di Teknik Industri Unand 2023.\n")
    def jalan_program_peserta(self):
        print("===Selamat Datang di Program Seleksi UTBK Teknik Industri Universitas Andalas 2023===")
        while True:
            print("===Menu Utama===")
            print("1. Tambahkan Data Peserta UTBK")
            print("2. Hapus Data Peserta UTBK")
            print("3. Ubah Data Peserta UTBK")
            print("4. Tampilkan Peserta Lolos Seleksi UTBK")
            print("5. Keluar")
            pilihan = int(input("Silahkan masukkan pilihan menu (1-5): "))
            if pilihan == 1:
                while len(self.pesertaUTBK_list) < 5:
                    print(f"\nInput data peserta ke-{len(self.pesertaUTBK_list) + 1} (minimal 5 peserta):")
                    self.tambah_peserta()
                while True:
                    tambah_data = input("Apakah anda ingin menambahkan data peserta lagi? (y/n): ")
                    if tambah_data == 'y':
                        print(f"\nInput data peserta ke-{len(self.pesertaUTBK_list) + 1}:")
                        self.tambah_peserta()
                    elif tambah_data == 'n':
                        break
                    else:
                        print("Input tidak valid. Masukkan 'y' untuk ya atau 'n' untuk tidak.")
            elif pilihan == 2:
                self.hapus_peserta()
            elif pilihan == 3:
                self.ubah_peserta()
            elif pilihan == 4:
                print(f"\nTotal peserta yang diinputkan: {len(self.pesertaUTBK_list)}")
                self.tampilkan_peserta_lolos()
            elif pilihan == 5:
                print("===Terima kasih banyak telah menggunakan program ini. Sampai jumpa lagi!===")
                break
            else: 
                print("===Pilihan menu tidak valid. Silahkan coba lagi!===")

#Program Dijalankan 
proses_seleksi = Seleksi_UTBK()
proses_seleksi.jalan_program_peserta()




