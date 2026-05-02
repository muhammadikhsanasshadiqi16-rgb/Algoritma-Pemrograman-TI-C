# ================================================================
# SOAL LATIHAN UTS — PRAKTIKUM ALGORITMA PEMROGRAMAN
# Game: Batu Gunting Kertas
# ================================================================

DAFTAR_PILIHAN = ["batu", "gunting", "kertas", "batu", "gunting",
                  "kertas", "batu", "gunting", "kertas", "batu"]

# === BAGIAN A ===

def main_giliran(pilihan_komputer, maks_giliran):
    """Meminta input pilihan pemain, membandingkan dengan pilihan komputer, mengembalikan hasil dan sisa giliran."""
    sisa = maks_giliran
    while sisa > 0:
        pilihan = input("Pilih (batu/gunting/kertas): ").strip().lower()
        if pilihan not in ["batu", "gunting", "kertas"]:
            print("Pilihan tidak valid. Masukkan batu, gunting, atau kertas.")
            continue
        sisa -= 1
        print(f"Komputer memilih: {pilihan_komputer}")