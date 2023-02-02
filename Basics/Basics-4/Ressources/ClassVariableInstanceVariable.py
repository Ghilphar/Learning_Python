class Dog:
    """This example show the differences between Class variable and Instance variable"""
    kind = "canine"          #Class variable shared by all instances

    def __init__(self, name):
        self.name = name    #Instance variable unique to each instance

d = Dog("Mous")
e = Dog("Kiria")

print(d.kind, e.kind)
print(d.name, e.name)


