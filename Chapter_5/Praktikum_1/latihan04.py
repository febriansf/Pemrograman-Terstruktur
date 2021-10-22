while(True):
    kodeKar = input("Masukkan Kode Karyawan: ")
    namaKar = input("Masukkan Nama Karyawan: ")
    golKar = str(input("Masukkan Golongan     : "))

    if (golKar == "A") or (golKar == "a"):
        gajiPokok = 10000000
        persen = 2.5
        break
    elif (golKar == "B") or (golKar == "b"):
        gajiPokok = 8500000
        persen = 2.0
        break
    elif (golKar == "C") or (golKar == "c"):
        gajiPokok = 7000000
        persen = 1.5
        break
    elif (golKar == "D") or (golKar == "d"):
        gajiPokok = 5500000
        persen = 1.0
        break
    else:
        print("Golongan Tidak Valid")

potongan = persen / 100 * gajiPokok
gajiBersih = gajiPokok - potongan

print("=====================================")
print("STRUK RINCIAN GAJI KARYAWAN")
print("-------------------------------------")
print("Nama Karyawan    : " + namaKar + " (Kode : " + kodeKar + ")")
print("Golongan         : " + golKar)
print("-------------------------------------")
print("Gaji Pokok       : Rp.", gajiPokok)
print("Potongan (" + str(persen) + "%)  : Rp.", int(potongan))
print("-------------------------------------")
print("Gaji Bersih      : Rp.", int(gajiBersih))
