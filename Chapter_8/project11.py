def tampilkan_data(data):
    print('======================')
    print('Daftar Buah: ')
    for key, value in data.items():
        print('-', key, ': ', value)


def beli_buah():
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


def tambah_data(data):
    print('======================')
    nama = input('Masukkan nama buah yang akan ditambahkan: ')
    if nama not in data:
        harga = int(input('Masukkan harga buah: '))
        data[nama.lower()] = harga
        print('OK')
    else:
        print('DATA SUDAH ADA!!')


def tampilkan_menu():
    print('======================')
    print('A. Tambah data buah\n' + 'B. Beli buah')
    print('======================')
    return input('Masukkan pilihan: ')


buah = {'apel': 5000,
        'jeruk': 8500,
        'mangga': 7800,
        'duku': 6500}

while True:
    pilihan = tampilkan_menu()
    if pilihan == 'a' or pilihan == 'A':
        tambah_data(buah)
        tampilkan_data(buah)
    elif pilihan == 'b' or pilihan == 'B':
        tampilkan_data(buah)
        beli_buah()
    else:
        print('INPUT TIDAK VALID')
