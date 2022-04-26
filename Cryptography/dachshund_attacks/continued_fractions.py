'''
    Adapted from https://gist.github.com/mananpal1997/73d07cdc91d58b4eb5c818aaab2d38bd
'''

def rational_to_contfrac(x, y, max_n=1000):
    # Converts a rational x/y fraction into a list of partial quotients [a0, ..., an]
    a = x // y
    pquotients = [a]
    while a * y != x and max_n > 0:
        max_n -= 1
        x, y = y, x - a * y
        a = x // y
        pquotients.append(a)
    return pquotients

def convergents_from_contfrac(frac):
    # computes the list of convergents using the list of partial quotients
    convs = []
    for i in range(len(frac)):
        convs.append(contfrac_to_rational(frac[0 : i]))
    return convs

def contfrac_to_rational(frac):
    # Converts a finite continued fraction [a0, ..., an] to an x/y rational.
    if len(frac) == 0:
        return (0, 1)
    num = frac[-1]
    denom = 1
    for _ in range(-2, -len(frac) - 1, -1):
        num, denom = frac[_] * num + denom, num
    return (num, denom)

def int_sqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x
