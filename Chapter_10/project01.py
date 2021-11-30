file = open("file/numbers.txt", 'r')

#Variabel untuk menyimpan banyaknya bilangan genap
even_number = 0
#Variabel untuk menyimpan banyaknya bilangan ganjil
odd_number = 0

while True:
    try:
        read_data = file.readline()
        if not read_data:
            print('Banyaknya bilangan genap:', even_number)
            print('Banyaknya bilangan ganjil:', odd_number)
            break

        number = int(read_data)

        if (number % 2 == 0):
            even_number += 1
        else:
            odd_number += 1
    except:
        continue
