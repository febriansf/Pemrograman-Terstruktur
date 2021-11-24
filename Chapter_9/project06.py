nilai = [{'nim': 'A01', 'nama': 'Agustina', 'mid': 50, 'uas': 80},
         {'nim': 'A02', 'nama': 'Budi', 'mid': 40, 'uas': 90},
         {'nim': 'A03', 'nama': 'Chicha', 'mid': 100, 'uas': 50},
         {'nim': 'A04', 'nama': 'Donna', 'mid': 20, 'uas': 100},
         {'nim': 'A05', 'nama': 'Fatimah', 'mid': 70, 'uas': 100},
         {'nim': 'A06', 'nama': 'Abdul', 'mid': 70, 'uas': 50}]

print('=' * 70)
print('NIM'.ljust(10), 'NAMA'.ljust(10), 'N.MID'.rjust(10),
      'N.UAS'.rjust(10), 'N.AKHIR'.rjust(10), 'STATUS'.rjust(12))
print('-' * 70)

#Iterasi untuk membaca value dari key 'mid' dan 'uas' dari setiap dictionary dalam list nilai
for data in nilai:
    #Menghitung nilai akhir berdasarkan rumus (mid + 2 * uas) / 3
    nilaiAkhir = (data['mid'] + (2 * data['uas'])) / 3
    #Menambahkan nilai akhir ke dalam dictionary
    data['nilaiAkhir'] = round(nilaiAkhir, 1)

    #Menambahkan status ke dalam dictionary berdasarkan nilai akhir
    if nilaiAkhir >= 60:
        data['status'] = 'LULUS'
    else:
        data['status'] = 'TIDAK LULUS'

    #Mencetak element dalam list dictionary nilai Ke Konsol
    print(data['nim'].ljust(10),
          data['nama'].ljust(10),
          str(data['mid']).rjust(10),
          str(data['uas']).rjust(10),
          str(data['nilaiAkhir']).rjust(10), ''.rjust(5),
          data['status'].ljust(5))

print('-' * 70)
