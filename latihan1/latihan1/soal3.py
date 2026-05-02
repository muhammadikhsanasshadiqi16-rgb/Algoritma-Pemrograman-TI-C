# Misal kita ambil total belanja dari proses sebelumnya
total_belanja = int(input("Masukkan total belanja pelanggan: "))

while True:
    bayar = int(input(f"Uang yang dibayarkan (Total Rp {total_belanja}): "))
    
    if bayar < total_belanja:
        print("Duitnya kurang, silakan input ulang.")
    else:
        break

kembalian = bayar - total_belanja

if kembalian == 0:
    print("Uang pas, nggak ada kembalian.")
else:
    print(f"Kembalian Anda: Rp {kembalian}")