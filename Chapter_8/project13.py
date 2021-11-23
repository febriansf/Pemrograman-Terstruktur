def cari_nilai_tertinggi(list):
    #Iterasi untuk mencari nilai akhir dan memasukkannya ke dictionary
    for daftar in list:
        nilai_akhir = ((daftar['mid'] + (2 * daftar['uas'])) / 3)
        daftar['nilai_akhir'] = round(nilai_akhir, 2)

    #stackoverflow is my friend
    #Menggunakan perulangan for untuk
    #-menentukan nilai akhir tertinggi"""
    tertinggi = max([x['nilai_akhir'] for x in list])

    #Iterasi untuk mencetak nilai akhir tertinggi ke konsol
    for nilai in list:
        if nilai['nilai_akhir'] >= tertinggi:
            print('Nama:', nilai['nama'],
                  '(' + nilai['nim'] + ')',
                  'dengan nilai akhir', nilai['nilai_akhir'])


#Main Program
nilaiMhs = [{'nim': 'A01', 'nama': 'Amir', 'mid': 50, 'uas': 80},
            {'nim': 'A02', 'nama': 'Budi', 'mid': 40, 'uas': 90},
            {'nim': 'A03', 'nama': 'Cici', 'mid': 50, 'uas': 50},
            {'nim': 'A04', 'nama': 'Dedi', 'mid': 20, 'uas': 30},
            {'nim': 'A05', 'nama': 'Fifi', 'mid': 70, 'uas': 40}, ]

cari_nilai_tertinggi(nilaiMhs)
