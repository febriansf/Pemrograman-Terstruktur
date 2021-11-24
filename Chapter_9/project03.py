def diamond(baris):
    space = baris
    #Cek nilai baris apakah bukan ganjil
    if baris % 2 == 0:
        print("Error... Jumlah baris harus bilangan ganjil")
    #Jika ganjil maka
    else:
        #Iterasi untuk mencetak baris pertama sampai baris // 2 + 1
        for i in range(baris//2+1):
            print(('*' * (2 * i + 1)).center(space))

        #Iterasi untuk mencetak baris sisanya sampai selesai
        for i in range(baris//2, 0, -1):
            print(('*' * (2 * i - 1)).center(space))


#Main Program
diamond(7)
