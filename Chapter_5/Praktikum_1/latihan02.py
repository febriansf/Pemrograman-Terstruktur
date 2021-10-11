status = "Status Kelulusan                       :"

while(True):
    mtk = int(input("Masukan angka nilai Matematika         : "))
    bIndo = int(input("Masukkan angka nilai Bahasa Indonesia  : "))
    ipa = int(input("Masukkan angka nilai IPA               : "))

    if (mtk < 0) or (mtk > 100):
        print("Nilai tidak valid\n")
    elif (bIndo < 0) or (bIndo > 100):
        print("Nilai tidak valid\n")
    elif (ipa < 0) or (ipa > 100):
        print("Nilai tidak valid\n")
    else:
        break

if (mtk < 70):
    print(status, "Tidak Lulus")
elif (ipa < 60) or (bIndo < 60):
    print(status, "Tidak Lulus")
else:
    print(status, "Lulus")
