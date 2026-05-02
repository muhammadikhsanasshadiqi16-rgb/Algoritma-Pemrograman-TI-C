class Node:
    def __init__(self, id_buku, judul):
        self.id_buku = id_buku
        self.judul = judul
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, id_buku, judul):
        node_baru = Node(id_buku, judul)
        if self.root is None:
            self.root = node_baru
        else:
            current = self.root
            while True:
                if id_buku < current.id_buku:
                    if current.left is None:
                        current.left = node_baru
                        break
                    else:
                        current = current.left
                else:
                    if current.right is None:
                        current.right = node_baru
                        break
                    else:
                        current = current.right
        print(f"[INSERT] Berhasil memasukkan: ID {id_buku} - {judul}")

    def search(self, id_buku):
        current = self.root
        while current is not None:
            if id_buku == current.id_buku:
                return current
            elif id_buku < current.id_buku:
                current = current.left
            else:
                current = current.right
        return None

    def _inorder_helper(self, node, result_container):
        if node is not None:
            self._inorder_helper(node.left, result_container)
            result_container.append((node.id_buku, node.judul))
            self._inorder_helper(node.right, result_container)

    def traversal_inorder(self):
        result_container = []
        self._inorder_helper(self.root, result_container)
        return result_container

    def get_min(self):
        if self.root is None:
            return None
        current = self.root
        while current.left is not None:
            current = current.left
        return current

    def get_max(self):
        if self.root is None:
            return None
        current = self.root
        while current.right is not None:
            current = current.right
        return current

    def _height_helper(self, node):
        if node is None:
            return -1
        left_height = self._height_helper(node.left)
        right_height = self._height_helper(node.right)
        if left_height > right_height:
            return left_height + 1
        else:
            return right_height + 1

    def height(self):
        return self._height_helper(self.root)


katalog = BST()

print('SISTEM KATALOG PERPUSTAKAAN "ILMU TERANG"')
print("=========================================")

katalog.insert(50, "Dasar Pemrograman")
katalog.insert(30, "Struktur Data")
katalog.insert(70, "Kecerdasan Buatan")
katalog.insert(20, "Matematika Diskrit")
katalog.insert(40, "Basis Data")
katalog.insert(60, "Jaringan Komputer")
katalog.insert(80, "Sistem Operasi")

print()

print("[INFO] Koleksi Buku (In-Order Traversal):")
buku_terurut = katalog.traversal_inorder()
for i, (id_buku, judul) in enumerate(buku_terurut, start=1):
    print(f"  {i}. {id_buku} - {judul}")

print()

hasil_60 = katalog.search(60)
if hasil_60:
    print(f"[SEARCH] Mencari ID 60... Ditemukan! Judul: {hasil_60.judul}")
else:
    print("[SEARCH] Mencari ID 60... Data tidak ditemukan.")

hasil_100 = katalog.search(100)
if hasil_100:
    print(f"[SEARCH] Mencari ID 100... Ditemukan! Judul: {hasil_100.judul}")
else:
    print("[SEARCH] Mencari ID 100... Data tidak ditemukan.")

print()

buku_min = katalog.get_min()
buku_max = katalog.get_max()
print(f"[STATISTIK] ID Terkecil: {buku_min.id_buku}")
print(f"[STATISTIK] ID Terbesar: {buku_max.id_buku}")

print()

print(f"[INFO] Tinggi (Height) Tree: {katalog.height()}")
print("=========================================")
print("Simulasi Selesai!")