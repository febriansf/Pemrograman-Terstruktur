sum = 0
jumlah = 0

print('Program untuk menghitung rata -rata data\n'
      + 'Ketik \'n\'/\'N\' untuk keluar dari program',
      'dan menampilkan hasilnya :)\n')

while True:
    try:
        data = input('Masukkan bilangan bulat: ')

        if data == 'n' or data == 'N':
            print('Rata-ratanya adalah: ', rerata)
            break

        sum += int(data)
        jumlah += 1
        rerata = sum / jumlah

    except ValueError:
        print('Bukan bilangan bulat!!')

    except NameError:
        again = input('Anda yakin ingin keluar program? (y/n): ')
        if again == 'y' or again == 'Y':
            print('\nTerimakasih :v')
            break
