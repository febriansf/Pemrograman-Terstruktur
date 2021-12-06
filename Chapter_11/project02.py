from datetime import *

now_date = datetime.date(datetime.now())
max_return = now_date + timedelta(days=7)

save_file = open('file/data_perpus.dat', 'a+')

while True:
    member_code = input('Masukkan Kode Member\t: ')
    member_name = input('Masukkan Nama Member\t: ')
    book_title = input('Masukkan Judul Buku\t: ')

    save_file.write(member_code + '|' + member_name + '|'
                    + book_title + '|' + str(now_date) + '|'
                    + str(max_return) + '\n')

    loop = input('\nUlangi lagi (y/n) : ')
    print('')
    if loop in ('n', 'N'):
        save_file.close()
        break
