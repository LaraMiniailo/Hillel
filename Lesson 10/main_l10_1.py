# HW 10.1. Генераторна функція.

def pow(x):
    return x ** 2

def some_gen(begin, end, func):

# begin: перший елемент послідовності  end: кількість елементів у послідовності func: функція, яка формує значення для послідовності

    curr = begin
    for _ in range(end):
        yield curr
        curr = func(curr)

from inspect import isgenerator

gen = some_gen(2, 4, pow)
assert isgenerator(gen) == True

result = list(some_gen(2, 4, pow))
assert list(gen) == [2, 4, 16, 256]

print(result)