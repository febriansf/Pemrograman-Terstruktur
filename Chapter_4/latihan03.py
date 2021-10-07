jarakKota = 795
jarakPerLiter = 12
maksTangki = 50

totalBensin = jarakKota / jarakPerLiter

isiBensin = int(totalBensin // 50)


print("Total Bensin yang diperlukan untuk sampai di kota C adalah", totalBensin, "Liter")
print("Total isi bensin di pom adalah", isiBensin, "kali")
