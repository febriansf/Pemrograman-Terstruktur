def tampilkan_data(data):
    i = 1
    for key, value in data.items():
        print(i, key, ': ', value)
        i += 1


def cekTermahal(data):
    termahal = max(list(data.values()))
    for key, value in data.items():
        if value == termahal:
            return key


buah = {'apel': 5000,
        'jeruk': 8500,
        'mangga': 7800,
        'duku': 6500}

tampilkan_data(buah)
print('Buah termahal adalah', cekTermahal(buah), ':', buah[cekTermahal(buah)])
