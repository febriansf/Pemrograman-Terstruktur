# Jarak ke Kota C
jarakKota = 795

# 1 Liter Bensin = 12KM
jarakPerLiter = 12

# Kapasitas Maksimal Tangki 50 Liter
maksTangki = 50

# Hitung penggunaan bensin
totalBensin = jarakKota / jarakPerLiter

# Hitung banyak isi bensin
isiBensin = int(totalBensin // maksTangki)

# Menampilkan Hasil
print("Total Bensin yang diperlukan untuk sampai di kota C adalah",
      totalBensin, "Liter")
print("Total isi bensin di pom adalah", isiBensin, "kali")
