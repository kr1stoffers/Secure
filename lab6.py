def find_prime_factors(n):
    factors = set()
    for i in range(2, int(n**0.5) + 1):
        while n % i == 0:
            factors.add(i)
            n //= i
    if n > 1:
        factors.add(n)
    return factors


def is_primitive_root(g, p):
    p_minus_1 = p - 1
    prime_factors = find_prime_factors(p_minus_1)

    for factor in prime_factors:
        if pow(g, p_minus_1 // factor, p) == 1:
            return False
    return True


def find_primitive_root(p):
    for g in range(2, p):
        if is_primitive_root(g, p):
            return g
    return None


q = 5639

p_root = find_primitive_root(q)

xa = 3994
xb = 2452

ya = pow(p_root, xa, q)
yb = pow(p_root, xb, q)

ka = pow(yb, xa, q)
kb = pow(ya, xb, q)

print(str(ya) + " " + str(yb))
print(str(ka) + " " + str(kb))
