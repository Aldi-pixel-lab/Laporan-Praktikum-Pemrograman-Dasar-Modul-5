def MaxBilangan(a, b, c, d):
    maks = a

    if b > maks:
        maks = b
    if c > maks:
        maks = c
    if d > maks:
        maks = d

    return maks


data = []
while len(data) < 4:
    data += input().split()

a, b, c, d = map(int, data)

hasil = MaxBilangan(a, b, c, d)
print(hasil)