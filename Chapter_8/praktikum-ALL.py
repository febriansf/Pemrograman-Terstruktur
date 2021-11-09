a = [1, 5, 6, 3, 6, 9, 11, 20, 12]
b = [7, 4, 5, 6, 7, 1, 12, 5, 9]

#Menambahkan Nilai 10 ke dalam indeks ke-3 dari list a
#Menambahkan Nilai 15 ke dalam indeks ke-2 dari list b
a.insert(3, 10)
b.insert(2, 15)
print('a =', a)
print('b =', b)

#Menambahkan Nilai 4 ke indeks terakhir list a
#Menambahkan Nilai 8 ke indeks terakhir list b
a.append(4)
b.append(8)
print('a =', a)
print('b =', b)

#Mengurutkan list a dan b secara ascending
a.sort()
b.sort()
print('a =', a)
print('b =', b)

#Mendefinisikan list c yang elemennya dari sublist a[0-7]
#Mendefinisikan list d yang elemennya dari sublist b[2-9]
c = a[:8]
d = b[2:10]

print('c =', c)
print('d =', d)
#Mendefinisikan list e yang elemennya dari penjumlahan dari setiap elemen dari
#list c dan d yang sama nilai indexnya
e = []
if len(c) >= len(d):
    try:
        for i in range(len(c)):
            e += [c[i] + d[i]]
    except IndexError:
        e += [c[i] + 0]
elif len(c) < len(d):
    try:
        for i in range(len(d)):
            e += [c[i] + d[i]]
    except IndexError:
        e += [0 + d[i]]

print('e =', e)

#Mengkonversi list e ke tipe data tuple
tuple_e = tuple(e)
print('E_Tuple =', tuple_e)

#Mencari nilai minimum dari elemen tuple_e
print('Nilai minimum dari tuple', tuple_e, 'adalah', min(tuple_e))
#Mencari nilai maximum dari elemen tuple_e
print('Nilai maximum dari tuple', tuple_e, 'adalah', max(tuple_e))
#Mencari jumlah seluruh elemen tuple_e
print('Jumlah seluruh elemen tuple', tuple_e, 'adalah', sum(tuple_e))

#Mendefinisikan variabel myString
myString = 'python adalah bahasa pemrograman yang menyenangkan'
print(myString)

#Melihat karakter huruf penyusun myString
huruf = set(myString)
print('Huruf penyusun =', huruf)

#Mengurutkan himpunan karakter huruf berdasarkan alfabet
list_huruf = list(huruf)
list_huruf.sort()
print('Setelah diurutkan alfabet', list_huruf)
