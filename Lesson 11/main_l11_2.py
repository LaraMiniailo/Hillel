# HW 11.2. Заповнення списку кабами чисел.

def generate_cube_numbers(limit):
# Генератор кубів чисел, починаючи з 2, поки значення куба менше за limit.

    n = 2
    while True:
        cube = n ** 3
        if cube >= limit:
            break
        yield cube
        n += 1

#gen = generate_cube_numbers(1)
#print(gen)

cube_list = list(generate_cube_numbers(10))
print(cube_list)

print('================================================================')

cube_list = list(generate_cube_numbers(100))
print(cube_list)

print('================================================================')

cube_list = list(generate_cube_numbers(1000))
print(cube_list)