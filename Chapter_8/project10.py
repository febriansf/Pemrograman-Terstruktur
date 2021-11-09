def tampilkan_data(data):
    print('======================')
    print('Daftar Buah: ')
    for key, value in data.items():
        print('-', key, ': ', value)


buah = {'apel': 5000,
        'jeruk': 8500,
        'mangga': 7800,
        'duku': 6500}

tampilkan_data(buah)
total_semua = 0
while True:
    try:
        print('======================')
        nama = input('Masukkan nama buah: ')
        harga = buah[nama]
        jumlah = int(input('Berapa KG     : '))
        total_harga = harga * jumlah
        total_semua += total_harga
        tambah = input('\nBeli buah yang lain (y/n)? ')
        if tambah == 'n' or tambah == 'N':
            print('======================')
            print('Total harga  :', total_semua)
            break
    except KeyError:
        print('DATA TIDAK DITEMUKAN!!\n')
