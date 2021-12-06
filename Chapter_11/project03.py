from datetime import *
from project01 import diffDate

file = open('file/data_perpus.dat', 'r')

now_date = datetime.date(datetime.now())

penalty_fee = 2000

member_code = input('Masukkan Kode Member\t: ')

while True:
    read_file = file.readline()
    split_data = read_file.split('|')

    if member_code == split_data[0]:
        diff = diffDate(split_data[4].replace('\n', ''))
        if diff < 0:
            diff = 0

        print('\nData Peminjaman Buku')
        print('\nKode Member\t\t:', split_data[0],
              '\nNama Member\t\t:', split_data[1],
              '\nJudul Buku\t\t:', split_data[2],
              '\nTanggal Mulai Pinjam\t:', split_data[3],
              '\nTanggal Maks Pinjam\t:', split_data[4].replace('\n', ''),
              '\nTanggal Pengembalian\t:', now_date,
              '\nTerlambat\t\t:', str(diff) + ' hari',
              '\nDenda\t\t\t: Rp.', penalty_fee * diff)
        break

    if not read_file:
        file.close()
        print('\nDATA TIDAK DITEMUKAN!!')
        break
