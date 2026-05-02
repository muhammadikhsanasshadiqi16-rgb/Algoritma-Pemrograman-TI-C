n_hari = int(input("Input jumlah hari: "))
n_menu = int(input("Input jumlah menu: "))

matriks_penjualan = []

# Isi data matriks
for i in range(n_hari):
    baris = []
    print(f"Data Hari ke-{i+1}:")
    for j in range(n_menu):
        porsi = int(input(f"  Jumlah menu {j+1} terjual: "))
        baris.append(porsi)
    matriks_penjualan.append(baris)

# Print matriks
print("\nMatriks Penjualan:")
for b in matriks_penjualan:
    print(b)

# Hitung total per hari (baris)
for i in range(n_hari):
    print(f"Total terjual hari ke-{i+1}: {sum(matriks_penjualan[i])}")