def bilangan_prima(n):
    prima_list = []

    for i in range(2, n + 1):
        prima = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                prima = False
                break
        if prima:
            prima_list.append(i)

    return prima_list

hasil_prima = bilangan_prima(50)
print("Bilangan prima sampai 50:", hasil_prima)