mhs = ['K001:ROSIHAN ARI:1979-09-01:SOLO',
       'K002:DWI AMALIA FITRIANI:1979-09-17:KUDUS',
       'K003:FAZA FAUZAN:2005-01-28:KARANGANYAR']

print('=' * 60)
print('NIM'.ljust(10),
      'NAMA MAHASISWA'.ljust(20),
      'TGL LAHIR'.ljust(20),
      'ALAMAT'.ljust(20))
print('-' * 60)

#Iterasi untuk membaca tiap element dalam list mhs
for i in range(len(mhs)):
    #Memecah tiap nilai dalam list mhs menjadi sublist
    x = mhs[i].split(':')
    #Nilai awal jarak untuk jusifikasi
    jarak = 11
    #Iterasi untuk mencetak nilai dalam sublist
    for j in range(len(x)):
        #Jika sampai pada index 2 pada sublist yg mana adalah tgl lahir
        if j == 2:
            #Memecah string tgl lahir menjadi sublist berdasarkan karakter '-'
            tgl = x[j].split('-')
            #Membalik urutan element dalam sublist tgl
            tgl.reverse()
            #Menggabungkan sublist tgl menjadi string dan mencetaknya ke konsol
            print('/'.join(tgl).ljust(jarak), end='')
            #Melompati syntax berikutnya karena nilai tgl sudah dieksekusi
            continue
        print(x[j].ljust(jarak), end='')
        #Mengubah nilai jarak untuk justifikasi
        jarak = 21
    #Mencetak newline
    print('')
