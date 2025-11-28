# HW 6.3. Добуток чисел.

import math
from functools import reduce
import operator

# Варіант 0 (Рішення з використанням лише арифметики)
n = int(input('Введіть число (Варіант 0): ').strip())
n = abs(n)  # Працюємо з модулем, якщо введено від'ємне

while n > 9:
    prod = 1
    m = n
    while m > 0:
        prod *= m % 10
        m //= 10
    n = prod

print("Результат: ",n)

# Варіант 1 (Через рядок і math.prod)
import math

n = abs(int(input('Введіть число (Варіант 1): ').strip()))

while n > 9:
    n = math.prod(int(ch) for ch in str(n))

print(n)

# Варіант 2 (Рекурсивний)
def mult_to_single_digit(n: int) -> int:
    n = abs(n)
    if n <= 9:
        return n
    prod = 1
    for ch in str(n):
        prod *= int(ch)
    return mult_to_single_digit(prod)

print(mult_to_single_digit(int(input('Введіть число (Варіант 2): ').strip())))

# Варіант 3 (reduce + operator.mul)
from functools import reduce
import operator

n = abs(int(input('Введіть число (Варіант 3): ').strip()))

while n > 9:
    n = reduce(operator.mul, (int(ch) for ch in str(n)), 1)

print(n)

