import itertools
from Crypto.Util.number import inverse

with open('msg.txt') as f:
    lines = f.readlines()
    n = int(lines[1])
    e = int(lines[4])
    msg = int(lines[7], 16)

# https://stackoverflow.com/a/15391420
def sqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x


def find(target):
    for p in filter(lambda x: x%2 == 1, range(target - 100, target + 100)):
        if n % p == 0:
            q = n // p
            print("P: {}, Q: {}".format(p, q))
            return p, q
    return 0, 0

def get_primes(n):
    for a, b in itertools.combinations(range(1, 1001), 2):
        s = sqrt(n * a // b)
        p, q = find(s)
        if p != 0:
            print("Found with a: {}, b: {}".format(a, b))
            return p, q
    return 0, 0

def decode(msg, n, d):
    return pow(msg, d, n)


P, Q = get_primes(n)
if P == 0:
    print("Did not find primes")
    exit()

totient = (P - 1) * (Q - 1)
d = inverse(e, totient)
decrypted = decode(msg, n, d)
print(str(bytes.fromhex("{:x}".format(decrypted)),'utf-8'))