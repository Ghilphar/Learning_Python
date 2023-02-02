class Pet:
    def speak(self):
        return "Pet makes sound"

class Dog(Pet):
    def speak(self):
        return "Wouf Wouf"

class Cat(Pet):
    def speak(self):
        return "Meawwww"

pet = Pet()
cat = Cat()
dog = Dog()

print(pet.speak())
print(dog.speak())
print(cat.speak())
