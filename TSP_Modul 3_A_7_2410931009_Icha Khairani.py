#Program ATM

print("=== Selamat datang di ATM ===")

#Data Login
nim = 2410931009 
pin = 931009
kesempatan_1 = 3

for kesempatan in range(1, kesempatan_1 + 1):
    PIN = int(input("Silahkan masukkan PIN anda:"))

    if PIN == pin:
        print("Selamat Datang!")
        break
    else:
        print(f"PIN yang anda masukkan salah, kesempatan anda tinggal {kesempatan_1 - kesempatan} x")
        if kesempatan == 3:
            print("Maaf PIN yang anda masukkan salah, Sesi anda telah berakhir")
        continue
    

#Menentukan pilihan transaksi
while True:
    saldo = nim
    print(f"Total saldo anda adalah Rp{saldo}")
    print("=== Pilihan Transaksi ===")
    print("1.Tarik Tunai")
    print("2.Transfer")
    print("3.Setor Tunai")
    transaksi = input("Silahkan pilih transaksi anda:")
    if transaksi == "1":
        jumlah = int(input("Masukkan jumlah yang ingin ditarik :Rp"))
        if jumlah <= saldo:
            saldo -= jumlah
            print(f"Tarik tunai sebesar Rp{jumlah} telah berhasil, sisa saldo anda adalah Rp{saldo}")
        else:
            print("Saldo anda tidak mencukupi")
    elif transaksi == "2":
        rekening_tujuan = int(input("Silahkan masukkan nomor rekening tujuan:"))
        nominal = int(input("Silahkan masukkan nominal yang akan di transfer :Rp"))
        if nominal <= saldo:
            saldo -= nominal
            print(f"Transfer ke rekening{rekening_tujuan} telah berhasil, sisa saldo anda adalah {saldo}")
        else:
            print("Saldo anda tidak mencukupi")
    elif transaksi == "3":
        jumlah = int(input("Silahkan masukkan jumlah yang ingin disetor:Rp"))
        saldo += jumlah
        print(f"Anda telah melakukan setor tunai sebesar Rp{jumlah}, saldo anda sekarang adalah Rp{saldo}")
    else:
        print("Pilihan anda tidak tersedia")
    
    next = input("Apakah anda ingin melakukan transaksi lagi? (y/n)")
    if next == "y":
        continue
    elif next == "n":
        print("===Transaksi anda telah selesai, Terimakasih dan sampai jumpa lagi===")
        break


    


