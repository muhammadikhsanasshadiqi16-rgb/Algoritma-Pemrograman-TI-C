list_buku = [
    ["algoritma", 2000],
    ["struktur data", 2500],
    ["basis data", 1800],
    ["statistika", 1900],
    ["pemograman", 1600]
]

print("=== LIST BUKU DAN DENDA ===")
for i in range(len(list_buku)):
    print(f"{i+1}. {list_buku[i][0]} - Rp {list_buku[i][1]}")

pilihan = int(input("Pilih list buku: "))

if 1 <= pilihan <= len(list_buku):
    item = list_buku[pilihan-1]
    print(f"Kamu pilih: {item[0]} denda keterlambatannya Rp {item[1]}")
else:
    print("error")