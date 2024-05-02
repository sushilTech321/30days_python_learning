# python -> inheritance 

class Person :
    def __init__(self, name, rollno, age):
        self.name = name
        self.rollno = rollno
        self.age = age

    def printname(self):
        print(self.name, self.rollno, self.age)

class Student(Person):
    def __init__(self, name, rollno, age):
        super().__init__(self, name, rollno, age)   

s = Person("mike",1,20)
s.printname()        
