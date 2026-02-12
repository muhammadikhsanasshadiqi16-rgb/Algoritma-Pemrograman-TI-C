def jumlah_digit(n):
    if n == 0:
        return 0
    else:
        return (n % 10) + jumlah_digit(n // 10)

angka = 1234
print("Jumlah digit", angka, "=", jumlah_digit(angka))
