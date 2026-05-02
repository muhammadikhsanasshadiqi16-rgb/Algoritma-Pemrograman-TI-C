# Nama File: 25071206455_NamaLengkap.py
# Deskripsi: UTS Praktikum Algoritma Pemrograman - Higher or Lower?

# === BAGIAN A ===
# [Variabel Global]
DAFTAR_ANGKA = [23, 67, 4, 89, 15, 42, 73, 31, 58, 9] # 

# --- A.1: tebak_angka ---
def tebak_angka(angka_rahasia, maks_percobaan):
    """
    Menjalankan loop tebakan pemain dan memberikan petunjuk arah angka. [cite: 26, 27]
    """
    percobaan = 0
    while percobaan < maks_percobaan:
        try:
            tebak = int(input(f"Masukkan tebakan (1-100): "))
            percobaan += 1
            
            if tebak < angka_rahasia:
                print("Terlalu kecil") # [cite: 12]
            elif tebak > angka_rahasia:
                print("Terlalu besar") # [cite: 13]
            else:
                print("Benar!") # [cite: 14]
                return True, (maks_percobaan - percobaan) # Mengembalikan status dan sisa percobaan [cite: 28]
        except ValueError:
            print("Masukkan angka yang valid!")
            
    return False, 0 # [cite: 28]

# --- A.2: hitung_skor ---
def hitung_skor(berhasil, sisa_percobaan):
    """
    Menghitung skor berdasarkan sisa percobaan dikali 10. [cite: 29, 30]
    """
    if berhasil:
        return sisa_percobaan * 10 # [cite: 17, 30]
    return 0 # [cite: 17, 30]

# --- A.3: main_satu_ronde ---
def main_satu_ronde(nama, nomor_ronde):
    """
    Mengambil angka rahasia dari daftar dan mengeksekusi satu ronde game. [cite: 31, 32]
    """
    # Menggunakan modulo jika ronde melebihi jumlah data di list [cite: 21, 22]
    indeks = nomor_ronde % len(DAFTAR_ANGKA)
    angka_rahasia = DAFTAR_ANGKA[indeks]
    
    # Jalankan inti game
    berhasil, sisa = tebak_angka(angka_rahasia, 7) # Maksimal 7 percobaan [cite: 17]
    skor = hitung_skor(berhasil, sisa)
    
    return [nama, skor] # [cite: 33]


# === BAGIAN B ===
# --- B.1: tampilkan_riwayat ---
def tampilkan_riwayat(riwayat):
    """
    Mencetak riwayat permainan dalam format tabel matrix 2D. [cite: 35, 36]
    """
    if not riwayat:
        print("\nBelum ada riwayat.") # [cite: 37]
        return

    print("\n" + "="*30)
    print(f"{'No':<4} | {'Nama':<15} | {'Skor':<5}")
    print("-" * 30)
    for i in range(len(riwayat)):
        print(f"{i+1:<4} | {riwayat[i][0]:<15} | {riwayat[i][1]:<5}")


# === BAGIAN C ===
# --- C.1: selection_sort_riwayat ---
def selection_sort_riwayat(riwayat):
    """
    Mengurutkan riwayat dari skor tertinggi ke terendah (Selection Sort). [cite: 39, 40]
    """
    # Salin list agar data asli tidak berubah [cite: 41]
    data_urut = []
    for item in riwayat:
        data_urut.append(item[:])

    n = len(data_urut)
    for i in range(n):
        maks_idx = i
        for j in range(i + 1, n):
            # Cek skor di indeks 1 untuk mengurutkan besar ke kecil [cite: 40]
            if data_urut[j][1] > data_urut[maks_idx][1]:
                maks_idx = j
        # Tukar posisi
        data_urut[i], data_urut[maks_idx] = data_urut[maks_idx], data_urut[i]
    
    return data_urut

# --- C.2: tampilkan_leaderboard ---
def tampilkan_leaderboard(riwayat):
    """
    Menampilkan peringkat akhir berdasarkan skor tertinggi. [cite: 42, 43]
    """
    if not riwayat:
        return

    sorted_data = selection_sort_riwayat(riwayat)
    print("\n" + "=== LEADERBOARD ===")
    print(f"{'Rank':<5} | {'Nama':<15} | {'Skor':<5}")
    print("-" * 30)
    
    for i in range(len(sorted_data)):
        # Berikan tanda bintang (*) untuk peringkat pertama [cite: 44]
        rank_display = f"{i+1}*" if i == 0 else f"{i+1}"
        print(f"{rank_display:<5} | {sorted_data[i][0]:<15} | {sorted_data[i][1]:<5}")


# === PROGRAM UTAMA ===
def main():
    riwayat_game = [] # Matrix 2D untuk menyimpan [nama, skor] [cite: 15]
    ronde_ke = 0
    
    print("=== UTS PRAKTIKUM ALPRO: HIGHER OR LOWER? ===")
    nama_user = input("Masukkan nama pemain: ") # [cite: 47]
    
    while True: # [cite: 50]
        hasil_ronde = main_satu_ronde(nama_user, ronde_ke) # [cite: 48]
        riwayat_game.append(hasil_ronde)
        ronde_ke += 1
        
        lagi = input("Ingin main lagi? (ya/tidak): ").lower() # [cite: 49]
        if lagi != 'ya':
            break
            
    # Tampilkan hasil akhir [cite: 51]
    tampilkan_riwayat(riwayat_game)
    tampilkan_leaderboard(riwayat_game)
    print("\nProgram selesai. Terima kasih!")

if __name__ == "__main__":
    main()