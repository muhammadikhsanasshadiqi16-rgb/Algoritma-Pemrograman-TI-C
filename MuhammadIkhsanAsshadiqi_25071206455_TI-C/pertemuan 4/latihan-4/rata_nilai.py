try:
    jumlah = int(input("Masukkan jumlah mata kuliah: "))
    total = float(input("Masukkan total nilai: "))

    rata_rata = total / jumlah

    print("Rata-rata nilai:", rata_rata)

except ValueError:
    print("Input harus berupa angka!")

except ZeroDivisionError:
    print("Jumlah mata kuliah tidak boleh nol!")

except:
    print("Terjadi kesalahan pada program!")