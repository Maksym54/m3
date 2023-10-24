import concurrent.futures
import multiprocessing


def factorize(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

def parallel_factorize(numbers):
    with concurrent.futures.ProcessPoolExecutor(max_workers=multiprocessing.cpu_count()) as executor:
        results = list(executor.map(factorize, numbers))
    return results


numbers = [128, 255, 99999, 10651060]
results = parallel_factorize(numbers)
a, b, c, d = results
print(a)
print(b)
print(c)
print(d)