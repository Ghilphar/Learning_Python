class Person:
    def __init__(self, firstName, name):
        self.firstName = firstName
        self.name = name
        self.fullName = firstName + " " + name
    def introduce(self):
        return "Hello I am {}.\n".format(self.fullName)

class Student(Person):
    def __init__(self, firstName, name, major):
        super().__init__(firstName, name)
        self.major = major
    def introduce(self):
        return super().introduce() + "My major is {}.".format(self.major)

computerScienceStudent = Student("Felipe", "Garibotti", "Computer Science")

print(computerScienceStudent.introduce())
