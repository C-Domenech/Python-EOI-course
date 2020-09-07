# Run-Length Decoding
def run_length_dec(c_list):
    letter = 0
    num = 1
    if c_list:
        new_list.extend(c_list[letter] * c_list[num])
        del c_list[letter:num + 1]
        run_length_dec(c_list)
        return new_list
    else:
        return 'La lista introducida está vacía.'


if __name__ == '__main__':
    new_list = []
    cod_list = ['A', 12, 'B', 4, 'A', 6, 'B', 1]
    print("Original:", cod_list)

    dec_list = run_length_dec(cod_list)
    print("Decodificada:", dec_list)
