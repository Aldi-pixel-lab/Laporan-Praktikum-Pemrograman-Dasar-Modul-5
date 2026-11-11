def mutlak(angka):
    if angka < 0:
        return -angka
    return angka


def hitung(nilai1, nilai2):
    return mutlak(nilai1 - nilai2)


data = []
while len(data) < 4:
    data += input().split()

x1, y1, x2, y2 = map(int, data)

Hasil = hitung(x1, x2) + hitung(y1, y2)
print(mutlak(Hasil))