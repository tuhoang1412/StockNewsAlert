from math import sqrt, floor


def normal_sieve(limit, primes):
    temp_mark = [False] * (limit + 1)

    for i in range(2, limit + 1):
        if not temp_mark[i]:

            primes.append(i)

            for j in range(i, limit + 1, i):
                temp_mark[j] = True


def segmented_sieve(low, high):
    primes = list()
    normal_sieve(limit=floor(sqrt(high)), primes=primes)
    n = high - low + 1

    mark = [True] * (n + 1)
    for i in range(len(primes)):
        smallest_mul = floor(low / primes[i]) * primes[i]

        if smallest_mul < low:
            smallest_mul += primes[i]

        for j in range(smallest_mul, high + 1, primes[i]):
            mark[j - low] = False

    for i in range(low, high + 1):
        if mark[i - low] == True:
            print(i, end=" ")


low = 49
high = 1000
segmented_sieve(low, high)
