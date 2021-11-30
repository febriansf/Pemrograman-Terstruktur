file = open('file/data.mhs', 'r')

search = input('Masukkan NIM yang mau dicari: ')
while True:
    read_file = file.readline()
    split_data = read_file.split('|')

    if search == split_data[0]:
        print('\nData Mahasiswa')
        print('NIM\t:', split_data[0],
              '\nNama\t:', split_data[1],
              '\nAlamat\t:', split_data[2].replace('\n', ''))
        break

    if not read_file:
        print('\nDATA TIDAK DITEMUKAN!!')
        file.close()
        break
