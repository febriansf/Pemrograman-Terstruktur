def ubahHuruf(teks, a, b):
    if a in teks:
        teks = teks.replace(a, b)
        print(teks)
    else:
        print('Huruf', a, 'Tidak ada dalam', teks)


ubahHuruf('MATEMATIKA', 'A', 'S')
