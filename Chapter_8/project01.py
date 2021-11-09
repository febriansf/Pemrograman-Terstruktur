try:
    banyak = int(input('Berapa banyak bilangan yang ingin dimasukan? '))
    bil = []

    for i in range(banyak):
        angka = int(input('Masukkan Angka Ke-' + str(i+1) + ': '))
        bil = bil + [angka]

    bil.sort(reverse=True)
    print('Angka yang anda masukkan adalah', bil)

except ValueError:
    print('INPUT BUKAN ANGKA!!')
