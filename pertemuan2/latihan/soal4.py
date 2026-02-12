def pangkat_rekursif(a, b):
    if b == 0:
        return 1
    else:
        return a * pangkat_rekursif(a, b - 1)
    
a = 2
b = 5
print(f"{a}^{b} =", pangkat_rekursif(a, b))
