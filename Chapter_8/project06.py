def length(x):
    return len(x)


def sortString(list):
    list.sort(key=length, reverse=True)
    return list


myData = ['apel', 'rambutan', 'jeruk ']
print('List', myData)
print('Diurutkan berdasarkan jumlah karakter')
print('menjadi', sortString(myData))
