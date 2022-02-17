## Praktikum 1
Langkah Kerja:
  1.	Buka Python IDLE atau Python IDE lainnya
  2.	Buatlah folder dengan nama ‘PythonProjects’ di sembarang direktori
  3.	Buatlah file baru dengan nama latihan01.py 
  4.	Ketikkan kode program berikut ini

        ```python
        print("Hello world")

  5.	Simpan kembali file latihan01.py 
  6.	Jalankan kode program latihan01.py
  7.	Amati hasilnya, kemudian simpulkan apa kegunaan dari perintah print()
  

## Praktikum 2
Langkah Kerja:
  1.	Buat file latihan02.py
  2.	Ketikkan kode program berikut ini di dalam file latihan02.py
  
        ```python
        print("Hello world ")
        print("Hello world ")
        print("Hello world ")

  3.	Jalankan kode program tersebut, lalu amati hasilnya!
  4.	Coba carilah referensi di internet, kemudian modifikasilah kode program di atas supaya tampilan output dari kode program di atas menjadi (masih menggunakan 3 buah print())


## Praktikum 3
 Langkah Kerja:
  1.	Buatlah file baru dengan nama latihan03.py
  2.	Ketikkan kode program berikut ini

        ```python
        # import library
        import time
        import datetime

        # input nama user
        nama = input("Hallo... nama saya Mr. Kompie, nama Anda siapa? ")

        ## tampilkan nama user
        print("Oh.. nama Anda", nama, ", nama yang bagus sekali.")


        # kasih jeda 3 detik
        time.sleep(3)

        # input tahun lahir
        thnLahir = int(input("BTW... " + nama + "kamu lahir tahun berapa? "))

        # kasih jeda 3 detik
        time.sleep(3)

        # hitung usia user 
        skrg = datetime.datetime.now()
        usia = skrg.year + thnLahir
        
        # tampilkan usia
        print("Hmmm...", namax,"kamu sudah", usia,"tahun ya..")
        
        # kasih jeda 3 detik
        time.sleep(3)
        
        # tampilkan pesan sesuai range usia
        if (usia > 50):
            print("Anda sudah cukup tua ya?)
            print("Jaga kesehatan ya!!")
        elif (usia > 20)
            print("Ternyata Anda masih cukup muda belia")
            print("Jangan sia-siakan masa mudamu ya!!")
        elif (usia > 17):
            print("Hihihi... Anda ternyata masih ABG")
            print("Mulai berpikirlah secara dewasa ya!!"
        else:
            print("Oalah.. Anda masih anak-anak toh?")
            print("Jangan suka merengek-rengek minta jajan ya!!")
        
        # kasih jeda 3 detik
        time.sleep(3)
        
        # say goodbye
        print("OK.. see you later", nama, ".. senang berkenalan denganmu")
        
        
  3.	Simpan file latihan03.py
  4.	Jalankan kode program latihan03.py
  5.	Apakah terdapat error? Jika Ya, maka jelaskan penyebab errornya!
  6.	Lakukan perbaikan terhadap setiap error yang muncul!
  7.	Jika sudah tidak error, maka coba lakukan input dengan beberapa macam variasi data input
  8.	Apakah masih terdapat error terhadap hasilnya? Jika ya maka jelaskan penyebabnya!
  9.	Lakukan perubahan terhadap kode program sehingga hasilnya benar!
  10.	Apa kegunaan dari:

        * a.	Tanda #
        * b.	Perintah input()
        * c.	Perintah int()

  11.	Apa yang terjadi jika perintah import time dihapus?
