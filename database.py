# 1. Daftar Harga Mobil
print("--- SELAMAT DATANG DI RENTAL MOBIL ---")
print("A. Avanza (Rp300.000/hari)")
print("B. Innova (Rp500.000/hari)")

# 2. Input dari Pengguna
pilihan = input("Pilih mobil (A/B): ")
hari = int(input("Mau sewa berapa hari? "))

# 3. Menentukan Harga per Hari
if pilihan.upper() == "A":
    harga_per_hari = 300000
    nama_mobil = "Avanza"
else:
    harga_per_hari = 500000
    nama_mobil = "Innova"

# 4. Hitung Total Tagihan
total_harga = harga_per_hari * hari
print(f"Total yang harus dibayar: Rp {total_harga}")

# 5. Proses Bayar dan Kembalian
uang_bayar = int(input("Masukkan uang Anda: Rp "))
kembalian = uang_bayar - total_harga

if uang_bayar >= total_harga:
    print(f"Kembalian Anda: Rp {kembalian}")
    print("Terima kasih sudah menyewa!")
else:
    print("Maaf, uang Anda tidak cukup.")