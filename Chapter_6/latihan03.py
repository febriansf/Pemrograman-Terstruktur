#Menghitung faktorial menggunakan perulangan for
def faktorial(n):
    hasil = 1
    for i in range(1, n+1):
        hasil *= i
    return hasil

#Menghitung faktorial menggunakan perulangan while
#def faktorial(n):
#    hasil = 1
#    while (n > 1):
#        hasil *= n
#        n -= 1
#    return hasil

#Menghitung faktorial menggunakan konsep rekursif
#def faktorial(n):
#    if (n > 1):
#        return n * (faktorial(n - 1))
#    else:
#        return 1

#Menghitung Kombinasi
def C(a, b):
    return faktorial(a)/(faktorial(b)*faktorial(a-b))

#Menghitung Permutasi
def P(a, b):
    return faktorial(a)/faktorial(a-b)


print(C(5, 3))
print(P(10, 7))
