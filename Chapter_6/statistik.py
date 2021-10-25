#Fungsi untuk menghitung total bilangan jika dijumlahkan
def sum(*angka):
    hasil = 0
    for data in angka:
        hasil += data

    return hasil

#Fungsi untuk menghitung banyaknya angka
def average(*angka):
    hasil = sum(*angka)
    jumlah = 0
    for data in angka:
        jumlah += 1

    return hasil / jumlah

#Fungsi untuk menghitung nilai maksimal dari kumpulan angka
def maks(*angka):
    maks = angka[0]
    for data in angka:
        if maks < data:
            maks = data

    return maks

#Fungsi untuk menghitung nilai minimal dari kumpulan angka
def min(*angka):
    min = angka[0]
    for data in angka:
        if min > data:
            min = data

    return min
