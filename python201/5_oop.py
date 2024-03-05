class Person:
    '''
    Class description

     init_attrs
    ----------
    name (str) : The name of the person
    age (int) : The age of the person

     class_attrs
    ----------
    is_human (bool) : A person is a human.
    has_heart (bool) : A person should have a functional heart? Right? Ironman?
    has_brain (bool) : Zombies eat your brains!!! -Plants vs Zombies
    '''
    # class attributes
    is_human = True
    has_heart = True
    has_brain = True
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_name(self):
        print(f"My name is {self.name}")

    def happy_birthday(self):
        print(f"I am {self.age} years old, yesterday.")
        print("But it's my birthday today!")
        self.age += 1
        print(f"So now, I am {self.age} years old")

bob = Person("bob", 30)
din = Person("din", 16)
gon = Person("gon", 16)

print(bob)
print(din)
print(gon)

print(din.name)
print(din.age)

print(hasattr(bob, "age"))
print(hasattr(bob, "qwe"))

print(getattr(bob, "name"))

setattr(bob, "asd", 100)

print(getattr(bob, "asd"))

gon.say_name()
gon.happy_birthday()

print("Are Bob and Din, a person?")
print(bob.is_human)
print(bob.has_heart)
print(din.is_human)
print(din.has_heart)

Person.is_human = False

print("Are Bob and Din, a person?")
print(bob.is_human)
print(bob.has_heart)
print(din.is_human)
print(din.has_heart)

din.has_heart = "YES"
print("Are Bob and Din, a person?")
print(bob.is_human)
print(bob.has_heart)
print(din.is_human)
print(din.has_heart)

# NOTE: Even if we delete the class 'Person', we can still access all the instantiated objects!

print(Person.__dict__)
print(Person.__doc__)
print(Person.__name__)
