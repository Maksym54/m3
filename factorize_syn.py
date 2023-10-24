def factorize(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors


a, b, c, d = factorize(128), factorize(255), factorize(99999), factorize(10651060)
print(a)
print(b)
print(c)
print(d)    