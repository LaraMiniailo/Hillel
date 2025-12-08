# HW 10.3. Перевірити чи є парним чи ні

def sequence_generator(func, start, n):
    current = start
    for _ in range(n):
        yield current
        current = func(current)

# Арифметична прогресія
def next_arithmetic(x):
    return x + 3

for value in sequence_generator(next_arithmetic, start=1, n=5):
    print(value)

print('============================================')

# Геометрична прогресія
def next_geo(x):
    return x * 3

for value in sequence_generator(next_geo, start=1, n=6):
    print(value)

print('============================================')

# Будь-яка інша ситуація
def weird(x):
    return x * x - 1

for value in sequence_generator(weird, start=2, n=4):
    print(value)

# Використати декоратор