# ================================================================
# UJIAN TENGAH SEMESTER - PRAKTIKUM ALGORITMA PEMROGRAMAN
# Game: Higher or Lower?
# ================================================================

DAFTAR_ANGKA = [23, 67, 4, 89, 15, 42, 73, 31, 58, 9]

# === BAGIAN A ===

def tebak_angka(angka_rahasia, maks_percobaan):
    """Meminta input tebakan dari pemain dan memberi petunjuk hingga benar atau percobaan habis."""
    sisa = maks_percobaan
    while sisa > 0:
        try:
            tebakan = int(input(f"Tebak angka (sisa percobaan: {sisa}): "))
        except ValueError:
            print("Input tidak valid. Masukkan angka bulat.")
            continue
        sisa -= 1
        if tebakan < angka_rahasia:
            print("Terlalu kecil")
        elif tebakan > angka_rahasia:
            print("Terlalu besar")
        else:
            print("Benar!")
            return True, sisa
    print(f"Percobaan habis! Angka rahasia adalah {angka_rahasia}.")
    return False, 0


def hitung_skor(berhasil, sisa_percobaan):
    """Mengembalikan skor berdasarkan hasil tebakan dan sisa percobaan."""
    if berhasil:
        return sisa_percobaan * 10
    return 0


def main_satu_ronde(nama, nomor_ronde):
    """Menjalankan satu ronde permainan dan mengembalikan list [nama, skor]."""
    angka_rahasia = DAFTAR_ANGKA[nomor_ronde % len(DAFTAR_ANGKA)]
    print(f"\n=== Ronde {nomor_ronde + 1} ===")
    print("Tebak angka antara 1 - 100. Kamu punya 7 percobaan.")
    berhasil, sisa_percobaan = tebak_angka(angka_rahasia, 7)
    skor = hitung_skor(berhasil, sisa_percobaan)
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

def selection_sort_riwayat(riwayat):
    """Mengurutkan salinan riwayat dari skor tertinggi ke terendah menggunakan Selection Sort."""
    salinan = [baris[:] for baris in riwayat]
    n = len(salinan)
    for i in range(n):
        idx_maks = i
        for j in range(i + 1, n):
            if salinan[j][1] > salinan[idx_maks][1]:
                idx_maks = j
        salinan[i], salinan[idx_maks] = salinan[idx_maks], salinan[i]
    return salinan


def tampilkan_leaderboard(riwayat):
    """Menampilkan leaderboard berdasarkan skor tertinggi dengan tanda bintang untuk peringkat pertama."""
    terurut = selection_sort_riwayat(riwayat)
    print("\n=== LEADERBOARD ===")
    print(f"{'Rank':<6} {'Nama':<20} {'Skor':<10}")
    print("-" * 36)
    for i, data in enumerate(terurut):
        peringkat = i + 1
        tanda = "* " if peringkat == 1 else "  "
        print(f"{tanda}{peringkat:<4} {data[0]:<20} {data[1]:<10}")


# === PROGRAM UTAMA ===

def main():
    """Fungsi utama untuk menjalankan program game Higher or Lower."""
    print("========================================")
    print("       Selamat Datang di Higher or Lower!")
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