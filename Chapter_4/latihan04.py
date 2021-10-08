jarakAkeB = 125
jarakBkeC = 256

kecepatanAkeB = 62
kecepatanBkeC = 70

jamMulai = 6
mntMulai = 0

mntIst = 45 / 60

#waktuTempuh dibulatkan
waktuAkeB = jarakAkeB / kecepatanAkeB
waktuBkeC = jarakBkeC / kecepatanBkeC

#waktuAkeB = round(waktuAkeB, 2)
#waktuBkeC = round(waktuBkeC, 2)

totalWaktu = waktuAkeB + waktuBkeC + mntIst
totalWaktu = round(totalWaktu, 2)

totalJam = int(totalWaktu // 1)
jamTiba = totalJam + jamMulai

totalMnt = totalWaktu % 1
totalMnt = int(totalMnt * 60)

if (mntMulai > 0):
    mntTiba = totalMnt + mntMulai
    if (mntTiba > 59) :
        mntTiba -= 60
        jamTiba += 1
else:
    mntTiba = totalMnt

print("Waktu Tempuh dari Kota A ke B adalah sekitar", waktuAkeB, "Jam")
print("Waktu Tempuh dari Kota B ke C adalah sekitar", waktuBkeC, "Jam")
print("Total waktu perjalanan + istirahat 45 menit adalah", totalWaktu, "jam")
print("Atau", totalJam, "jam", totalMnt, "menit")
print("Jika berangkat pada pukul", jamMulai, "lebih", mntMulai)
print("Tiba di tujuan pada pukul", jamTiba, "lebih", mntTiba)
