while True:
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
            continue
        result = a / b
    else:
        print("Введіть одну з операцій: +, -, *, /")
        continue
    print(f"(Результат:) {a} {op} {b} = {result}")

    cnt = input("Бажаєте продовжити? (y/yes для продовження, все інше - завершення):").strip().lower()

    if cnt not in ("y", "yes"):
        print(" Роботу завершено.")
        break