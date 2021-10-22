def max(*angka):
    maks = angka[0]

    for i in angka:
        if i > maks:
            maks = i

    return maks

print(max(1, 14, 6, 10))
