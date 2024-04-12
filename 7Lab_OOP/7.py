class Worker:
    'doc class Worker'
    count = 0

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        Worker.count += 1

    def display(self):
        print("Worker:")
        print("{} {}".format(self.name, self.surname))

class Animal:
    id = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Animal.id += 1
    def display(self):
        print("Animal id: {}".format(Animal.id))
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))

w1 = Worker("Ivan", "Golom")
print("w1.count:", w1.count)
w2 = Worker("Oleg", "Ivanov")
print("w2.count:", w2.count)
print("w1.count:", w1.count)
print("Worker.count:", Worker.count, "\n")

a1 = Animal("Bob", 3)
a2 = Animal("Rax", 2)
a3 = Animal("Star", 3)

a1.display()
a2.display()
a3.display()