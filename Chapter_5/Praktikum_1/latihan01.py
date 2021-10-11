status = "Status Kelulusan                       :"

mtk = int(input("Masukan angka nilai Matematika         : "))
bIndo = int(input("Masukkan angka nilai Bahasa Indonesia  : "))
ipa = int(input("Masukkan angka nilai IPA               : "))

if (mtk < 70):
    print(status, "Tidak Lulus")
elif (ipa < 60) or (bIndo < 60):
    print(status, "Tidak Lulus")
else:
    print(status, "Lulus")
