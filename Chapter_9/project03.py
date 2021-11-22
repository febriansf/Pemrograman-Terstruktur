def diamond(baris):
    space = baris

    #Inner function untuk mencetak bagian atas
    def atas(n):
        for i in range(n):
            print(('*' * (2 * i + 1)).center(space))

    #Inner function untuk mencetak bagian bawah
    def bawah(n):
        for i in range(n, 0, -1):
            print(('*' * (2 * i - 1)).center(space))

    atas(baris // 2)
    #Cek Jika baris = genap, baris bagian bawah - 1
    if (baris % 2 == 0):
        bawah(baris//2)
    else:
        bawah(baris//2+1)


#Main Program
diamond(7)
