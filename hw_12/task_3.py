def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def count_primes_in_list(lst):
    primes = list(filter(is_prime, lst))
    return len(primes)


print("Count of prime numbers in the list:", count_primes_in_list([2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))
