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
        self.__age = age

    def say_name(self):
        print(f"My name is {self.name}")

    def happy_birthday(self):
        print(f"I am {self.__age} years old, yesterday.")
        print("But it's my birthday today!")
        self.__age += 1
        print(f"So now, I am {self.__age} years old")

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @age.deleter
    def age(self):
        del self.__age

    @classmethod
    def show_person_base_stats(cls):
        print(cls.is_human)
        print(cls.has_heart)
        print(cls.has_brain)

    @classmethod
    def din_factory(cls):
        # We can also use class methods as a type of factory to create instances of a class
        return cls("Din", 11)

    @staticmethod
    def static_print():
        # Ables to define a static method in the class
        # Cannot access class attributes or per instance attributes
        # does not need to have a class instance!!! can be called by either the class or by an instance of the class!!!
        print("I am always the same")


din = Person("Din", 18)

din.happy_birthday()

try:
    print(din.__age)
except AttributeError:
    print("\ndin__age is not accessible")
    print("Use din.age instead.")

print(din.age)

din.age = 23

print(din.age)

din.show_person_base_stats()

din1 = Person.din_factory()
din2 = Person.din_factory()
din3 = Person.din_factory()

print(din1.name)
print(din2.name)
print(din3.name)

Person.static_print()
din.static_print()
