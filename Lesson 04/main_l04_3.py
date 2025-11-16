# Список випадкових чисел

import random
base_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = random.randint(5, 10)
lst = [random.choice(base_lst) for _ in range(n)]
print(lst)

# Створення іншого списку

base_lst = [1, 2, 3, 4, 5, 6, 7, 9]
new_lst = [base_lst[0], base_lst[2], base_lst[-2]]
print(new_lst)

base_lst = [1, 1, 2, 1]
new_lst = [base_lst[0], base_lst[2], base_lst[-2]]
print(new_lst)

base_lst = [6, 3, 7]
new_lst = [base_lst[0], base_lst[2], base_lst[-2]]
print(new_lst)

import random

# Крок 1: Створення списку випадкових чисел
length = random.randint(3, 10)
numbers = [random.randint(1, 100) for _ in range(length)]
print("Список випадкових чисел:", numbers)

# Крок 2: Створення нового списку з першого, третього і другого з кінця елементів
new_list = [numbers[0], numbers[2], numbers[-2]]
print("Новий список:", new_list)