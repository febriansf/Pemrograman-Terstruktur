nilai = [{'nim': 'A01', 'nama': 'Agustina', 'mid': 50, 'uas': 80},
         {'nim': 'A02', 'nama': 'Budi', 'mid': 40, 'uas': 90},
         {'nim': 'A03', 'nama': 'Chicha', 'mid': 100, 'uas': 50},
         {'nim': 'A04', 'nama': 'Donna', 'mid': 20, 'uas': 100},
         {'nim': 'A05', 'nama': 'Fatimah', 'mid': 70, 'uas': 100}]

#Iterasi untuk membaca 'mid' dan 'uas' dari setiap dictionary dalam list nilai
for i in range(len(nilai)):
    #Menghitung nilai akhir berdasarkan rumus (mid + 2 * uas) / 3
    nilaiAkhir = (nilai[i]['mid'] + (2 * nilai[i]['uas'])) / 3
    #Menambahkan nilai akhir ke dalam dictionary
    nilai[i]['nilaiAkhir'] = round(nilaiAkhir, 1)

    #Menambahkan status ke dalam dictionary berdasarkan nilai akhir
    if nilaiAkhir >= 60:
        nilai[i]['status'] = 'LULUS'
    else:
        nilai[i]['status'] = 'TIDAK LULUS'


print('=' * 70)
print('NIM'.ljust(10), 'NAMA'.ljust(10), 'N.MID'.rjust(10),
      'N.UAS'.rjust(10), 'N.AKHIR'.rjust(10), 'STATUS'.rjust(12))
print('-' * 70)

#Iterasi untuk membaca list dictionary nilai
for i in range(len(nilai)):
    print(nilai[i]['nim'].ljust(10),
          nilai[i]['nama'].ljust(10),
          str(nilai[i]['mid']).rjust(10),
          str(nilai[i]['uas']).rjust(10),
          str(nilai[i]['nilaiAkhir']).rjust(10), ''.rjust(5),
          nilai[i]['status'].ljust(5))

print('-' * 70)
