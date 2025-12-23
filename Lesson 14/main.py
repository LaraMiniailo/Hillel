# HW 14.2. Створення власних модулів. Main.

from student import Student
from group import Group

# Тестування
st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')

gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)

print(gr)

# Перевірки пошуку
assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод пошуку повинен повертати екземпляр'

# Перевірка порівняння студентів (тепер працює через __eq__)
assert gr.find_student('Jobs') == st1, 'Порівняння студентів має працювати через __eq__'

# Перевірка видалення
gr.delete_student('Taylor')
print(gr)  # Only one student

# Повторне видалення — без помилки
gr.delete_student('Taylor')

# Додаткова перевірка: робота set з рівністю/хешем
duplicate_st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
gr.add_student(duplicate_st1)  # не додасться дубль через однаковий __str__ і __hash__
print(f'Кількість студентів у групі: {len(gr.group)}')  # все ще 1