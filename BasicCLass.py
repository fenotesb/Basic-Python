class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("Person")
        print(" name: " +self.name+" age: "+str(self.age))
    def identify(self):
        print("My name is ",self.name)
    def eat(self):
        print("Mmm. Tastes good.")
class Child(Person):
    def __init__(self, name, age, hobby, grade):
        Person.__init__(self, name, age)
        self.hobby=hobby
        self.grade=grade
    def display(self):
        print("Child")
        Person.display(self)
        print("I love to " +self.hobby+".")
        print("I am in grade "+str(self.grade)+".")
    def identify(self):
        print("I'm a kid named ",self.name)
    def happy(self):
        print("I'm a happy kid!")


def main():
    him = Person ("Sven",45)
    him.display()
    girl = Child("Tina", 13, "play soccer", 7)
    girl.display()
    him.identify()
    girl.identify()

    him.eat()
    girl.eat()
    girl.happy()
    
    
main()


