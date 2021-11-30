file = open('file/data.mhs', 'a+')

while True:
    nim = input('Masukkan NIM\t: ')
    nama = input('Masukkan Nama\t: ')
    alamat = input('Masukkan Alamat\t: ')

    file.write(nim + '|' + nama + '|' + alamat + '\n')

    again = input('\nUlangi input lagi? (y/n)\t: ')
    print('')
    if (again in {'n', 'N'}):
        print('Exit...')
        file.close()
        break
