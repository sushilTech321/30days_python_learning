# Python Classes and Objects


# The __init__() Function
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("john",30)
# print(p1.name) 
# print(p1.age)


class Car:
    def __init__(self, name, brand, model, color):
        self.name = name
        self.brand = brand
        self.model = model
        self.color = color

c1 = Car("Corolla","Toyota","2020","blue")
# print(c1.name)
# print(c1.brand)
# print(c1.model)
# print(c1.color)


# The __str__() Function
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name}({self.age})"
    
p1 = Person("john",30)
# print(p1)


class Car:
    def __init__(self, name, brand, model, color) :
        self.name = name
        self.brand = brand
        self.model = model
        self.color = color

    def __str__(self) :
        return f" {self.name} {self.brand} {self.model} {self.color}"
    
c1 = Car("Corolla","Toyota", 2020,"blue")
# print(c1)


# Object Methods
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def print_info(self):
        print("hello my name is:"+ self.name)
    
p1 = Person("john",30)
# p1.print_info()


# Practice
class Teacher :
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course
t1 = Teacher("Dev",32,"science")
# print(t1.name)
# print(t1.age)
# print(t1.course)

class Teacher :
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def __str__(self):
        return f"{self.name} {self.age} {self.course}"

t1 = Teacher("Dev",32,"science")
# print(t1)

class Teacher :
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def show(self):
        print("Teacher's name:", self.name +"\n"+ "Teachear's age:",str(self.age) + "\n" + "Course:",self.course)

t1 = Teacher("Dev",32,"Maths")
t1.show()


