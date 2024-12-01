key = "назмиеввад"
vowels = ["а", "я", "у", "ю", "и", "ы", "о", "ё", "э", "е"]


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


def cipher(k1, k2):
    text = [1, 1, 0, 1, 1, 0, 1, 0]

    ip = [2, 6, 3, 1, 4, 8, 5, 7]

    ip_1 = [ip.index(i) + 1 for i in range(1, 9)]

    e_p = [4, 1, 2, 3, 2, 3, 4, 1]

    changed_text = [text[i - 1] for i in ip]

    left_ep = ip[:4]
    right_ep = ip[4:]

    post_ep = [right_ep[i - 1] for i in e_p]

    xor_post_ep = [i ^ j for i, j in zip(post_ep, k1)]

    # return xor_post_ep
    return post_ep

    # lef


print(cipher([1, 1, 0, 1, 0, 1, 1, 0], 0))

# k1, k2 = gen_keys(["1" if i not in vowels else "0" for i in key])
# print(cipher())

# 0111 10-2 : 11-3 11
# print(gen_keys(["1" if i not in vowels else "0" for i in key]))
