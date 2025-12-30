# 1. Data Barang (bisa diganti sesuai kebutuhan)
daftar_harga = {
    "kopi": 5000,
    "teh": 4000,
    "roti": 3000,
    "air mineral": 2000
}

# 2. Variabel untuk menyimpan keranjang belanja
keranjang = []
total_belanja = 0

print("===== Selamat Datang di Toko Sederhana =====")

# 3. Loop untuk input barang
while True:
    nama_barang = input("Masukkan nama barang (atau 'selesai' untuk selesai): ").lower()
    if nama_barang == 'selesai':
        break # Keluar dari loop jika user mengetik 'selesai'

    if nama_barang in daftar_harga:
        jumlah = int(input(f"Jumlah {nama_barang}: "))
        harga_total_item = daftar_harga[nama_barang] * jumlah
        keranjang.append({
            'nama': nama_barang,
            'jumlah': jumlah,
            'harga_satuan': daftar_harga[nama_barang],
            'total_item': harga_total_item
        })
        total_belanja += harga_total_item
        print(f"-> {nama_barang} ({jumlah}x) - Rp{harga_total_item:,}") # Format angka
    else:
        print(f"Maaf, {nama_barang} tidak ada di daftar kami.")

# 4. Cetak Struk
print("\n" + "="*30)
print("        STRUK PEMBELIAN")
print("="*30)
print(f"{'Barang':<15}{'Qty':<5}{'Harga':>10}")
print("-" * 30)

for item in keranjang:
    # Format harga satuan agar rapi (misal: Rp5.000)
    harga_satuan_fmt = f"Rp{item['harga_satuan']:,}"
    print(f"{item['nama']:<15}{item['jumlah']:<5}{harga_satuan_fmt:>10}")

print("-" * 30)
print(f"{'Total':<20}{'Rp{total_belanja:,}':>10}")
print("="*30)

# 5. Pembayaran & Kembalian
uang_pembeli = int(input("Uang Pembeli: Rp"))
kembalian = uang_pembeli - total_belanja

print(f"Dibayar    : Rp{uang_pembeli:,}")
print(f"Kembalian  : Rp{kembalian:,}")
print("="*30)
print("Terima Kasih!")
print("="*30)
