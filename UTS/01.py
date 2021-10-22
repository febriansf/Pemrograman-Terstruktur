#Script untuk menentukan apakah tahun kabisat

print("Apakah merupakan tahun kabisat?")

#Input Angka Tahun
tahun = int(input("Masukkan Tahun: "))

#Menentukan apakah tahun kabisat
if (tahun % 4 == 0):
    isKabisat = 'yes'
elif (tahun % 100 == 0):
    if (tahun % 400 == 0):
        isKabisat = 'yes'
    else:
        isKabisat = 'no'
else:
    isKabisat = 'no'

#Menampilkan output
if (isKabisat == 'yes'):
    print('Tahun', tahun, 'merupakan Tahun Kabisat')
elif (isKabisat == 'no'):
    print('Tahun', tahun, 'bukan Tahun Kabisat')
