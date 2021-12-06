try:
    input_file = input('Masukkan nama file yang ingin di enkripsi: ')
    #input_file = 'file/teks.dat'
    file = open(input_file, 'r')
    enc_file = open('file/encrypted.dat', 'w')

    input_code = int(input('Masukkan angka referensi: '))
    print('Tolong simpan angka referensi anda!!')

    while True:
        read_file = file.readline()

        split_data = read_file.split(' ')
        last_element = len(split_data) - 1
        split_data[last_element] = split_data[last_element].replace('\n', '')

        list_new_data = list()

        for data in split_data:
            temp_char = list()
            for char in data:
                ascii_code = ord(char)
                if char.isupper() == True:
                    if ascii_code + input_code > ord('Z'):
                        ascii_code = input_code - (ord('Z') - ord(char))
                        ascii_code += ord('A') - 1
                    else:
                        ascii_code += input_code

                elif char.islower() == True:
                    if ascii_code + input_code > ord('z'):
                        ascii_code = input_code - (ord('z') - ord(char))
                        ascii_code += ord('a') - 1
                    else:
                        ascii_code += input_code
                temp_char.append(chr(ascii_code))
            list_new_data.append(''.join(temp_char))

        enc_file.write(' '. join(list_new_data)+'\n')
        #print(' '. join(list_new_data)+'\n')

        if not read_file:
            file.close()
            enc_file.close()
            print("File disimpan dengan nama 'encrypted.dat'")
            break

except FileNotFoundError:
    print('FILE TIDAK DITEMUKAN!!')

except ValueError:
    print('INPUT TIDAK VALID!!!')
