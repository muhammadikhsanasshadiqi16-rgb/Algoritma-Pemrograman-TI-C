list_buku = [["algoritma", 2000], 
             ["struktur data", 2500],
             ["basis data", 18000],
             ["statitiska", 1900],
             ["pemograman", 1600]]

judul_buku = []
lama_pinjaman = 0

while True:
    print("\n(Ketik 0 buat selesai)")
    pilih = int(input("Masukkan nomor buku: "))
    
    if pilih == 0:
        break
    
    if 1 <= pilih <= len(list_buku):
        lama = int(input(f"Berapa lama dipinjam buku {list_buku[pilih-1][0]}? "))
        judul_buku.append([list_buku[pilih-1][0], lama])
        lama_pinjaman += list_buku[pilih-1][1] * lama
    else:
        print("buku tidak ada!")

print("\n--- buku yang dipinjam ---")
for p in list_buku:
    print(f"- {p[0]} ({p[1]} lama)")
print(f"Total Bayar denda: Rp {lama_pinjaman}")
    
    