# Run-Length Encoding
def run_length_enc(d_list):
    pos = 1
    if d_list:
        while pos < len(d_list) and d_list[0] == d_list[pos]:
            pos += 1
        new_list.append(d_list[0])
        new_list.append(pos)
        run_length_enc(d_list[pos:])
        return new_list
    else:
        return 'La lista introducida está vacía.'


if __name__ == '__main__':
    new_list = []
    dec_list = ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'A', 'A',
                'A', 'B']
    print("Original:", dec_list)

    cod_list = run_length_enc(dec_list)
    print("Codificada:", cod_list)
