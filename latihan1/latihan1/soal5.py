class Menu:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga
    
    def tampilkan(self):
        print(f"{self.nama} - Rp {self.harga}")

class Transaksi:
    def __init__(self):
        self.total = 0
    
    def tambah(self, menu_obj, jumlah):
        self.total += menu_obj.harga * jumlah
    
    def struk(self):
        print(f"Total Belanja: Rp {self.total}")

# Inisialisasi objek
m1 = Menu("Ayam Bakar", 20000)
m2 = Menu("Es Teh", 5000)
m3 = Menu("Nasi Putih", 5000)

daftar = [m1, m2, m3]
for i, m in enumerate(daftar):
    print(f"{i+1}. ", end="")
    m.tampilkan()

# Coba transaksi
t = Transaksi()
pil = int(input("Pilih menu (1-3): "))
jml = int(input("Jumlah: "))

t.tambah(daftar[pil-1], jml)
t.struk()