status = "Status Kelulusan                       : "

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
    lulus = "Tidak Lulus"
    print(status + lulus)
elif (ipa < 60) or (bIndo < 60):
    lulus = "Tidak Lulus"
    print(status + lulus)
else:
    lulus = "Lulus"
    print(status + lulus)

if (lulus == "Tidak Lulus"):
    print("Sebab                                  :")
    if (mtk < 70):
        print("- Nilai Matematika kurang dari 70")
    if (ipa < 60):
        print("- Nilai IPA kurang dari 60")
    if (bIndo < 60):
        print("- Nilai Bahasa Indonesia Kurang dari 60")
