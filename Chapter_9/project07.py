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
for data in mhs:
    #Memecah element string pada list menjadi sublist
    #-berdasarkan karakter '-'
    split_data = data.split(':')
    #Mendefinsikan jarak spasi awal
    space = 11
    #Iterasi untuk mencetak tiap elemen pada sublist data
    for i in range(len(split_data)):
        #Jika sampai pada index 2 yang berisi string tgl lahir
        if i == 2:
            #Memecah string tgl lahir menjadi list
            #-dan menyimpannya pada variabel tgl
            tgl = split_data[i].split('-')
            #Membalik urutan index list tgl
            tgl.reverse()
            #Menggabungkan elemen pada list tgl menjadi string
            #-dan mencetaknya ke konsol
            print('/'.join(tgl).ljust(space), end='')
            #Melompati syntax berikutnya
            continue
        print(split_data[i].ljust(space), end='')
        #Mendefinisikan jarak spasi selanjutnya
        space = 21
    #Pindah baris
    print('')
