struktur = {
    "Skripsi_Aqil": {
        "Bab_1": {
            "pendahuluan.docx": 45,
            "latar_belakang.docx": 62
        },
        "Bab_2": {
            "landasan_teori.docx": 118,
            "referensi": {
                "paper_A.pdf": 340,
                "paper_B.pdf": 210
            }
        },
        "Bab_3": {
            "metodologi.docx": 89,
            "diagram": {
                "flowchart.png": 512,
                "erd.png": 278,
                "arsitektur": {
                    "sistem.png": 430
                }
            }
        },
        "sidang": {
            "presentasi.pptx": 2048,
            "catatan_revisi.txt": 15
        },
        "README.txt": 8
    }
}

def total_ukuran(folder: dict) -> int:
    total = 0
    for nama, isi in folder.items():
        if isinstance(isi, dict):
            total += total_ukuran(isi)
        else:
            total += isi
    return total

print("Total ukuran skripsi:", total_ukuran(struktur["Skripsi_Aqil"]), "KB")

def hitung_file(folder: dict) -> int:
    jumlah = 0
    for nama, isi in folder.items():
        if isinstance(isi, dict):
            jumlah += hitung_file(isi)
        else:
            jumlah += 1
    return jumlah

print("Jumlah file:", hitung_file(struktur["Skripsi_Aqil"]), "file")

def cari_terbesar(folder: dict) -> tuple:
    terbesar = ("", 0)
    for nama, isi in folder.items():
        if isinstance(isi, dict):
            kandidat = cari_terbesar(isi)
            if kandidat[1] > terbesar[1]:
                terbesar = kandidat
        else:
            if isi > terbesar[1]:
                terbesar = (nama, isi)
    return terbesar

nama_file, ukuran = cari_terbesar(struktur["Skripsi_Aqil"])
print(f"File terbesar: {nama_file} ({ukuran} KB)")

def tampilkan_tree(folder: dict, nama: str = "root", level: int = 0):
    indent = "  " * level
    print(f"{indent}[folder] {nama}")
    for item, isi in folder.items():
        if isinstance(isi, dict):
            tampilkan_tree(isi, item, level + 1)
        else:
            print(f"{indent}  [file] {item} ({isi} KB)")

tampilkan_tree(struktur["Skripsi_Aqil"], "Skripsi_Aqil")