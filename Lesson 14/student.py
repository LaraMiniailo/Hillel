# HW 14.2. Створення власних модулів. Student.

from human import Human

class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return (f'Student: {self.first_name} {self.last_name}, {self.gender}, '
                f'{self.age} years old, Record book: {self.record_book}')

    # Порівняння за рядком, що повертає __str__
    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return str(self) == str(other)

    # Узгоджений з __eq__ хеш, щоб екземпляри були хешовані (для set, dict)
    def __hash__(self):
        return hash(str(self))
