from random import randint

angka = randint(1, 100)
skor = 100

print("Tebak angka yang aku pikirkan antara 1 sampai 100")


while(True):

    jawab = int(input("\nTebakan Kamu: "))
    if (jawab > angka):
        print("Tebakan kamu terlalu besar")
        skor -= 2
    elif (jawab < angka):
        print("Tebakan kamu terlalu kecil")
        skor -= 2
    else:
        print("Tebakan kamu benar!!")
        #print("Jawabannya adalah", angka)
        print("Skor Kamu adalah", skor)
        break
    if (skor < 0):
        skor = 0
