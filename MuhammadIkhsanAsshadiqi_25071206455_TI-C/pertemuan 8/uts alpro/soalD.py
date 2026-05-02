# ================================================================
# SOAL LATIHAN UTS — PRAKTIKUM ALGORITMA PEMROGRAMAN
# Game: Tebak Langkah Catur
# ================================================================

DAFTAR_SOAL = [
    ["Raja",    "Bergerak 1 langkah ke segala arah",               "raja"],
    ["Ratu",    "Bergerak bebas lurus dan diagonal",               "ratu"],
    ["Benteng", "Bergerak bebas secara lurus saja",                "benteng"],
    ["Gajah",   "Bergerak bebas secara diagonal saja",             "gajah"],
    ["Kuda",    "Bergerak membentuk huruf L",                      "kuda"],
    ["Pion",    "Maju 1 langkah, makan diagonal",                  "pion"],
    ["Raja",    "Tidak boleh masuk petak yang diserang musuh",     "raja"],
    ["Ratu",    "Buah paling kuat di papan catur",                 "ratu"],
    ["Benteng", "Digunakan dalam gerakan rokade bersama Raja",     "benteng"],
    ["Kuda",    "Satu-satunya buah yang bisa melompati buah lain", "kuda"],
]

# === BAGIAN A ===

def tebak_buah(jawaban_benar, deskripsi, maks_percobaan):
    """Menampilkan deskripsi gerakan dan meminta pemain menebak nama buah catur."""
    sisa = maks_percobaan
    print(f"Petunjuk: {deskripsi}")

    while sisa > 0:
        tebakan = input(f"Tebak nama buah catur (sisa percobaan: {sisa}): ").strip().lower()
        sisa -= 1

        if tebakan == jawaban_benar:
            print("Benar!")
            return True, sisa
        else:
            print(f"Salah! Bukan '{tebakan}'.")

    print(f"Percobaan habis! Jawaban yang benar adalah '{jawaban_benar}'.")
    return False, 0


def hitung_skor(berhasil, sisa_percobaan):
    """Mengembalikan skor berdasarkan hasil tebakan dan sisa percobaan."""
    if berhasil:
        return sisa_percobaan * 20
    return 0


def main_satu_ronde(nama, nomor_ronde):
    """Menjalankan satu ronde tebak buah catur dan mengembalikan list [nama, skor]."""
    soal = DAFTAR_SOAL[nomor_ronde % len(DAFTAR_SOAL)]
    deskripsi = soal[1]
    jawaban_benar = soal[2]

    print(f"\n=== Ronde {nomor_ronde + 1} ===")
    berhasil, sisa = tebak_buah(jawaban_benar, deskripsi, 3)
    skor = hitung_skor(berhasil, sisa)
    print(f"Skor kamu: {skor}")
    return [nama, skor]


# === BAGIAN B ===

def tampilkan_riwayat(riwayat):
    """Menampilkan seluruh riwayat permainan dalam format tabel."""
    if not riwayat:
        print("Belum ada riwayat.")
        return
    print("\n=== RIWAYAT PERMAINAN ===")
    print(f"{'No':<5} {'Nama':<20} {'Skor':<10}")
    print("-" * 35)
    for i, data in enumerate(riwayat):
        print(f"{i + 1:<5} {data[0]:<20} {data[1]:<10}")


# === BAGIAN C ===

def bubble_sort_riwayat(riwayat):
    """Mengurutkan salinan riwayat dari skor tertinggi ke terendah menggunakan Bubble Sort."""
    salinan = [baris[:] for baris in riwayat]
    n = len(salinan)
    for i in range(n):
        for j in range(0, n - i - 1):
            if salinan[j][1] < salinan[j + 1][1]:
                salinan[j], salinan[j + 1] = salinan[j + 1], salinan[j]
    return salinan


def tampilkan_leaderboard(riwayat):
    """Menampilkan leaderboard berdasarkan skor tertinggi dengan tanda bintang untuk peringkat pertama."""
    terurut = bubble_sort_riwayat(riwayat)
    print("\n=== LEADERBOARD ===")
    print(f"{'Rank':<6} {'Nama':<20} {'Skor':<10}")
    print("-" * 36)
    for i, data in enumerate(terurut):
        peringkat = i + 1
        tanda = "* " if peringkat == 1 else "  "
        print(f"{tanda}{peringkat:<4} {data[0]:<20} {data[1]:<10}")


# === PROGRAM UTAMA ===

def main():
    """Fungsi utama untuk menjalankan program game Tebak Langkah Catur."""
    print("========================================")
    print("   Selamat Datang di Tebak Langkah Catur!")
    print("========================================")
    nama = input("Masukkan nama kamu: ")
    riwayat = []
    nomor_ronde = 0

    while True:
        hasil = main_satu_ronde(nama, nomor_ronde)
        riwayat.append(hasil)
        nomor_ronde += 1

        lagi = input("\nIngin bermain lagi? (ya/tidak): ").strip().lower()
        if lagi != "ya":
            break

    tampilkan_riwayat(riwayat)
    tampilkan_leaderboard(riwayat)
    print("\nTerima kasih sudah bermain!")


if __name__ == "__main__":
    main()