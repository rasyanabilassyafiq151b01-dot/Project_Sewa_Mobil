from sewa import tampil_mobil, sewa_mobil, kembalikan_mobil


while True:
    print("\nMENU SEWA MOBIL")
    print("1. Lihat Mobil")
    print("2. Sewa Mobil")
    print("3. Kembalikan Mobil")
    print("4. Keluar")

    menu = input("Pilih menu: ")

    if menu == "1":
        tampil_mobil()
    elif menu == "2":
        tampil_mobil()
        sewa_mobil()
    elif menu == "3":
        kembalikan_mobil()
    elif menu == "4":
        print("Terima kasih")
        break
    else:
        print("Menu tidak tersedia")