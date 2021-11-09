def tampilkan_data(data):
    for key, value in data.items():
        print('-' + key, ': ', value)


buah = {'apel': 5000,
        'jeruk': 8500,
        'mangga': 7800,
        'duku': 6500}

tampilkan_data(buah)
try:
    print('=========================')
    nama = input('Masukkan nama buah: ')
    harga = buah[nama]
    jumlah = int(input('Berapa KG         : '))
    total_harga = jumlah * harga
    print('=========================')
    print('Total harga       :', total_harga)

except KeyError:
    print('DATA TIDAK DITEMUKAN!!')
