def longer_substring(entrada):
    d = ""
    f = ""
    for i in range(len(entrada)):
        if entrada[i] not in f:
            f += entrada[i]
        else:
            if len(d) < len(f):
                d = f
            f = f[f.index(entrada[i]) + 1::] + entrada[i]

    return max(len(d), len(f)), d


entrada = "abcabcbb"
print("La respuesta es", longer_substring(entrada))
