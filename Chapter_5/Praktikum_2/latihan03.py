jumlah = 0
sum = 0
for i in range(100):
    if (i % 2 == 1):
        print(i)
        sum = sum + i
        jumlah = jumlah + 1

print("Jumlah seluruh bilangan:", sum)
print("Banyaknya bilangan ganjil:", jumlah)
