from dict import daftarmobil

def tampilkan_mobil_tersedia():
    print("Daftar Mobil Tersedia untuk Disewa:")
    for mobil, info in daftarmobil.items():
        if info["status"] == "tersedia":
            print(f"{mobil} - Tahun: {info['tahun']}, Harga Sewa per Hari: Rp{info['harga_sewa_per_hari']}")
def sewa_mobil(nama_mobil, hari):
    if nama_mobil in daftarmobil:
        if daftarmobil[nama_mobil]["status"] == "tersedia":
            total_harga = daftarmobil[nama_mobil]["harga_sewa_per_hari"] * hari
            daftarmobil[nama_mobil]["status"] = "disewa"
            print(f"Anda telah menyewa {nama_mobil} selama {hari} hari. Total harga: Rp{total_harga}")
        else:
            print(f"Maaf, {nama_mobil} sedang tidak tersedia untuk disewa.")
    else:
        print("Mobil tidak ditemukan dalam daftar.")
def kembalikan_mobil(nama_mobil):
    if nama_mobil in daftarmobil:
        if daftarmobil[nama_mobil]["status"] == "disewa":
            daftarmobil[nama_mobil]["status"] = "tersedia"
            print(f"Terima kasih telah mengembalikan {nama_mobil}.")
        else:
            print(f"{nama_mobil} tidak sedang disewa.")
    else:
        print("Mobil tidak ditemukan dalam daftar.")

def main():
    while True:
        print("\nMenu Rental Mobil:")
        print("1. Tampilkan Mobil Tersedia")
        print("2. Sewa Mobil")
        print("3. Kembalikan Mobil")
        print("4. Keluar")
        pilihan = input("Pilih menu (1-5): ")
        if pilihan == "1":
            tampilkan_mobil_tersedia()
        elif pilihan == "2":
            nama_mobil = input("Masukkan nama mobil yang ingin disewa: ")
            hari = int(input("Masukkan jumlah hari sewa: "))
            sewa_mobil(nama_mobil, hari)
        elif pilihan == "3":
            nama_mobil = input("Masukkan nama mobil yang ingin dikembalikan: ")
            kembalikan_mobil(nama_mobil)
        elif pilihan == "4":
            print("Terima kasih telah menggunakan layanan rental mobil kami.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()