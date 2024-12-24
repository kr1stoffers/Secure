from sympy import mod_inverse


def gen_key():
    p = 100000000019
    q = 2295222731

    n = p * q
    phi_n = (p - 1) * (q - 1)

    # print(n)
    e = 65537
    d = mod_inverse(e, phi_n)
    return ((e, n), (d, n))


def crypt(p, m):
    e, n = p
    return pow(m, e, n)


def decrypt(s, c):
    d, n = s
    return pow(c, d, n)


p, s = gen_key()

text = "нвда"

t = int.from_bytes(text.encode("utf-8"))

enc = crypt(p, t)
dec = decrypt(s, enc)


print(enc)
print(dec.to_bytes((dec.bit_length() + 7) // 8).decode("utf-8"))
