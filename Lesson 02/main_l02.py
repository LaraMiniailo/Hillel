# 1
print("Завдання №1")
x = float(input("Введіть число:"))
print(x**2)
print("=========================================")

# 2
print("Завдання №2")
a = float(input("Перше число: "))
b = float(input("Друге число: "))
c = float(input("Третє число: "))
print("Середнє:", (a + b + c) / 3)
print("=========================================")

# 3
print("Завдання №3")
minutes = int(input("Кількість хвилин: "))
hours = minutes // 60
mins = minutes % 60
print(f"{hours} годин {mins} хвилин")
print("=========================================")

# 4
print("Завдання №4")
price = float(input("Введіть ціну: "))
discount = float(input("Введіть % знижки: "))
final_price = price * (1 - discount / 100)
print(final_price)
print("=========================================")

# 5
print("Завдання №5")
n = int(input("Введіть ціле число: "))
print(abs(n) % 10)
print("=========================================")

# 6
print("Завдання №6")
length = float(input("Довжина: "))
width = float(input("Ширина: "))
perimeter = 2 * (length + width)
print(f"{perimeter:.2f}")
print("=========================================")

# 7
print("Завдання №7")
n = abs(int(input("Введіть ціле 4-х значне число:")))
a, r = divmod(n, 1000)
b, r = divmod(r, 100)
c, d = divmod(r, 10)
print(a)
print(b)
print(c)
print(d)
print("=========================================")