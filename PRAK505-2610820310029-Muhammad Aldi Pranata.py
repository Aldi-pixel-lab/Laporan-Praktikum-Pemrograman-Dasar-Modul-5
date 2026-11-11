def Biodata(tahun, nama, asal):
    tahun_sekarang = 2026   
    umur = tahun_sekarang - tahun

    print(f"Perkenalkan Nama Saya : {nama}")
    print(f"Umur Saya : {umur}")
    print(f"Saya Adalah Angkatan : {tahun_sekarang}")
    print(f"Asal Saya dari : {asal}")


tahunLahir = int(input())
Namaku = input()
Asal = input()

Biodata(tahunLahir, Namaku, Asal)