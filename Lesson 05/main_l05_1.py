# HW 5.1. Ім'я змінної

import keyword
import string

list_hw51 = ['_', '__', '___', 'x', 'get_value', 'get value', 'get!value', 'some_super_puper_value',
             'Get_value', 'get_Value', 'getValue', '3m', 'm3', 'assert', 'assert_exception']

# Змінна з усіма знаками пунктуації
punctuation_chars = string.punctuation

for name_chars in list_hw51:
    ok = True

    # Перевіряємо на порожній рядок
    if name_chars == "":
        ok = False

    # Перевіряємо name_chars у списку зареєстрованих слов
    if ok:
        for kw in keyword.kwlist:
            if name_chars == kw:
                ok = False
                break

    # Перевіряємо, чи не починається name_chars з цифри
    if ok:
        ch0 = name_chars[0]
        if '0' <= ch0 <= '9':
            ok = False

    # Перевіряємо символи (дозволені: [a-z], [0-9], "_"; без пробілів і великих літер)
    if ok:
        i = 0
        while i < len(name_chars):
            ch = name_chars[i]

            # Перевірка на великі літери
            if 'A' <= ch <= 'Z':
                ok = False
                break

            # Перевірка на пробіл
            if ch == ' ':
                ok = False
                break

            # Перевірка на символи пунктуації (за виключенням "_")
            if ch in punctuation_chars and ch != '_':
                ok = False
                break

            # В Python дозволені лише латинські малі літери, цифри та "_"
            if not (('a' <= ch <= 'z') or ('0' <= ch <= '9') or ch == '_'):
                ok = False
                break

            if ok and set(name_chars) == {'_'} and len(name_chars) >= 2:
                ok = False

            i += 1

    print("'" + name_chars + "'", "->", ok)



