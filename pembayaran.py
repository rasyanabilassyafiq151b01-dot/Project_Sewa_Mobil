def pembayaran(total):
    print("\nMETODE PEMBAYARAN")
    print("1. Cash")
    print("2. Transfer")
    print("3. batal")

    pilih = input("Pilih (1-3): ")

    if pilih == "1":
        cash = int(input("Masukan Jumlah Uang Anda:"))
        kembalian = cash - total
        if cash < total:
            print("Maaf Uang Tidak Cukup")
        elif cash > total:
            print("Kembalian Dari Sewa Mobil Anda:", kembalian)
        else:
            print ("Pembayaran Selesai")
        return True 
    elif pilih == "2":
        print("Silahkan Transfer ke Rekening 123-456-789 a.n rental mobil")
        tf = input("Masukkan jumlah yang ditransfer: ")
        if int(tf) < total:
            print("Maaf Uang Tidak Cukup")
            return False
        else:
            print("Pembayaran Selesai")
        return True
    elif pilih == "3":
        print("Pembayaran dibatalkan")
        return False
    else:
        print("Pilihan tidak valid")
        return False