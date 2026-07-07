
class Student:
    def __init__(self, name, age):
        self.name1 = name    # instance variable
        self.age1 = age

    def display(self):
        print("Name:", self.name1)
        print("Age:", self.age1)

# Create object
s1 = Student("Rahul", 21)

# Call method
s1.display()