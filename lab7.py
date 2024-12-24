from sympy import mod_inverse
import random


def find_g(a, b, p):
    x = 0
    while True:
        mod_y = pow(x, 3) + (a * x) + b
        if pow(mod_y, (p - 1) // 2, p) == 1:
            for y in range(0, p - 1):
                if (y**2) % p == mod_y:
                    return (x, y)
        x += 1


def multi_g(G, a, p, n=2):
    Q = G
    for _ in range(0, n - 1):
        Q = add_points(G, Q, a, p)
    return Q


def add_points(G, Q, a, p):
    if G != None and Q == None:
        return G
    if G == None and Q != None:
        return Q
    if G == None and Q == None:
        return None

    x1, y1 = G
    x2, y2 = Q
    try:
        if G == Q:
            lambd = ((3 * (x1**2) + a) % p) * mod_inverse(2 * y1, p)
        else:
            lambd = ((y2 - y1) % p) * mod_inverse(x2 - x1, p)
        x3 = (lambd**2 - x1 - x2) % p
        y3 = (lambd * (x1 - x3) - y1) % p
        return (x3, y3)
    except:
        return None


def find_O(G, a, p):
    n = 1
    res = multi_g(G, a, p)
    while res != None:
        res = multi_g(G, a, p, n)
        # print(n)
        n += 1
    return n


def neg_point(Q, p):
    x, y = Q
    return (x, (-y) % p)


p = 2141
a = 104
b = 727

k = random.randint(0, p - 1)

pm = (513, 167)

print("Message: " + str(pm))

g = find_g(a, b, p)
print("G: " + str(g))

n = find_O(g, a, p) - 1
print("n: " + str(n))


na = random.randint(102, n)
nb = random.randint(102, n)

pa = multi_g(g, a, p, na)
pb = multi_g(g, a, p, nb)

print("Pa: " + str(pa))
print("Pb: " + str(pb))

cm = (multi_g(g, a, p, k), add_points(pm, multi_g(pb, a, p, k), a, p))

print("Encode: " + str(cm))

first, second = cm

dec = add_points(second, neg_point(multi_g(first, a, p, nb), p), a, p)

print("Decode: " + str(dec))
