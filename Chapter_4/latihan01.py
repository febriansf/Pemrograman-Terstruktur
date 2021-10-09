
# Waktu Rental
# Rental dimulai pukul 06.00 - 23.50
jamMasuk = 6
mntMasuk = 0
jamKeluar = 23
mntKeluar = 50

# Biaya Rental per 1 jam
biaya1Jam = 10000

# Biaya Rental 12 Jam pertama
biaya12Jam = 200000

# Hitung Durasi Waktu
slshJam = jamKeluar - jamMasuk
slshMnt = mntKeluar - mntMasuk

# Jika Menit Keluar < Menit Masuk
# Selisih Jam akan dikurangi 1
# Selisih Menit akan ditambah 60
if (slshMnt < 0):
    slshJam -= 1
    slshMnt += 60

# Hitung Total Biaya Rental berdasarkan Selisih Waktu
if (slshJam >= 12):
    totalBiaya = biaya12Jam + biaya1Jam * (slshJam - 12)
    if (slshMnt > 0):
        totalBiaya = totalBiaya + slshMnt * (biaya1Jam / 60)

else:
    totalBiaya = biaya12Jam

# Menampilkan Output
print("Rental mulai pada jam", jamMasuk, "lebih", mntMasuk)
print("Dan berakhir pada jam", jamKeluar, "lebih", mntKeluar)
print("Total Durasi Rental adalah", slshJam, "Jam", slshMnt, "Menit")
print("Total Biaya Rental adalah Rp.", totalBiaya)
print("Jika dibulatkan menjadi Rp.", round(totalBiaya))
