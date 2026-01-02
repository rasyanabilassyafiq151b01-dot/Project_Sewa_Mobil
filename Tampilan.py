from data import daftarmobil

def tampilkan_mobil_tersedia():
    print("Daftar Mobil Tersedia untuk Disewa:")
    for mobil, info in daftarmobil.items():
        if info["status"] == "tersedia":
            print(f"{mobil} - Tahun: {info['tahun']}, Harga Sewa per Hari: Rp{info['harga_sewa_per_hari']}")