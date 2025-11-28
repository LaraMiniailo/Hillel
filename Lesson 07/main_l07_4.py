# HW 7.4. Пошук спільних елементів

def common_elements() -> set:
    # 0..99 — 100 елементів
    multiples_of_3 = [x for x in range(100) if x % 3 == 0]
    multiples_of_5 = [x for x in range(100) if x % 5 == 0]
    return set(multiples_of_3) & set(multiples_of_5)
res = common_elements()


print(res)