import math
from functools import reduce
import operator


# --------------------------- Варіант 0 ---------------------------
def variant_0(n: int) -> int:
    n = abs(n)
    while n > 9:
        prod = 1
        m = n
        while m > 0:
            prod *= m % 10
            m //= 10
        n = prod
    return n


# --------------------------- Варіант 1 ---------------------------
def variant_1(n: int) -> int:
    n = abs(n)
    while n > 9:
        n = math.prod(int(ch) for ch in str(n))
    return n


# --------------------------- Варіант 2 (рекурсія) ---------------------------
def mult_to_single_digit(n: int) -> int:
    n = abs(n)
    if n <= 9:
        return n

    prod = 1
    for ch in str(n):
        prod *= int(ch)
    return mult_to_single_digit(prod)


# --------------------------- Варіант 3 ---------------------------
def variant_3(n: int) -> int:
    n = abs(n)
    while n > 9:
        n = reduce(operator.mul, (int(ch) for ch in str(n)), 1)
    return n


# --------------------------- Основна частина ---------------------------
try:
    num = int(input("Введіть число: ").strip())
except ValueError:
    print("❌ Помилка: введено не число!")
else:
    print("Варіант 0:", variant_0(num))
    print("Варіант 1:", variant_1(num))
    print("Варіант 2:", mult_to_single_digit(num))
    print("Варіант 3:", variant_3(num))

