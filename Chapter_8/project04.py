line = '================================'


def tambah_data(data):
    print(line)
    print('Tambah data')
    nama = input('Masukkan nama sayur: ')
    data.add(nama)


def hapus_data(data):
    print(line)
    print('Hapus data')
    while True:
        try:
            nama = input('Masukkan NAMA sayur: ')
            data.remove(nama)
            break
        except:
            print(line)
            print('DATA TIDAK DTEMUKAN!!')
            break


def tampil_data(data):
    print(line)
    print('Daftar Sayur: ')
    i = 1
    for nama in data:
        print(str(i)+'.', nama)
        i += 1


data_sayur = {'bayam', 'kangkung', 'wortel', 'selada'}

while True:
    print(line)
    print('A. Tambah data sayur')
    print('B. Hapus data sayur')
    print('C. Tampilkan data sayur')
    print('E. Keluar')
    print(line)
    pilihan = input('Masukan pilihan: ')

    if pilihan == 'a' or pilihan == 'A':
        tambah_data(data_sayur)
    elif pilihan == 'b' or pilihan == 'B':
        hapus_data(data_sayur)
    elif pilihan == 'c' or pilihan == 'C':
        tampil_data(data_sayur)
    elif pilihan == 'e' or pilihan == 'E':
        break
    else:
        print('Input tidak valid')
