class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def display(self):
        print("Имя:", self.firstname, self.lastname)
        print("Возраст:", self.age)


class Student(Person):
    current_student_id = 1  # Статическое поле для отслеживания текущего studentID

    def __init__(self, firstname, lastname, age, recordBook):
        super().__init__(firstname, lastname, age)
        self.studentID = Student.current_student_id
        self.recordBook = recordBook
        Student.current_student_id += 1  # Увеличиваем studentID для следующего студента

    def display(self):
        super().display()
        print("Student ID:", self.studentID)
        print("Record Book:")
        for grade, count in self.recordBook.items():
            print(f"{grade}: {count}")


# Создание трех объектов класса Student
student1 = Student("Ivan", "Golom", 20, {"Кол-во пятёрок": 2, "Кол-во четвёрок": 1, "Кол-во троек": 5})
student2 = Student("Oleg", "Ivanov", 21, {"Кол-во пятёрок": 3, "Кол-во четвёрок": 4, "Кол-во троек": 3})
student3 = Student("Danil", "Gromov", 20, {"Кол-во пятёрок": 3, "Кол-во четвёрок": 2, "Кол-во троек": 4})

# Вывод информации о студентах
print("Student 1:")
student1.display()
print("\nStudent 2:")
student2.display()
print("\nStudent 3:")
student3.display()