# Define a class Student()
class Student():

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def changeID(self, id):
        self.id = id

    def print(self):
        print("{} - {}".format(self.name, self.id))

# Create a Student() object called "jane"
jane = Student("Jane", 10)

# Call methods on object "jane"
jane.print()
jane.changeID(11)
jane.print()
