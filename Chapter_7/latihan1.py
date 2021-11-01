try:
    namaFile = input("Masukkan nama file: ")

    file = open(namaFile, "r")

    print('Isi dari file', namaFile, 'adalah:\n')
    print(file.read())

except FileNotFoundError:
    print('File tidak ditemukan!!')
