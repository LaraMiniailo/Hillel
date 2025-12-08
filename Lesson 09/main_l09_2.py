# HW 9.2. Різниця між числами

def difference(*args):
    if not args:
        return 0

    diff = max(args)- min(args)

    return diff

print(difference(1, 2, 3))
print(difference(5.5, 1.1, 9.0))
print(difference())
print(difference(-10, 10))