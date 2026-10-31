class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Dog(Animal):
    def bark(self):
        print(self.name, "says Woof!")


class Cat(Animal):
    def meow(self):
        print(self.name, "says Meow!")


dog = Dog("Rex", 3)
cat = Cat("Murchyk", 2)

print("DOG:")
dog.info()
dog.bark()

print("CAT:")
cat.info()
cat.meow()