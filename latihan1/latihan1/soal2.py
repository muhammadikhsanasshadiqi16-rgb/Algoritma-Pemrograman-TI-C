# Copy list menu dari soal 1
menu_barokah = [["Nasi Goreng", 15000], ["Es Teh", 5000], ["Ayam Penyet", 18000], ["Mie Rebus", 12000], ["Es Jeruk", 7000]]

list_pesanan = []
total_harga = 0

# Loop biar bisa nambah pesanan terus
while True:
    print("\n(Ketik 0 buat selesai)")
    pilih = int(input("Masukkan nomor menu: "))
    
    if pilih == 0:
        break
    
    if 1 <= pilih <= len(menu_barokah):
        porsi = int(input(f"Berapa porsi {menu_barokah[pilih-1][0]}? "))
        # Simpan nama dan jumlah porsi
        list_pesanan.append([menu_barokah[pilih-1][0], porsi])
        # Tambah ke total
        total_harga += menu_barokah[pilih-1][1] * porsi
    else:
        print("Menu nggak ketemu!")

# Tampilkan ringkasan
print("\n--- Pesanan Kamu ---")
for p in list_pesanan:
    print(f"- {p[0]} ({p[1]} porsi)")
print(f"Total Bayar: Rp {total_harga}")