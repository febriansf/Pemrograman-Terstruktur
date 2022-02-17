## Latihan:
1.	Buatlah kode program dengan Python untuk menentukan status kelulusan ujian mahasiswa. Syarat kelulusan adalah:
-	Tidak ada nilai yang kurang dari 60, dan
-	Nilai matematikanya harus di atas 70
Keterangan:
-	Input berupa nilai-nilai mata pelajaran: bhs indonesia, matematika, ipa
-	Range input nilai adalah 0 - 100
Contoh tampilan:
Masukkan nilai Bhs Indonesia : 50Masukkan nilai IPA   : 70Masukkan nilai Matematika : 80
Status Kelulusan  : TIDAK LULUS
2.	Modifikasilan kode program yang sudah dibuat pada soal nomor 1, sehingga bisa menolak nilai yang tidak valid (di luar range 0-100).



Contoh tampilan:

Masukkan nilai Bhs Indonesia : -2Masukkan nilai IPA  : 70Masukkan nilai Matematika : 100

Maaf input ada yang tidak valid

3.	Modifikasilah kode program yang sudah dibuat pada soal nomor 2, sehingga menampilkan sebab ketidaklulusannya pada output program.
Contoh tampilan:

Masukkan nilai Bhs Indonesia : 50Masukkan nilai IPA  : 70Masukkan nilai Matematika : 40
Status Kelulusan  : TIDAK LULUS
Sebab    : 
-	Nilai bahasa indonesia kurang dari 60
-	Nilai matematikanya kurang dari 70

4.	Buatlah kode program Python untuk menentukan gaji pokok dan gaji bersih dari seorang karyawan berdasarkan golongannya. Berikut ini adalah aturan perhitungan gaji pokoknya:

Golongan | Gaji Pokok | Potongan
---------|------------|----------
A | Rp 10.000.000 | 2.5%
B | Rp 8.500.000 | 2.0%
C | Rp 7.000.000 | 1.5%
D | Rp 5.500.000 | 1.0%

Contoh tampilan program:

Masukkan kode karyawan : XXXXXMasukkan nama karyawan : XXXXXMasukkan golongan  : XXX

====================================STRUK RINCIAN GAJI KARYAWAN-----------------------------------------------------------
Nama Karyawan  : XXXXX (Kode: XXXXX)
Golongan   : XXX-----------------------------------------------------------
Gaji Pokok   : Rp XXXXXX
Potongan (XXXX %)  : Rp XXXXXX------------------------------------------------------------
Gaji Bersih   : Rp XXXXXX

Keterangan: Program harus bisa memvalidasi golongan yang diinputkan
5.	Modifikasilah kode program yang dihasilkan dari nomor 4, apabila dalam perhitungan gaji terdapat tunjangan-tunjangan sbb:
-	Tunjangan istri/suami : 10% dari gaji pokok (jika statusnya menikah)
-	Tunjangan anak  : 5% dari gaji pokok untuk setiap anak (jika memiliki anak)        dan statusnya menikah
Adapun rumus untuk menghitung gaji bersih adalah sbb:
Gaji Kotor = Gaji Pokok + Tunjangan Istri/suami + Tunjangan anak 
Gaji Bersih = Gaji Kotor – Potongan
Keterangan:Perhitungan potongan dilakukan terhadap gaji kotor, yang besar % nya menyesuaikan golongan karyawan
Contoh Tampilan:
Masukkan kode karyawan  : XXXXXMasukkan nama karyawan  : XXXXXMasukkan golongan   : XXXMasukkan status (1: menikah, 2: blm) : XXXMasukkan jumlah anak   : XXX    Input ini muncul jika statusnya menikah

====================================STRUK RINCIAN GAJI KARYAWAN-----------------------------------------------------------
Nama Karyawan  : XXXXX (Kode: XXXXX)Golongan   : XXXStatus Menikah   : XXX Jumlah Anak   : XXX   -----------------------------------------------------------Gaji Pokok   : Rp XXXXXXTunjangan Istri/Suami  : Rp XXXXXXTunjangan anak   : Rp XXXXXX----------------------------------------------------------- +Gaji Kotor   : Rp XXXXXXPotongan (XXX %)  : Rp XXXXXX----------------------------------------------------------- -Gaji Bersih   : Rp XXXXXX
