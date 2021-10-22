def segitiga(baris):
    atas = baris // 2
    for i in range(1, atas+1):
        for j in range(i):
            print("*", end="")
        print("")

    if (baris % 2 == 0):
        bawah = baris // 2
    else:
        bawah = baris // 2 + 1

    for i in range(bawah, 0, -1):
        for i in range(i):
            print("*", end="")
        print("")


segitiga(7)
segitiga(8)
