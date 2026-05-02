DAFTAR_PILIHAN = ["batu", "gunting", "kertas", "batu", "gunting",
                  "kertas", "batu", "gunting", "kertas", "batu"]

# === BAGIAN A  
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

        if pilihan == pilihan_komputer:
            print("Seri!")
            continue
        elif (pilihan == "batu" and pilihan_komputer == "gunting") or \
             (pilihan == "gunting" and pilihan_komputer == "kertas") or \
             (pilihan == "kertas" and pilihan_komputer == "batu"):
            print("Kamu menang ronde ini!")
            return True, sisa
        else:
            print("Komputer menang ronde ini!")

    print("Giliran habis! Kamu tidak berhasil menang.")
    return False, 0


def hitung_skor(berhasil, sisa_giliran):
    """Mengembalikan skor berdasarkan hasil dan sisa giliran."""
    if berhasil:
        return sisa_giliran * 10
    return 0


def main_satu_ronde(nama, nomor_ronde):
    """Menjalankan satu ronde permainan dan mengembalikan list [nama, skor]."""
    pilihan_komputer = DAFTAR_PILIHAN[nomor_ronde % len(DAFTAR_PILIHAN)]
    print(f"\n=== Ronde {nomor_ronde + 1} ===")
    print("Kamu punya 3 giliran untuk mengalahkan komputer minimal sekali.")
    berhasil, sisa = main_giliran(pilihan_komputer, 5)
    skor = hitung_skor(berhasil, sisa)
    print(f"Skor kamu: {skor}")
    return [nama, skor]


# === BAGIAN B ===

def tampilkan_riwayat(riwayat):
    """Menampilkan seluruh riwayat permainan dalam format tabel."""
    if not riwayat:
        print("Belum ada riwayat.")
        return
    print("\n=== RIWAYAT PERMAINAN LU ===")
    print(f"{'No':<5} {'Nama':<20} {'Skor':<10}")
    print("-" * 35)
    for i, data in enumerate(riwayat):
        print(f"{i + 1:<5} {data[0]:<20} {data[1]:<10}")

# === BAGIAN c ===
def main():
    print (" mulai game nya ")