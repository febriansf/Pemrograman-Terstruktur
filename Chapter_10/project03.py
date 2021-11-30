file = open('file/data.mhs', 'r')

dataMhs = list()
while True:
    read_file = file.readline()
    if not read_file:
        file.close()
        break
    split_data = read_file.split('|')
    last_element = len(split_data) - 1
    split_data[last_element] = split_data[last_element].replace('\n', '')

    data = dict()
    data['nim'] = split_data[0]
    data['nama'] = split_data[1]
    data['alamat'] = split_data[2]
    dataMhs.append(data)


print('dataMhs =', dataMhs)
#for data in dataMhs:
#print(data)
