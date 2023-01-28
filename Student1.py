class Student:
    def __init__(self, name='Ivan', age=18, group_number='10A'):
        self. name = name
        self. age = age
        self.groupNumber = group_number

    def get_name(self):
        return f'Имя студента - {self.name}'

    def get_age(self):
        return f'возраст студента - {self.age}'

    def get_group_number(self):
        return f'группа студента - {self.groupNumber}.'

    def set_name_age(self, name, age):
        self. name = name
        self. age = age
        return f'Имя студента - {self.name}, возраст студента - {self.age}'

    def set_group_number(self, group_number):
        self.groupNumber = group_number
        return f'группа студента - {self.groupNumber}.'


Nikita = Student("Никита", 18, "03b")
Dasha = Student("Даша", 21, "3k")
Ivan = Student("Иван", 18, "10А")
Michail = Student()
Yna = Student("Яна", 16, "11AA")
print(f'{Nikita.get_name()}, {Nikita.get_age()}, {Nikita.get_group_number()}')
print(f'{Dasha.get_name()}, {Dasha.get_age()}, {Dasha.get_group_number()}')
print(f'Имя студента - {Ivan.name}, возраст студента - {Ivan.age}, группа студента - {Ivan.groupNumber}.')
print(f'{Michail.set_name_age("Георгий", 30)}, {Michail.set_group_number("0303SDE")}')
print(f'{Yna.get_name()}, {Yna.get_age()}, {Yna.get_group_number()}')