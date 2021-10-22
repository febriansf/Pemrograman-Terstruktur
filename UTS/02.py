#Script Permainan menghitung sederhana

from random import randint

nyawa = 3
skor = 0

print('1. Level 1 (Penjumlahan)')
print('2. Level 2 (Pengurangan)')
print('3. Level 3 (Perkalian)')
print('4. Exit')
pilihan = input('Masukkan pilihan kamu: ')

if (pilihan == '1'):
    while True:
        a = randint(-100, 100)
        b = randint(-100, 100)
        hasil = a + b

        if (b > 0):
            print('\nHasil dari', a, '+', b, 'adalah ', end='')
        else:
            print('\nHasil dari', a, '+(' + str(b) + ') adalah ', end='')

        pemain = int(input())

        if (pemain == hasil):
            skor += 2
            print('Jawaban kamu benar, skor kamu', skor,
                    ', Nyawa:', nyawa)
        else:
            nyawa -= 1
            print('Jawaban kamu salah, skor kamu', skor,
                    ', Nyawa:', nyawa)
            if (nyawa == 0):
                print('\n=== (Permainan Berakhir) ===')
                break

elif (pilihan == '2'):
    while True:
        a = randint(-100, 100)
        b = randint(-100, 100)
        hasil = a - b

        if (b > 0):
            print('\nHasil dari', a, '-', b, 'adalah ', end='')
        else:
            print('\nHasil dari', a, '-(' + str(b) + ') adalah ', end='')

        pemain = int(input())

        if (pemain == hasil):
            skor += 2
            print('Jawaban kamu benar, skor kamu', skor,
                    ', Nyawa:', nyawa)
        else:
            nyawa -= 1
            print('Jawaban kamu salah, skor kamu', skor,
                    ', Nyawa:', nyawa)
            if (nyawa == 0):
                print('\n=== (Permainan Berakhir) ===')
                break

elif (pilihan == '3'):
    while True:
        a = randint(-100, 100)
        b = randint(-100, 100)
        hasil = a * b
        print('\nHasil dari', a, 'x', b, 'adalah ', end='')
        pemain = int(input())

        if (pemain == hasil):
            skor += 2
            print('Jawaban kamu benar, skor kamu', skor,
                    ', Nyawa:', nyawa)
        else:
            nyawa -= 1
            print('Jawaban kamu salah, skor kamu', skor,
                    ', Nyawa:', nyawa)
            if (nyawa == 0):
                print('\n=== (Permainan Berakhir) ===')
                break

elif (pilihan == '4'):
    exit()

else:
    print('Maaf, pilihan kamu salah')
    exit()
