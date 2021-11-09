def dataStat(x):
    x = tuple(x)
    maks = max(x)
    minimum = min(x)
    average = sum(x) / len(x)

    return [round(average, 2), maks, minimum]


data = [6, 5, 10]
print('Mencari [Rata-rata, Max, Min] dari', data)
print('adalah', dataStat(data))
