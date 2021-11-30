source_file = 'file/data.numbers'
dest_file = source_file + '.SUM'

#File berisi bilangan dengan format bil1|bil2
file_data = open(source_file, 'r')
#File baru untuk menyimpan hasil penjumlahan
new_file = open(dest_file, 'w')

while True:
    read_data = file_data.readline()
    if not read_data:
        file_data.close()
        new_file.close()
        break

    split_data = read_data.split('|')
    split_data[1] = split_data[1].replace('\n', '')

    sum = int(split_data[0]) + int(split_data[1])
    new_file.write(str(sum)+'\n')

    print(' + '.join(split_data), '=', sum)

print('\nHasil penjumlahan dari data diatas disimpan ke: ' + dest_file)
