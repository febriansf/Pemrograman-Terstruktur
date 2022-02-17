# Latihan
1.	Buatlah function `isPythagoras(a, b, c)` yang digunakan untuk menentukan apakah pasangan a, b, c yang merupakan sisi-sisi sebuah segitiga merupakan triple Pythagoras atau bukan. Function tersebut menghasilkan nilai boolean: `True` apabila a, b, c merupakan triple Pythagoras, dan `False` jika ketiganya bukan triple Pythagoras.

    *Keterangan: c merupakan sisi miring segitiga*

    Untuk mengecek benar tidaknya function yang Anda buat, ujilah dengan beberapa pasangan nilai a, b, c berikut ini
    - a.	a = 3, b = 4, c = 5  -> True
    - b.	a = 5, b = 9, c = 12 -> False
    - c.	a = 8, b = 6, c = 10 -> True
    - d.	a = 7, b = 8, c = 11 -> False
    
2.	Buatlah function `starFormation1(n)` yang digunakan untuk mencetak output berupa formasi bintang berikut ini
    ```
      *
      * *
      * * *
      * * * *
    ```
    *(contoh output function jika n = 4)*
    
    Dan buat pula function `starFormation2(n)` yang digunakan untuk mencetak output berupa formasi bintang berikut ini
    ```
      * * * *
      * * *
      * *
      *
    ```
    *(contoh output function jika n = 4)*

    Berdasarkan kedua function tersebut, gunakan keduanya untuk membentuk formasi bintang sebagai berikut
    ```
      *
      * *
      * * *
      * * * *
      * * *
      * *
      *
    ```

    *(contoh output program jika n = 7)*
    
3.	Buatlah function `faktorial(n)` yang digunakan untuk menghitung nilai n faktorial. Output dari function ini adalah sebuah bilangan yang merupakan nilai dari n faktorial tersebut.
    Gunakan function tersebut untuk menghitung nilai dari:
      - a.	C(5, 3)
      - b.	P(10, 7)
      
4.	Buatlah sebuah file Python dengan nama `statistik.py` yang hanya berisi function-function berikut ini:

      - a.	Buatlah function `sum(a, b, c, d, …)` dengan jumlah parameter tidak terbatas, yang digunakan untuk mencari jumlah total seluruh nilai parameternya yang berupa bilangan. Misalnya: sum(3, 5, 6, 7) akan menghasilkan nilai 21, sum(1, 0, 0, 2, 4) akan menghasilkan nilai 7.

          *Petunjuk: pelajari modul teori bab 6 untuk membuat function dengan parameter dinamis seperti pada kasus ini*
      - b.	Buatlah function `average(a, b, c, d, …)` dengan jumlah parameter tidak terbatas, yang digunakan untuk mencari rata-rata dari seluruh nilai parameternya yang berupa bilangan. Manfaatkan function sum(a, b, c, d, …) untuk menghitung jumlah total data dalam proses perhitungan rata-ratanya. 
      - c.	Buatlah function `maks(a, b, c, d, …)` dengan jumlah parameter tidak terbatas, yang digunakan untuk mencari nilai maksimum dari seluruh nilai parameternya.
      - d.	Buat pula function `min(a, b, c, d, …)` dengan jumlah parameter tidak terbatas, yang digunakan untuk mencari nilai minimum dari seluruh nilai parameternya.
5.	Gunakan function-function yang ada di `statistik.py` untuk mencari rata-rata, nilai maks, dan minimum dari data-data berikut ini:
      - a.	5, 10, 4, 9, 30, 16, 2, 11
      - b.	81, 98, 12, 83, 45, 77, 69, 30, 56
