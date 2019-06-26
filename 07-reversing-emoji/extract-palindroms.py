# primes list downloaded from https://primes.utm.edu/lists/small/millions/

def is_palindrome(str):
    return str == str[::-1]

filenames = ['primes1.txt', 'primes2.txt', 'primes3.txt', 'primes4.txt', 'primes5.txt', 'primes6.txt']

palindromes = []
for filename in filenames:
    with open(filename, 'r') as f:
        primes = ['']
        primes.extend(f.read().split())

        p = [int(n) for n in map(str.strip, filter(is_palindrome, filter(None, primes)))]
        palindromes.extend(p)

        print("found {} palindromes".format(len(p)))

with open('palindromes', 'w') as f:
    f.write(','.join(map(str, palindromes)))
