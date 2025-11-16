# HW 4.2. Знайти суму елементів із парними індексами
lst = [1, 3, 5]
even_sum = sum(lst[j] for j in range(0, len(lst), 2))
result = even_sum * lst[-1]
print(result)

lst = [6]
even_sum = sum(lst[j] for j in range(0, len(lst), 2))
result = even_sum * lst[-1]
print(result)

lst = []
if lst:
    even_sum = sum(lst[j] for j in range(0, len(lst), 2))
    result = even_sum * lst[-1]
    print(result)
else:
    print("Список порожній - обчислити результат неможливо!!!!!!!")
