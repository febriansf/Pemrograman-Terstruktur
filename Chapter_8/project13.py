def cari_nilai_tertinggi(list):
    #Mencari nilai akhir dan
    #Memasukkannya ke dalam list_nilai_akhir
    list_nilai_akhir = []
    for data in list:
        mid = data['mid']
        uas = data['uas']
        nilai_akhir = (mid + 2 * uas)/3
        list_nilai_akhir += [round(nilai_akhir, 1)]

    #Mencari nilai tertinggi dari list_nilai_akhir
    #Kemudian cek apabila ada nilai akhir yang sama
    #Variabel nomor_index untuk menyimpan nomor urut dari list nilaiMhs-
    #-Pemilik nilai akhir tertinggi
    nomor_index = []
    i = 0
    for nilai_akhir in list_nilai_akhir:
        tertinggi = max(list_nilai_akhir)
        if nilai_akhir == tertinggi:
            nomor_index += [i]
        i += 1

    #Menampilkan output nama dan nim dari pemilik nilai akhir tertinggi
    for i in nomor_index:
        print('Nama:', list[i]['nama'],
              '(' + list[i]['nim'] + ')',
              'dengan nilai akhir', list_nilai_akhir[i])


nilaiMhs = [{'nim': 'A01', 'nama': 'Amir', 'mid': 50, 'uas': 80},
            {'nim': 'A02', 'nama': 'Budi', 'mid': 40, 'uas': 90},
            {'nim': 'A03', 'nama': 'Cici', 'mid': 50, 'uas': 50},
            {'nim': 'A04', 'nama': 'Dedi', 'mid': 20, 'uas': 30},
            {'nim': 'A05', 'nama': 'Fifi', 'mid': 70, 'uas': 40}]

cari_nilai_tertinggi(nilaiMhs)
