class Person:
    head = None

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.next = None
        self.add_to_list()

    def __del__(self):
        if self.head == self:
            self.head = self.next
        else:
            p = self.head
            while p is not None and p.next != self:
                p = p.next
            if p is not None:
                p.next = self.next

    def show(self):
        print(f"Имя: {self.name}, Возраст: {self.age}")

    def add_to_list(self):
        if self.head is None:
            self.head = self
        else:
            p = self.head
            while p.next is not None:
                p = p.next
            p.next = self

    @staticmethod
    def print_list():
        p = Person.head
        print("---------------------------------")
        while p is not None:
            p.show()
            p = p.next
            print()
        print("---------------------------------")

class Student(Person):
    def __init__(self, name, age, student_id, major):
        super().__init__(name, age)
        self.student_id = student_id
        self.major = major
        self.add_to_list()

    def show(self):
        super().show()
        print(f"Я студент с номером: {self.student_id}, и учусь на специальности: {self.major}")

class Teacher(Person):
    def __init__(self, name, age, department):
        super().__init__(name, age)
        self.department = department
        self.add_to_list()

    def show(self):
        super().show()
        print(f"Я преподаю на кафедре: {self.department}")

class DepartmentHead(Teacher):
    def __init__(self, name, age, department, office):
        super().__init__(name, age, department)
        self.office = office
        self.add_to_list()

    def show(self):
        super().show()
        print(f"Я заведующий кафедрой {self.department} и мой кабинет находится в {self.office}.")

# Пример использования
p1 = Person("Петр", 16)
s1 = Student("Иван", 20, 12345, "Информатика")
t1 = Teacher("Мария", 35, "Математика")
d1 = DepartmentHead("Алла", 40, "Программирование", "Аудитория 202")
d11 = DepartmentHead("Анна", 50, "Физика", "Аудитория 101")

Person.print_list()

del p1
del d11

Person.print_list()

del s1
del d1
del t1

Person.print_list()

s3 = Student("Иван", 20, 12345, "Информатика")
t3 = Teacher("Мария", 35, "Математика")
d3 = DepartmentHead("Анна", 50, "Физика", "Аудитория 101")

Person.print_list()

del s3
del t3
del d3

Person.print_list()

p = Person("Петр", 16)
s = Student("Иван", 20, 12345, "Информатика")
t = Teacher("Мария", 35, "Математика")
d = DepartmentHead("Анна", 50, "Физика", "Аудитория 101")

Person.print_list()
