from data import mobil
from pembayaran import pembayaran

def tampil_mobil():
    print("\nDAFTAR MOBIL")
    for kode, info in mobil.items():
        status = "Tersedia" if info["tersedia"] else "Disewa"
        print(kode, info["nama"], "Rp", info["harga"], status)


def sewa_mobil():
    kode = input("Masukkan kode mobil: ").upper()

    if kode in mobil:
        if mobil[kode]["tersedia"] == False:
            print("Mobil sedang disewa")
            return

        lama = int(input("Lama sewa (hari): "))
        total = mobil[kode]["harga"] * lama
        print("Total bayar: Rp", total)

        bayar = pembayaran(total)

        if bayar == True:
            mobil[kode]["tersedia"] = False
            print("Mobil", mobil[kode]["nama"], "berhasil disewa")
        else:
            print("Sewa dibatalkan")
    else:
        print("Kode mobil tidak ditemukan")

def kembalikan_mobil():
    kode = input("Masukkan kode mobil: ")

    if kode in mobil:
        if mobil[kode]["tersedia"] == True:
            print("Mobil tidak sedang disewa")
        else:
            mobil[kode]["tersedia"] = True
            print("Mobil berhasil dikembalikan")
    else:
        print("Kode mobil tidak ditemukan")
