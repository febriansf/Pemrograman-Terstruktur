def inputFile():
    while True:
        global namaFile
        try:
            namaFile = input('Masukkan nama file: ')
            file = open(namaFile)
            break
        except FileNotFoundError:
            print('Error...File Tidak ditemukan')


def read():
    file = open(namaFile, 'r')
    print('\nIsi file', namaFile)
    print('')
    print(file.read())


def write():
    file = open(namaFile, 'a')
    data = input('Data yang mau ditambahkan: ')
    file.write(data)

    if len(data) > 0:
        file.write('\n')

    file.close()


inputFile()
while True:
    read()
    write()
    read()

    lanjut = input('Mau Lanjut? (y/n): ')
    if lanjut == 'n' or lanjut == 'N':
        print('Exit...')
        break
