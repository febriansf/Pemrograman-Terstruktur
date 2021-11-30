try:
    #input_file = input('Masukkan file yang ingin di dekripsi: ')
    input_file = 'file/encrypted.dat'
    enc_file = open(input_file, 'r')
    dec_file = open('file/decrypted.dat', 'w')

    #angka sebagai referensi geseran huruf
    input_code = int(input('Masukkan angka referensi: '))

    while True:
        read_file = enc_file.readline()

        split_data = read_file.split(' ')
        last_element = len(split_data) - 1
        split_data[last_element] = split_data[last_element].replace('\n', '')

        list_new_data = list()

        for data in split_data:
            temp_char = list()
            for char in data:
                ascii_code = ord(char)
                if char.isupper() == True:
                    if ascii_code - input_code < ord('A'):
                        ascii_code = input_code - (ord(char) - ord('A'))
                        ascii_code = ord('Z') - ascii_code + 1
                    else:
                        ascii_code -= input_code
                elif char.islower() == True:
                    if ascii_code - input_code < ord('a'):
                        ascii_code = input_code - (ord(char) - ord('a'))
                        ascii_code = ord('z') - ascii_code + 1
                    else:
                        ascii_code -= input_code

                temp_char.append(chr(ascii_code))

            list_new_data.append(''.join(temp_char))

        dec_file.write(' '. join(list_new_data)+'\n')
        #print(' '. join(list_new_data)+'\n')

        if not read_file:
            enc_file.close()
            dec_file.close()
            break

except FileNotFoundError:
    print('FILE TIDAK DITEMUKAN!!')

except ValueError:
    print('INPUT TIDAK VALID!!!')
