# Найпростіший калькулятор

a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))
op = input("Оберіть дію (+, -, *, /): ").strip()

if op == '+':
    result = a + b
elif op == '-':
    result = a - b
elif op == '*':
    result = a * b
elif op == '/':
    if b == 0:
        print("Помилка: ділення на нуль неможливе!")
        exit()
    result = a / b
else:
    print("Невідома дія. Введіть одну з: +, -, *, /")
    exit()

print(f"Результат: {a} {op} {b} = {result}")