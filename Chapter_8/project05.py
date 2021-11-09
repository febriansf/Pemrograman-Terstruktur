def kuadrat(bil):
    x = []
    for data in bil:
        data = data ** 2
        x = x + [data]

    return x


bil = [2, 4, 5, 6]
print('Kuadrat dari list', bil)
print('adalah', kuadrat(bil))
