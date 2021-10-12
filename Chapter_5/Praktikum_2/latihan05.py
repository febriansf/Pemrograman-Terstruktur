import random

angka = random.randint(0, 100)

print("Tebaklah angka yang ada di memoriku, antara 1 sampai 100")


while(True):

    jawab = int(input("\nTebakan Kamu: "))
    if (jawab > angka):
        print("Tebakan kamu terlalu besar")
    elif (jawab < angka):
        print("Tebakan kamu terlalu kecil")
    else:
        print("Tebakan kamu benar!!")
        print("Jawabannya adalah", angka)
        break
