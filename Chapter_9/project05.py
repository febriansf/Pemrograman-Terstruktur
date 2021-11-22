nilai = [{'nim': 'A01', 'nama': 'Agustina', 'mid': 50, 'uas': 80},
         {'nim': 'A02', 'nama': 'Budi', 'mid': 40, 'uas': 90},
         {'nim': 'A03', 'nama': 'Chicha', 'mid': 100, 'uas': 50},
         {'nim': 'A04', 'nama': 'Donna', 'mid': 20, 'uas': 100},
         {'nim': 'A05', 'nama': 'Fatimah', 'mid': 70, 'uas': 100}]


print('=' * 50)
print('NIM'.ljust(10), 'NAMA'.ljust(10), 'N.MID'.rjust(10), 'N.UAS'.rjust(10))
print('-' * 50)
#Iterasi untuk membaca list dictionary nilai
for i in range(len(nilai)):
    print(nilai[i]['nim'].ljust(10),
          nilai[i]['nama'].ljust(10),
          str(nilai[i]['mid']).rjust(10),
          str(nilai[i]['uas']).rjust(10))

print('-' * 50)
