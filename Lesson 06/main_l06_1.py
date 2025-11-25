# HW 6.1. Диапазон букв

import string

example_hw61 = ["a-c", "a-a", "s-H", "a-A", "t-g"]
alphabet = string.ascii_letters

for k in example_hw61:

    # 1) має бути рівно один дефіс
    if k.count('-') != 1:
        print(f"{k} -> некоректно: має бути один дефіс")
        continue

    left, right = k.split('-')

    # 2) зліва/справа рівно по одному символу
    if len(left) != 1 or len(right) != 1:
        print(f"{k} -> некоректно: з кожного боку має бути рівно 1 символ")
        continue

    # 3) обидва символи — ASCII-літери
    if left not in alphabet or right not in alphabet:
        print(f"{k} -> некоректно: дозволені лише ASCII-літери")
        continue

    # 4) порядок у string.ascii_letters (a..z потім A..Z)
    i = alphabet.index(left)
    j = alphabet.index(right)

    if i > j:
        print(f"{k} -> некоректно: '{left}' іде пізніше за '{right}' в ascii_letters")
        continue

    # 5) все добре — друкуємо діапазон
    print(f"{k} -> {alphabet[i:j + 1]}")

