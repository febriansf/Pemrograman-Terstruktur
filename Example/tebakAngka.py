import random

angka = random.randint(0,100)
nyawa = 7

print("Tebak angka antara 1 sampai 100")
print("Kamu memiliki", nyawa, "kesempatan untuk menjawab")


while(True):

    jawab = int(input("\nTebakan Kamu: "))
    if (jawab > angka):
        print("Tebakan kamu terlalu besar")
        nyawa -= 1
        print("Sisa", nyawa, "Kesempatan")
    elif (jawab < angka):
        print("Tebakan kamu terlalu kecil")
        nyawa -=1
        print("Sisa", nyawa, "Kesempatan")
    else:
        print("Tebakan kamu benar!!")
        print("Jawabannya adalah", angka)
        break
    if (nyawa == 0):
        print("\nKesempatan Kamu habis")
        print("Jawabannya adalah", angka)
        break
