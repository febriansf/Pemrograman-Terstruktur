while(True):
    kodeKar = input("Masukkan Kode Karyawan: ")
    namaKar = input("Masukkan Nama Karyawan: ")
    golKar = str(input("Masukkan Golongan     : "))

    if (golKar == "A") or (golKar == "a"):
        gajiPokok = 10000000
        persen = 2.5
    elif (golKar == "B") or (golKar == "b"):
        gajiPokok = 8500000
        persen = 2.0
    elif (golKar == "C") or (golKar == "c"):
        gajiPokok = 7000000
        persen = 1.5
    elif (golKar == "D") or (golKar == "d"):
        gajiPokok = 5000000
        persen = 1.0
    else:
        print("Golongan Tidak Valid")
        continue

    statMenikah = int(input("Masukkan Status (1: Menikah, 2: Belum): "))

    if (statMenikah == 1):
        status = "Menikah"
        tunjMenikah = 10 / 100 * gajiPokok
        jumAnak = int(input("Masukkan jumlah Anak  : "))
        tunjAnak = 5 / 100 * gajiPokok
        tunjAnak = tunjAnak * jumAnak
        break
    elif (statMenikah == 2):
        status = "Belum Menikah"
        tunjMenikah = 0
        tunjAnak = 0
        jumAnak = "-"
        break
    else:
        print("Status Menikah Tidak Valid")

gajiKotor = gajiPokok + tunjMenikah + tunjAnak
potongan = persen / 100 * gajiKotor
gajiBersih = gajiKotor - potongan

print("=====================================")
print("STRUK RINCIAN GAJI KARYAWAN")
print("-------------------------------------")
print("Nama Karyawan    : " + namaKar + " (Kode : " + kodeKar + ")")
print("Golongan         : " + golKar)
print("Status Menikah   : " + status)
print("Jumlah Anak      : " + str(jumAnak))
print("-------------------------------------")
print("Gaji Pokok       : Rp.", gajiPokok)
print("Tunjangan Menikah: Rp.", int(tunjMenikah))
print("Tunjangan Anak   : Rp.", int(tunjAnak))
print("-------------------------------------")
print("Gaji Kotor       : Rp.", int(gajiKotor))
print("Potongan (" + str(persen) + "%)  : Rp.", int(potongan))
print("-------------------------------------")
print("Gaji Bersih      : Rp.", int(gajiBersih))
print("-------------------------------------")
