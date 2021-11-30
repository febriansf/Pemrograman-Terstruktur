import time
import random

while True:
    print('=' * 50, '\nProgram untuk men-generate angka acak untuk project 05')
    print('=' * 50)
    try:
        file_name = input('Masukkan nama atau direktori file : ')
        file = open(file_name, 'w')
        sum = int(input('Masukkan banyaknya angka yang ingin dihasilkan : '))
        min_number = int(input('Masukkan batas bawah angka : '))
        max_number = int(input('Masukkan batas atas angka : '))

        for i in range(1, sum+1):
            a = random.randint(min_number, max_number)
            b = random.randint(min_number, max_number)
            file.write(str(a) + '|' + str(b) + '\n')

        for i in range(4):
            print('*')
            time.sleep(1)

        print('\nData disimpan di', file_name)
        break

    except FileNotFoundError:
        print('\nNama file tidak boleh KOSONG!!', '\n')

    except ValueError:
        print('\nAngka tidak boleh KOSONG!!', '\n')
