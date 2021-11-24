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

    #Cek nilai baris
    if baris % 2 == 0:
        print("Error... Jumlah baris harus bilangan ganjil")
    else:
        atas(baris//2)
        bawah(baris//2+1)


#Main Program
diamond(7)
