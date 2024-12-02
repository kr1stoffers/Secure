import math
from sympy import isprime, mod_inverse


# var 10
def gen_key():
    p = 53319
    q = 50283

    n = p * q
    phi_n = (p - 1) * (q - 1)
    e = 46805

    d = mod_inverse(e, phi_n)
    return ((e, n), (d, n))


def encrypt(p_key, text):
    e, n = p_key
    m = text

    c = pow(m, e, n)
    return c


def decrypt(s_key, text):
    d, n = s_key
    m = pow(text, d, n)
