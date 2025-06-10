#Toko Buku LSIK
import copy
class DataBuku:
    def __init__ (self, jenis, harga, warna_sampul, stok):
        self.jenis = jenis.title()
        self.harga = harga
        self.warna_sampul = warna_sampul.title()
        self.stok = stok

    def __str__ (self):
        return f"Jenis Buku: {self.jenis}, Harga: {self.harga}, Warna Sampul: {self.warna_sampul}, Stok: {self.stok}"
    
class TokoBuku: 
    def __init__ (self):
        self.buku = [
            DataBuku("Novel", 75000, "Putih", 10),
            DataBuku("Pendidikan", 50000, "Putih", 15),
            DataBuku("Biografi", 35000, "Kuning", 20)
        ]
        self.buku_awal = copy.deepcopy(self.buku)
    
    def tampilkan_daftar_buku(self):
        print("\nDaftar Buku Toko LSIK\n")
        for i in self.buku:
            print(i)

    def tambah_daftar_buku(self, jenis, harga, warna_sampul, stok):
        daftar_buku_baru = DataBuku(jenis, harga, warna_sampul, stok)
        self.buku.append(daftar_buku_baru)

    def hapus_daftar_buku(self, jenis):
        for i in self.buku:
            if i.jenis.title() == jenis.title():
                self.buku.remove(i)
                return True
        return False
    
    def cari_buku(self, jenis = None, warna_sampul = None):
        pencarian = [i for i in self.buku 
                     if (jenis is None or i.jenis.lower() == jenis.lower()) and
                     (warna_sampul is None or i.warna_sampul.lower()== warna_sampul.lower())                  
                     ]
        if pencarian:
            print("\nHasil Pencarian Buku\n")
            for i in pencarian:
                print(i)
        else:
            print("\nBuku Tidak ditemukan. Silahkan coba lagi\n")

    def jalan_program_buku(self):
        print("Selamat Datang di Toko Buku LSIK")
        while True:
            print("===Menu===")
            print("1. Tampilkan Daftar Buku")
            print("2. Tambah Daftar Buku")
            print("3. Hapus Daftar Buku")
            print("4. Menampilkan daftar buku awal dan setelah perubahan")
            print("5. Cari Buku")
            print("6. Keluar")
            while True:
                try:
                    pilihan = int(input("Silahkan masukkan pilihan anda: "))
                    break
                except ValueError:
                    print("===Pilihan tidak valid. Silahkan masukkan angka dari 1-6===")
                print("\n=========================================================\n")

            if pilihan == 1:
                self.tampilkan_daftar_buku()
                print("\n=========================================================\n")

            elif pilihan == 2:

                jenis = input("Silahkan masukkan jenis buku: ").title()
                harga = int(input("Silahkan masukkan harga buku: "))
                warna_sampul = input("Silahkan masukkan warna sampul buku: ").title()
                stok = int(input("Silahkan masukkan jumlah stok buku: "))
                self.tambah_daftar_buku(jenis, harga, warna_sampul, stok)

                print("Buku telah berhasil ditambahkan ke daftar")
                
                print("\n=========================================================\n")
            elif pilihan == 3:
                
                jenis = input("Silahkan masukkan jenis buku yang ingin di hapus: ").title()
                if self.hapus_daftar_buku(jenis):
                    print(f"===Buku {jenis} telah berhasil dihapus===")
                else:
                    print(f"Buku {jenis} tidak ditemukan. Silahkan coba lagi!")
                
                print("Buku telah berhasil di hapus dari daftar")
                
                print("\n=========================================================\n")

            elif pilihan == 4:
                print("===Daftar Buku Awal===")
                for i in self.buku_awal:
                    print(i)
                print("\n===Daftar Buku Setelah Perubahan===")
                for i in self.buku:
                    print(i)
                print("\n=========================================================\n")
                  
            elif pilihan == 5: 
                jenis = input("Silahkan masukkan jenis buku yang ingin di cari(kosongkan jika ingin mencari dengan warna sampul buku): ").title()
                warna_sampul = input("Silahkan masukkan warna sampul buku yang ingin di cari(kosongkan jika ingin mencari dengan jenis buku): ").title()
                self.cari_buku(jenis=jenis if jenis else None, warna_sampul=warna_sampul if warna_sampul else None)
                print("\n=========================================================\n")
                
            elif pilihan == 6: 
                print("===Terima kasih telah menggunakan program Toko Buku LSIK===")
                print("===Sampai Jumpa Lagi===")
                break

            else: 
                print("===Pilihan Tidak Valid. Silahkan coba lagi!===")

Toko = TokoBuku()
Toko.jalan_program_buku()
