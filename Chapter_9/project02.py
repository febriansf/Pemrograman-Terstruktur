def bintang(n):
    space = 2*n-1
    char = '*'
    #iterasi untuk mencetak segitiga ke konsol
    for i in range(n):
        count = 2 * i + 1
        print((char * count).center(space))


bintang(4)
