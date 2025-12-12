# HW 11.1. Генератор простих чисел

def prime_generator(limit):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    for num in range(2, limit + 1):
        if is_prime(num):
            yield num

print(list(prime_generator(10)))
print(list(prime_generator(15)))
print(list(prime_generator(29)))