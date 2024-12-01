def gen_keys(key):
    p10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
    p8 = [6, 3, 7, 4, 8, 5, 10, 9]

    changed_key = [key[i - 1] for i in p10]
    left = changed_key[:5]
    right = changed_key[5:]

    left = left[1:] + left[:1]
    right = right[1:] + right[:1]

    k1 = [(left + right)[i - 1] for i in p8]

    left = left[2:] + left[:2]
    right = right[2:] + right[:2]

    k2 = [(left + right)[i - 1] for i in p8]

    return k1, k2


def bits_to_decimal_array(bits):
    bits = list(map(str, bits))
    return [int(bits[0] + bits[3], 2), int(bits[1] + bits[2], 2)]


def to_bin(dec):
    res = []
    if dec == 0:
        return [0, 0]
    while dec != 0:
        res.insert(0, dec % 2)
        dec //= 2
    if len(res) % 2 != 0:
        res.insert(0, 0)
    return res


def i_permuted(char_bits, ip):
    return [char_bits[i - 1] for i in ip]


def fk(bits_of_char, key):
    e_p = [4, 1, 2, 3, 2, 3, 4, 1]

    left_ip = bits_of_char[:4]
    right_ip = bits_of_char[4:]

    post_ep = [right_ip[i - 1] for i in e_p]

    xor_post_ep = [i ^ j for i, j in zip(post_ep, key)]

    s0 = [[1, 0, 3, 2], [3, 2, 1, 0], [0, 2, 1, 3], [3, 1, 3, 1]]
    s1 = [[1, 1, 2, 3], [2, 0, 1, 3], [3, 0, 1, 0], [2, 1, 0, 3]]

    left_xor = xor_post_ep[:4]
    right_xor = xor_post_ep[4:]

    row, col = bits_to_decimal_array(left_xor)
    s0_bits = to_bin(s0[row][col])

    row, col = bits_to_decimal_array(right_xor)
    s1_bits = to_bin(s1[row][col])

    p4 = [2, 4, 3, 1]

    post_p4 = [(s0_bits + s1_bits)[i - 1] for i in p4]

    return [i ^ j for i, j in zip(left_ip, post_p4)] + right_ip


def key_char_to_bits(char_array):
    bits = []
    for i in char_array:
        if i in vowels:
            bits.append(0)
        else:
            bits.append(1)
    return bits


def cipher(text, key, flag=True):
    enc = []
    for i in text:
        k1, k2 = gen_keys(key_char_to_bits(key))
        ip = [2, 6, 3, 1, 4, 8, 5, 7]
        ip_1 = [ip.index(i) + 1 for i in range(1, 9)]

        char = bin(ord(i) - 912)[2:]
        char = (8 - len(char)) * "0" + char
        if flag == False:
            k1, k2 = k2, k1

        encrypted = fk(i_permuted([int(i) for i in char], ip), k1)
        encrypted = encrypted[4:] + encrypted[:4]
        encrypted = fk(encrypted, k2)
        enc.append(int("".join(map(str, i_permuted(encrypted, ip_1))), 2))
    return " ".join(map(str, enc))


key = "назмиевади"
text = "назми"

vowels = ["а", "я", "у", "ю", "и", "ы", "о", "ё", "э", "е"]


def decimal_to_bin_str(dec_array):
    arr = []
    dec_array = list(map(int, dec_array.split(" ")))
    for i in dec_array:
        j = chr(i + 912)
        arr.append(j)
    return "".join(map(str, arr))


def decrypt(crypt):
    dec = cipher(decimal_to_bin_str(crypt), key, False)
    dec = dec.split(" ")
    return list(map(lambda x: chr(int(x) + 912), dec))


enc = cipher(text, key)
print(enc)


print(decrypt(enc))
