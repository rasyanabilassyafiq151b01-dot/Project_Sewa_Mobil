from Pembeli import sewa_mobil

def pembayaran():
    print("""

===========================
  PILIH METODE PEMBAYARAN
===========================

 DEBIT      |         TUNAI

""")

    bayar = input("PILIH METODE DIATAS:").lower()

    if bayar == "debit":

        while True:
            no_debit = input("Masukkan nomor debit 16 digit: ")

            if len(no_debit) == 16:
                print("Nomor debit diterima")
                break
            else:
                print("Nomor debit tidak valid")
                print("Harus 16 karakter")
                print("Silakan ulangi")

    elif bayar == "tunai":    
        tunai = int(input("Masukan Nominal Pembayaran Sesuai dengan Struk Diatas"))
        total = sewa_mobil
        uang = tunai
        
        if uang < total:
                print("Uang kurang")
                print("Total:", total)
        else:
                kembalian = uang - total
                print("Pembayaran berhasil")
                print("Kembalian:", kembalian)

    else:
        print("Metode tidak tersedia")