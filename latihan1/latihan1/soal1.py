# List menu: [Nama, Harga]
menu_barokah = [
    ["Nasi Goreng", 15000],
    ["Es Teh", 5000],
    ["Ayam Penyet", 18000],
    ["Mie Rebus", 12000],
    ["Es Jeruk", 7000]
]

print("=== MENU WARUNG BAROKAH ===")
# Nampilin menu pakai loop
for i in range(len(menu_barokah)):
    print(f"{i+1}. {menu_barokah[i][0]} - Rp {menu_barokah[i][1]}")

# Input pilihan
pilihan = int(input("Pilih nomor menu: "))

# Cek valid atau nggak
if 1 <= pilihan <= len(menu_barokah):
    item = menu_barokah[pilihan-1]
    print(f"Kamu pilih: {item[0]} harganya Rp {item[1]}")
else:
    print("Nomor menu nggak ada, bro!")