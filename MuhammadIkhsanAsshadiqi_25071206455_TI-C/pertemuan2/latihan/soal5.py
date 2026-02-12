import math

def jarak(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

x1, y1 = 1, 2
x2, y2 = 4, 6

hasil_jarak = jarak(x1, y1, x2, y2)
print("Jarak =", hasil_jarak)