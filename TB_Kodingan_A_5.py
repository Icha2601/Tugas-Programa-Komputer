import os
from colorama import init, Fore, Back, Style
init(autoreset=True)

lebar = 163 # Lebar layar yang diinginkan

def tengah_manual(teks):
    try:
        lebar_terminal = os.get_terminal_size().columns
    except OSError:
        lebar_terminal = 163
    margin = max((lebar_terminal - len(teks)) // 2, 0)
    return " " * margin + teks

class Login: 
    def __init__(self,tanaman,hargapasar,hargakomoditas):
        self.akun_list =[
            {"username": "101admin", "password": "admin123"},
            {"username": "102icha", "password": "icha123"},
            {"username": "102raffa", "password": "raffa123"},
            {"username": "102faiz", "password": "faiz123"},
            
        ]
        self.tanaman=tanaman
        self.hargapasar=hargapasar 
        self.hargakomoditas=hargakomoditas 

    def tampilkan_awal(self):
        print(Fore.WHITE)
        print(("=" * 80).center(163))
        print("")
        print("TUGAS BESAR".center(163))
        print("PROGRAM KOMPUTER".center(163))
        print("")
        print("Pengembangan Aplikasi Pengolahan Pertanian Hortikultura Berbasis Web".center(163))
        print("(Studi Kasus: Desa Wonosari Kecamatan Tutur)".center(163))
        print("")
        print("OLEH:".center(163))
        print("Kelompok 5A".center(163))
        print("")
        print("Anggota:".center(163))
        print("M. Raffa Fahrezi             (2410931017)".center(163))
        print("Icha Khairani                (2410931009)".center(163))
        print("Faiz Anadel Kurnia           (2410933009)".center(163))
        print("")
        print("Asisten Pembimbing:".center(163))
        print("Ridwan Leo Candra".center(163))
        print("")
        print("Dosen:".center(163))
        print("Dr.Eng Ardhian Agung Yulianto S.Kom, M.T".center(163))
        print("")
        print("LABORATORIUM SISTEM INFORMASI DAN KEPUTUSAN".center(163))
        print("DEPARTEMEN TEKNIK INDUSTRI".center(163))
        print("FAKULTAS TEKNIK".center(163))
        print("UNIVERSITAS ANDALAS".center(163))
        print("2025".center(163))
        print("")
        print(("=" * 80).center(163))
        print("")
        print("=" * 147)
        print(Fore.GREEN + "🌿 SELAMAT DATANG DI SISTEM INFORMASI HORTIKULTURA 🌿".center(lebar))
        print("=" * 147)
        print(Fore.GREEN + "Aplikasi ini membantu Anda mengelola data tanaman,".center(lebar))
        print(Fore.GREEN + "harga pasar, dan harga komoditas hortikultura.".center(lebar))
        print(Fore.GREEN + "Silakan login atau registrasi untuk melanjutkan".center(lebar))
        print("=" * 147)
        print ()

    def registrasi(self):
        print((Back.BLUE + Fore.WHITE + "=== REGISTRASI AKUN ===".center(lebar) + Style.BRIGHT))
        username = input(Fore.GREEN + "Silahkan masukkan username (harus diawali dengan 102): ") 
        password = input(Fore.GREEN + "Silahkan masukkan password: ") 
        if not username.startswith("102"):
            print((Back.RED + Fore.WHITE + "REGISTRASI GAGAL! USERNAME HARUS DIAWALI DENGAN 102. SILAHKAN COBA LAGI!".center(lebar)) + Style.BRIGHT)
            return
        for akun in self.akun_list:
            if akun["username"] == username:
                print((Back.RED + Fore.WHITE + "REGISTRASI GAGAL! USERNAME SUDAH TERDAFTAR. SILAHKAN COBA LAGI!".center(lebar)) + Style.BRIGHT)
                return
        self.akun_list.append({"username": username, "password": password})
        print((Back.BLUE + Fore.WHITE + "REGISTRASI BERHASIL! SILAHKAN LOGIN UNTUK MELANJUTKAN.".center(lebar)) + Style.BRIGHT)

    def login(self):
        print((Back.BLUE + Fore.WHITE + "=== LOGIN AKUN ===".center(lebar)) + Style.BRIGHT)
        username = input(Fore.GREEN + "Silahkan masukkan username: ") 
        password = input(Fore.GREEN + "Silahkan masukkan password: ") 

        for akun in self.akun_list:
            if akun["username"] == username and akun["password"] == password:
                if username.startswith("101"):
                    print((Back.BLUE + Fore.WHITE + "LOGIN SEBAGAI ADMIN BERHASIL.".center(lebar)) + Style.BRIGHT)

                    admin=Admin(self.tanaman,self.hargapasar,self.hargakomoditas)
                    admin.menu()

                elif username.startswith("102"):
                    print((Back.BLUE + Fore.WHITE + "LOGIN SEBAGAI PENGUNJUNG BERHASIL.".center(lebar)) + Style.BRIGHT)
                    pengunjung=Pengunjung(self.tanaman,self.hargapasar,self.hargakomoditas, self.akun_list, username)
                    pengunjung.menu()
                return
        print((Back.RED + Fore.WHITE + "LOGIN GAGAL! USERNAME ATAU PASSWORD SALAH. SILAHKAN COBA LAGI!".center(lebar)) + Style.BRIGHT)

    def menu(self):
        self.tampilkan_awal()
        while True:
            print(Fore.WHITE + "=" * 42)
            print(Fore.WHITE + "|{:^40}|".format("SELAMAT DATANG DI SISTEM HORTIKULTURA"))
            print(Fore.WHITE + "=" * 42)
            print(Fore.WHITE + "| {:<2} | {:<33} |".format("1", "Registrasi"))
            print(Fore.WHITE + "| {:<2} | {:<33} |".format("2", "Login"))
            print(Fore.WHITE + "| {:<2} | {:<33} |".format("3", "Keluar"))
            print(Fore.WHITE + "=" * 42)
            pil = input(Fore.YELLOW + "Silahkan masukkan pilihan: ")
            if pil == "1":
                self.registrasi()
            elif pil == "2":
                self.login()
            elif pil == "3":
                print((Back.BLUE + Fore.WHITE + "🌿 TERIMA KASIH TELAH MENGGUNAKAN SISTEM INFORMASI HORTIKULTURA. SELAMAT BERKEBUN DAN SEMOGA PANENMU MELIMPAH! 🌿".center(lebar)) + Style.BRIGHT)
                break
            else:
                print((Back.RED + Fore.WHITE + "PILIHAN TIDAK VALID. SILAHKAN COBA LAGI!".center(lebar)) + Style.BRIGHT)

class Admin :
    def __init__(self,tanaman,hargapasar,hargakomoditas):
        self.tanaman=tanaman
        self.hargapasar=hargapasar
        self.hargakomoditas=hargakomoditas

    def menu(self):
        while True:
            print( "=" * 42)
            print(Fore.WHITE + "|{:^40}|".format("MENU UTAMA"))
            print(Fore.WHITE + "=" * 42)
            print(Fore.WHITE + "| {:<2} | {:<33} |".format("1", "Kelola Data Tanaman"))
            print(Fore.WHITE + "| {:<2} | {:<33} |".format("2", "Kelola Harga Pasar"))
            print(Fore.WHITE + "| {:<2} | {:<33} |".format("3", "Kelola Komoditas"))
            print(Fore.WHITE + "| {:<2} | {:<33} |".format("0", "Keluar Program"))
            print(Fore.WHITE + "=" * 42)
            pilihan = input(Fore.YELLOW + "Silahkan masukkan pilihan: ") 
            if pilihan == "1":
                while True :
                    print(Fore.WHITE + "=" * 50)
                    print(Fore.WHITE + "|{:^48}|".format("KELOLA DATA TANAMAN"))
                    print(Fore.WHITE + "=" * 50)
                    print(Fore.WHITE + "| {:<2} | {:<41} |".format("a", "Melihat data tanaman"))
                    print(Fore.WHITE + "| {:<2} | {:<41} |".format("b", "Menambah data tanaman"))
                    print(Fore.WHITE + "| {:<2} | {:<41} |".format("c", "Menghapus data tanaman"))
                    print(Fore.WHITE + "| {:<2} | {:<41} |".format("d", "Mengubah data tanaman"))
                    print(Fore.WHITE + "| {:<2} | {:<41} |".format("e", "Kembali"))
                    print(Fore.WHITE + "=" * 50)
                    p = input(Fore.YELLOW + "Silahkan masukkan pilihan: ")
                    if p.lower() == "a" :
                        self.tanaman.tampiltanaman()
                    elif p.lower() == "b" :
                        self.tanaman.tambahtanaman()
                    elif p.lower() == "c" :
                        self.tanaman.hapustanaman()
                    elif p.lower() == "d" :
                        self.tanaman.ubahtanaman()
                    elif p.lower() == "e" :
                        print((Back.BLUE + Fore.WHITE + "TERIMA KASIH. SILAHKAN KEMBALI KE MENU UTAMA.".center(lebar)) + Style.BRIGHT)
                        break
                    else :
                        print((Back.RED + Fore.WHITE + "PILIHAN TIDAK TERSEDIA. SILAHKAN COBA LAGI!".center(lebar)) + Style.BRIGHT)
                        continue
            elif pilihan == "2":
                while True:
                    print(Fore.WHITE + "=" * 54)
                    print(Fore.WHITE + "|{:^52}|".format("KELOLA HARGA PASAR"))
                    print(Fore.WHITE + "=" * 54)
                    print(Fore.WHITE + "| {:<2} | {:<45} |".format("a", "Melihat data harga pasar"))
                    print(Fore.WHITE + "| {:<2} | {:<45} |".format("b", "Menambah data harga pasar"))
                    print(Fore.WHITE + "| {:<2} | {:<45} |".format("c", "Menghapus data harga pasar"))
                    print(Fore.WHITE + "| {:<2} | {:<45} |".format("d", "Mengubah data harga pasar"))
                    print(Fore.WHITE + "| {:<2} | {:<45} |".format("e", "Kembali"))
                    print(Fore.WHITE + "=" * 54)

                    p = input(Fore.YELLOW + "Silahkan masukkan pilihan: ") 
                    if p.lower() == "a" :
                        self.hargapasar.tampilhargapasar()
                    elif p.lower() == "b" :
                        self.hargapasar.tambahhargapasar()
                    elif p.lower() == "c" :
                        self.hargapasar.hapushargapasar()
                    elif p.lower() == "d" :
                        self.hargapasar.ubahhargapasar()
                    elif p.lower() == "e" :
                        print((Back.BLUE + Fore.WHITE + "TERIMA KASIH. SILAHKAN KEMBALI KE MENU UTAMA.".center(lebar)) + Style.BRIGHT)
                        break
                    else :
                        print((Back.RED + Fore.WHITE + "PILIHAN TIDAK TERSEDIA. SILAHKAN COBA LAGI!".center(lebar)) + Style.BRIGHT)
            elif pilihan == "3":
                while True:
                    print(Fore.WHITE + "=" * 60)
                    print(Fore.WHITE + "|{:^58}|".format("KELOLA HARGA KOMODITAS"))
                    print(Fore.WHITE + "=" * 60)
                    print(Fore.WHITE + "| {:<2} | {:<51} |".format("a", "Melihat data harga komoditas"))
                    print(Fore.WHITE + "| {:<2} | {:<51} |".format("b", "Menambah data harga komoditas"))
                    print(Fore.WHITE + "| {:<2} | {:<51} |".format("c", "Menghapus data harga komoditas"))
                    print(Fore.WHITE + "| {:<2} | {:<51} |".format("d", "Mengubah data harga komoditas"))
                    print(Fore.WHITE + "| {:<2} | {:<51} |".format("e", "Kembali"))
                    print(Fore.WHITE + "=" * 60)

                    p = input(Fore.YELLOW + "Silahkan masukkan pilihan: ")
                    if p.lower() == "a" :
                        self.hargakomoditas.tampilhargakomoditas()
                    elif p.lower() == "b" :
                        self.hargakomoditas.tambahhargakomoditas()
                    elif p.lower() == "c" :
                        self.hargakomoditas.hapushargakomoditas()
                    elif p.lower() == "d" :
                        self.hargakomoditas.ubahhargakomoditas() 
                    elif p.lower() == "e" :
                        print((Back.BLUE + Fore.WHITE + "TERIMA KASIH. SILAHKAN KEMBALI KE MENU UTAMA.".center(lebar)) + Style.BRIGHT)
                        break
                    else :
                        print((Back.RED + Fore.WHITE + "PILIHAN TIDAK TERSEDIA. SILAHKAN COBA LAGI!".center(lebar)) + Style.BRIGHT)
                        continue
            elif pilihan == "0":
                print(Back.BLUE + Fore.WHITE + "TERIMA KASIH. SILAHKAN KEMBALI KE MENU UTAMA.".center(lebar)) 
                return
            else :
                print((Back.RED + Fore.WHITE + "PILIHAN TIDAK TERSEDIA. SILAHKAN COBA LAGI!".center(lebar)) + Style.BRIGHT)

class Pengunjung:
    def __init__(self,tanaman,hargapasar,hargakomoditas, akun_list, username):
        self.tanaman=tanaman
        self.hargapasar=hargapasar
        self.hargakomoditas=hargakomoditas
        self.akun_list = akun_list
        self.username = username
        
    def tampilkan_profil(self):
        for akun in self.akun_list:
            if akun["username"] == self.username:
                print(Back.BLUE + Fore.WHITE + "=== PROFIL PENGUNJUNG ===".center(lebar))
                print(Fore.BLUE + "="* 163) 
                print(f"Username: {akun['username']}")
                print(Fore.BLUE + "="* 163)
                return
        print((Back.RED + Fore.WHITE + "PROFIL TIDAK DITEMUKAN. SILAHKAN COBA LAGI!".center(lebar)) + Style.BRIGHT)

    def ubah_password(self):
        for akun in self.akun_list:
            if akun["username"] == self.username:
                current_pass = input("Silahkan masukkan password lama: ")
                if current_pass != akun["password"]:
                    print((Back.RED + Fore.WHITE + "PASSWORD LAMA SALAH! SILAHKAN COBA LAGI!".center(lebar)) + Style.BRIGHT)
                    return
                new_pass = input("Silahkan masukkan password baru: ")
                konfirmasi = input("Silahkan konfirmasi password baru: ")
                if new_pass != konfirmasi:
                    print((Back.RED + Fore.WHITE + "KONFIRMASI PASSWORD TIDAK COCOK!".center(lebar)) + Style.BRIGHT)
                    return
                akun["password"] = new_pass
                print((Back.BLUE + Fore.WHITE + "PASSWORD BERHASIL DIUBAH!".center(lebar)) + Style.BRIGHT)
                return
        print((Back.RED + Fore.WHITE + "PROFIL TIDAK DITEMUKAN.".center(lebar)) + Style.BRIGHT)

    def menu (self) :
        while True:
            print(Fore.WHITE + "=" * 50)
            print(Fore.WHITE + "|{:^48}|".format("MENU PENGUNJUNG"))
            print(Fore.WHITE + "=" * 50)
            print(Fore.WHITE + "| {:<2} | {:<41} |".format("1", "Lihat Data Tanaman"))
            print(Fore.WHITE + "| {:<2} | {:<41} |".format("2", "Lihat Harga Pasar"))
            print(Fore.WHITE + "| {:<2} | {:<41} |".format("3", "Lihat Harga Komoditas"))
            print(Fore.WHITE + "| {:<2} | {:<41} |".format("4", "Lihat Profil & Ubah Password"))
            print(Fore.WHITE + "| {:<2} | {:<41} |".format("0", "Kembali"))
            print(Fore.WHITE + "=" * 50)
            pilihan = input(Fore.YELLOW + "Silahkan masukkan pilihan: ") 
            if pilihan == "1":
                self.tanaman.tampiltanaman()
            elif pilihan == "2":
                self.hargapasar.tampilhargapasar()
            elif pilihan == "3":
                self.hargakomoditas.tampilhargakomoditas()
            elif pilihan == "4":
                self.tampilkan_profil()
                pil = input(Fore.YELLOW + "Apakah Anda ingin mengubah password? (y/n): ")
                if pil.lower() == "y":
                    self.ubah_password()
                elif pil.lower() == "n":
                    continue
                else:
                    print((Back.RED + Fore.WHITE + "PILIHAN TIDAK VALID. SILAHKAN COBA LAGI !".center(lebar)) + Style.BRIGHT)

            elif pilihan == "0":
                print((Back.BLUE + Fore.WHITE + "TERIMA KASIH. SILAHKAN KEMBALI KE MENU UTAMA.".center(lebar)) + Style.BRIGHT)
                return
            else:
                print((Back.RED + Fore.WHITE + "PILIHAN TIDAK VALID. SILAHKAN COBA LAGI!".center(lebar)) + Style.BRIGHT)

class Tanaman:
    def __init__(self, nama, jenis, teknik, masa, warna):
        self.nama = nama
        self.jenis = jenis
        self.teknik = teknik
        self.masa = masa
        self.warna = warna

class DaftarTanaman:
    def __init__(self):
        self.tanamanlist = [
            Tanaman("Mangga", "Buah", "Cangkok", "5 Bulan", "Hijau Kekuningan"),
            Tanaman("Tomat", "Sayur", "Irigasi Tetes", "3 Bulan", "Merah"),
            Tanaman("Bayam", "Sayuran", "Tanam Langsung", "1 Bulan", "Hijau"),
            Tanaman("Mentimun", "Sayur", "Irigasi Tetes", "2 Bulan", "Hijau"),
            Tanaman("Jeruk", "Buah", "Cangkok", "4 Bulan", "Oranye"),
            Tanaman("Jahe", "Herbal", "Tanam Langsung", "6 Bulan", "Coklat muda"),
            Tanaman("Sereh", "Herbal", "Stek", "5 Bulan", "Hijau"),
            Tanaman("Cabai", "Sayur", "Semai", "2 Bulan", "Merah"),
            Tanaman("Bawang Merah", "Sayur", "Tanam Langsung", "2 Bulan", "Merah Muda"),
            Tanaman("Kangkung", "Sayur", "Hidroponik", "1 Bulan", "Hijau"), 
            Tanaman("Melon", "Buah", "Irigasi Tetes", "3 Bulan", "Kuning Hijau")
        ]

    def tampiltanaman(self):
        if not self.tanamanlist:
            print((Back.RED + Fore.WHITE + "DATA TANAMAN MASIH KOSONG.".center(lebar)) + Style.BRIGHT) 
        else:
            print((Back.BLUE + Fore.WHITE + "INFORMASI DATA TANAMAN".center(lebar)) + Style.BRIGHT)
            header = f"| {'No.':^4} | {'Nama':^15} | {'Jenis':^12} | {'Teknik Menanam':^22} | {'Masa Panen':^14} | {'Warna':^20} |"
            garis = "-" * len(header)
            print(tengah_manual(garis))
            print(tengah_manual("    " + Fore.GREEN + header))
            print(tengah_manual(garis))
            for i, tanaman in enumerate(self.tanamanlist, start=1):
                baris = f"| {i:^4} | {tanaman.nama:^15} | {tanaman.jenis:^12} | {tanaman.teknik:^22} | {tanaman.masa:^14} | {tanaman.warna:^20} |"
                print(tengah_manual(baris))
                print(tengah_manual(garis))

    def tambahtanaman(self):
        nama=input("Silahkan masukkan nama tanaman baru: ").title()
        jenis=input("Silahkan masukkan jenis tanaman baru: ").title()
        teknik=input("Silahkan masukkan teknik menanam baru : ").title()
        masa=input("Silahkan masukkan masa panen baru: ").title()
        warna=input("Silahkan masukkan warna baru : ").title()

        tanamanbr=Tanaman(nama,jenis,teknik,masa,warna)
        self.tanamanlist.append(tanamanbr)
        print((Back.GREEN + Fore.BLACK + f"TANAMAN ({nama}) BERHASIL DITAMBAHKAN!".center(lebar)) + Style.BRIGHT)

    def hapustanaman(self):
        nama=input("Silahkan masukkan nama tanaman yang akan dihapus : ")
        terhapus=False
        for tanaman in self.tanamanlist :
            if tanaman.nama.title() == nama.title() :
                self.tanamanlist.remove(tanaman)
                print ((Back.GREEN + Fore.BLACK + f"TANAMAN ({nama}) BERHASIL DIHAPUS!".center(lebar)) + Style.BRIGHT)
                terhapus=True
        if not terhapus:
            print((Back.RED + Fore.WHITE + "TANAMAN TIDAK DITEMUKAN, HARAP DISESUAIKAN DENGAN DATA!".center(lebar)) + Style.BRIGHT)

    def ubahtanaman(self) :
        print((Back.BLUE + Fore.WHITE + "== MENGUBAH DATA TANAMAN ==".center(lebar)) + Style.BRIGHT)
        namatnm=input("Silahkan masukkan nama tanaman yang akan diubah: ")
        while True :
            for i in self.tanamanlist:
                if i.nama.title() == namatnm.title():
                    namabr=input("Silahkan masukkan nama tanaman baru: ").title()
                    jenisbr=input("Silahkan masukkan jenis tanaman baru: ").title()
                    teknikbr=input("Silahkan masukkan teknik menanam baru : ").title()
                    masabr=input("Silahkan masukkan masa panen baru: ").title()
                    warnabr=input("Silahkan masukkan warna baru : ").title()
                    i.nama=namabr
                    i.jenis=jenisbr
                    i.teknik=teknikbr
                    i.masa=masabr
                    i.warna=warnabr

                    print((Back.GREEN + Fore.BLACK + f"DATA TANAMAN {namatnm} BERHASIL DIUBAH!".center(lebar)) + Style.BRIGHT)
                    break
            else :
                print((Back.RED + Fore.WHITE + "DATA TIDAK DITEMUKAN, HARAP DISESUAIKAN DENGAN DATA".center(lebar)) + Style.BRIGHT)
            break     
class Hargapasar:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

class DaftarHargapasar:
    def __init__(self):
        self.hargapasarlist = [
            Hargapasar("Mangga", 15000),
            Hargapasar("Tomat", 50000),
            Hargapasar("Bayam", 6000),
            Hargapasar("Mentimun", 8000),
            Hargapasar("Jeruk", 12000),
            Hargapasar("Jahe", 10000),
            Hargapasar("Sereh", 7000),  
            Hargapasar("Cabai", 30000),
            Hargapasar("Bawang Merah", 25000),
            Hargapasar("Kangkung", 4000),
            Hargapasar("Melon", 20000)

        ]

    def tampilhargapasar(self):
        if not self.hargapasarlist:
            print((Back.RED + Fore.WHITE + "DATA HARGA PASAR MASIH KOSONG.".center(lebar)) + Style.BRIGHT)
        else:
            print((Back.BLUE + Fore.WHITE + "=== HARGA PASAR ===".center(lebar)) + Style.BRIGHT)
            print((Fore.GREEN + "Harga pasar adalah harga setelah masuk ke rantai distribusi".center(lebar)) + Style.BRIGHT)
            header = f"| {'No.':^4} | {'Nama':^20} | {'Harga (Rp)':^15} |"
            garis = "-" * len(header)
            print(tengah_manual(garis))
            print(tengah_manual("     " +Fore.GREEN+header))
            print(tengah_manual(garis))
            for i, item in enumerate(self.hargapasarlist, start=1):
                baris = f"| {i:^4} | {item.nama:^20} | {item.harga:^15,} |"
                print(tengah_manual(baris))
                print(tengah_manual(garis))

    def tambahhargapasar(self):
        nama=input("Silahkan masukkan nama tanaman baru: ").title()
        while True:
            try:
                harga=int(input("Silahkan masukkan harga pasar baru (Rp.):  "))
                break
            except ValueError:
                print((Back.RED + Fore.WHITE + "INPUT TIDAK VALID. HARAP MASUKKAN ANGKA.".center(lebar)) + Style.BRIGHT)

        hargapasarbr=Hargapasar(nama,harga)
        self.hargapasarlist.append(hargapasarbr)
        print((Back.GREEN + Fore.BLACK + f"HARGA PASAR ({nama}) BERHASIL DITAMBAHKAN!".center(lebar)) + Style.BRIGHT)

    def hapushargapasar(self):
        nama=input("Silahkan masukkan nama tanaman yang akan dihapus : ").title()
        terhapus=False
        for hargapasar in self.hargapasarlist :
            if hargapasar.nama.title() == nama.title() :
                self.hargapasarlist.remove(hargapasar)
                print((Back.GREEN + Fore.BLACK + f"HARGA PASAR ({nama}) BERHASIL DIHAPUS!".center(lebar)) + Style.BRIGHT)
                terhapus=True
        if not terhapus:
            print((Back.RED + Fore.WHITE + "HARGA PASAR TIDAK DITEMUKAN, HARAP DISESUAIKAN DENGAN DATA!".center(lebar)) + Style.BRIGHT)
    def ubahhargapasar(self):
        print((Back.BLUE + Fore.WHITE + "== MENGUBAH DATA HARGA PASAR ==".center(lebar)) + Style.BRIGHT)
        nama=input("Silahkan masukkan nama tanaman yang akan diubah: ").title()
        while True:
            for i in self.hargapasarlist:
                if i.nama.title() == nama.title():
                    namabr=input("Silahkan masukkan nama tanaman baru: ").title()
                    while True:
                        try:
                            hargabr=int(input("Silahkan masukkan harga baru (Rp.): "))
                            break
                        except ValueError:
                            print((Back.RED + Fore.WHITE + "INPUT TIDAK VALID. HARAP MASUKKAN ANGKA.".center(lebar)) + Style.BRIGHT)
                    i.nama=namabr
                    i.harga=hargabr
                    print((Back.GREEN + Fore.BLACK + f"DATA HARGA PASAR {nama} BERHASIL DIUBAH!".center(lebar)) + Style.BRIGHT)
                    break
            else :
                print((Back.RED + Fore.WHITE + "DATA HARGA PASAR TIDAK DITEMUKAN, HARAP DISESUAIKAN DENGAN DATA".center(lebar)) + Style.BRIGHT)
            break

class Hargakomoditas:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga
    
class DaftarHargakomoditas:
    def __init__(self):
        self.hargakomoditaslist = [
            Hargakomoditas("Mangga", 10000),
            Hargakomoditas("Tomat", 30000),
            Hargakomoditas("Bayam", 4000),
            Hargakomoditas("Mentimun", 6000),
            Hargakomoditas("Jeruk", 9000),
            Hargakomoditas("Jahe", 8000),
            Hargakomoditas("Sereh", 5000),  
            Hargakomoditas("Cabai", 25000),
            Hargakomoditas("Bawang Merah", 20000),
            Hargakomoditas("Kangkung", 2000),
            Hargakomoditas("Melon", 15000)
        ]

    def tampilhargakomoditas(self):
        if not self.hargakomoditaslist:
            print((Back.RED + Fore.WHITE + "DATA HARGA KOMODITAS MASIH KOSONG.".center(lebar)) + Style.BRIGHT)
        else:
            print((Back.BLUE + Fore.WHITE + "== HARGA KOMODITAS ==".center(lebar)) + Style.BRIGHT)
            print((Fore.GREEN + "Harga komoditas adalah harga sebelum masuk ke rantai distribusi dan diterima langsung dari petani".center(lebar)) + Style.BRIGHT)
            header = f"| {'No.':^4} | {'Nama':^20} | {'Harga (Rp)':^15} |"
            garis = "-" * len(header)
            print(tengah_manual(garis))
            print(tengah_manual("     " + Fore.GREEN + header))
            print(tengah_manual(garis))
            for i, item in enumerate(self.hargakomoditaslist, start=1):
                baris = f"| {i:^4} | {item.nama:^20} | {item.harga:^15,} |"
                print(tengah_manual(baris))
                print(tengah_manual(garis))

    def tambahhargakomoditas(self):
        nama=input("Silahkan masukkan nama komoditas baru: ").title()
        while True:
            try:
                harga=int(input("Silahkan masukkan harga komoditas baru (Rp.): "))
                break
            except ValueError:
                print((Back.RED + Fore.WHITE + "INPUT TIDAK VALID. HARAP MASUKKAN ANGKA.".center(lebar)) + Style.BRIGHT)
        hargakomoditasbr=Hargakomoditas(nama,harga)
        self.hargakomoditaslist.append(hargakomoditasbr)
        print((Back.GREEN + Fore.BLACK + f"HARGA KOMODITAS ({nama}) BERHASIL DITAMBAHKAN!".center(lebar)) + Style.BRIGHT)
        pass

    def hapushargakomoditas(self):
        nama=input("Silahkan masukkan nama tanaman yang akan dihapus : ").title()
        terhapus=False
        for hargakomoditas in self.hargakomoditaslist :
            if hargakomoditas.nama.title() == nama.title() :
                self.hargakomoditaslist.remove(hargakomoditas)
                print((Back.GREEN + Fore.BLACK + f"HARGA KOMODITAS ({nama}) BERHASIL DIHAPUS!".center(lebar)) + Style.BRIGHT)
                terhapus=True
        if not terhapus:
            print((Back.RED + Fore.WHITE + "HARGA KOMODITAS TIDAK DITEMUKAN, HARAP DISESUAIKAN DENGAN DATA!".center(lebar)) + Style.BRIGHT)
    def ubahhargakomoditas(self):
        print((Back.BLUE + Fore.WHITE + "== MENGUBAH DATA HARGA KOMODITAS ==".center(lebar)) + Style.BRIGHT)
        nama=input("Silahkan masukkan nama komoditas yang akan diubah: ").title()
        while True:
            for i in self.hargakomoditaslist:
                if i.nama.title() == nama.title():
                    namabr=input("Silahkan masukkan nama komoditas baru: ").title()
                    while True:
                        try:
                            hargabr=int(input("Silahkan masukkan harga baru (Rp.): "))
                            break
                        except ValueError: 
                            print(tengah_manual(Back.RED + Fore.WHITE + "INPUT TIDAK VALID. HARAP MASUKKAN ANGKA.".center(lebar)) + Style.BRIGHT)
                    i.nama=namabr
                    i.harga=hargabr
                    print((Back.GREEN + Fore.BLACK + f"DATA HARGA KOMODITAS {nama} BERHASIL DIUBAH!".center(lebar)) + Style.BRIGHT)
                    break
            else :
                print((Back.RED + Fore.WHITE + "DATA HARGA KOMODITAS TIDAK DITEMUKAN, HARAP DISESUAIKAN DENGAN DATA".center(lebar)) + Style.BRIGHT)
            break
            
if __name__ == "__main__":
    tanaman = DaftarTanaman()
    hargapasar=DaftarHargapasar()
    hargakomoditas=DaftarHargakomoditas()
    proses = Login(tanaman,hargapasar,hargakomoditas)
    proses.menu()
                
