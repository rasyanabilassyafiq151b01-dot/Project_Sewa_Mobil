def pembayaran(total):
    print("\nMETODE PEMBAYARAN")
    print("1. Cash")
    print("2. Transfer")
    print("3. E-Wallet")
    print("4. Batal")

    pilih = input("Pilih (1-4): ")

    if pilih == "4":
        print("Pembayaran dibatalkan")
        return False
    else:
        print("Pembayaran Rp", total, "berhasil")
        return True
