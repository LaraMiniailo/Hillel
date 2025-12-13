# HW 11.3. Перевірка на парність.
# Варыант 1.
def is_even(n):
    return (n & 1) == 0

print('Варыант 1.')
print(is_even(2494563894038**2))
print(is_even(1056897**2))
print(is_even(24945638940387**3))
print('====================================================')

def is_even(n: int) -> bool:
    return not (n & 1)
print('Варыант 2.')
print(is_even(2494563894038**2))
print(is_even(1056897**2))
print(is_even(24945638940387**3))
print('====================================================')

def is_even(n: int) -> bool:
    return not bool(n & 1)
print('Варыант 3.')
print(is_even(2494563894038**2))
print(is_even(1056897**2))
print(is_even(24945638940387**3))