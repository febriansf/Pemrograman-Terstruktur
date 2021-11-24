import random


def shuffleString(string, n=1):
    #Membuat sebuah variabel untuk menyimpan list
    listString = list()
    #Iterasi untuk memasukkan element ke dalam listString
    while True:
        #Mengacak tiap karakter pada string
        #Fungsi random.sample akan memecah tiap karakter pada string, mengacaknya
        # -dan mengembalikan nilai dengan tipe data list
        #Menggabungkan nilai kembalian dari random.sample menjadi string
        #-Dan menyimpannya ke dalam variabel randString
        randString = ''.join(random.sample(string, len(string)))
        #Memeriksa apakah nilai randString belum ada dalam listString
        #-Jika True nilai dari randString akan dtambahkan ke dalam listString
        if randString not in listString:
            listString.append(randString)

        #Menghentikan Loop jika sudah mencapai jumlah n
        if (len(listString) == n):
            break

    #Mencetak nilai listString ke konsol
    print(listString)


shuffleString('aku')
shuffleString('aku', 2)
shuffleString('aku', 3)
shuffleString('aku', 4)
