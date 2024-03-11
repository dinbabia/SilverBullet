class Person:

    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

din = Person("Din", 12)
print(f"Newly instantiated object")
print(f"Name: {din.name}")

try:
    print("\nPrinting 'age' of Din")
    print(din.age)
except AttributeError:
    print("'age' is encapsulated, therefore, cannot be accessed directly.")

try:
    print("\nPrinting '__age' of Din")
    print(din.__age)
except AttributeError:
    print("'__age' is encapsulated, therefore, cannot be accessed directly.")

print("\nGettin age using getter")
print(f"Din's age is now {din.get_age()}")

print("Setting age using setter")
din.set_age(16)

print("Gettin age using getter")
print(f"Din's age is now {din.get_age()}")

print("\nAside from Getter and Setter, we can access it via __dict__")
# But we can check the hidden/encapsulated attributes using __dict__
print(din.__dict__)
# You will see '_Person__age' when running din__dict__
print(din._Person__age)
print("Setting age using _Person__age")
din._Person__age = 21
print(f"Din's age is now {din.get_age()}")

