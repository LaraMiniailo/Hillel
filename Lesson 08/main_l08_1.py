# HW 8.1. Додати 1 до числа.
def add_one(digits):
# Функція add_one: Приймає список цифр (0–9), що утворюють число зліва направо.  Повертає новий список цифр після додавання 1.

# Перевіряємо рядок на наявність даних. Якщо це пустий список, то функція оверне 1.
    if not digits:
        return [1]

# Побудувати число зі списку цифр
    num = int(''.join(str(d) for d in digits))

# Тепер додаэм 1 до числа
    num += 1

# Розбиваємо отримане число  на цифри
    return [int(ch) for ch in str(num)]

digits = list(map(int, input('Введіть цифри через пробіл: ').split()))

result = add_one(digits)

print(result)