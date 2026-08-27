class Student:
    def __init__(self, name, marks):
        self.__name = name      # private attribute
        self.__marks = marks    # private attribute

    # Getter methods
    def get_name(self):
        return self.__name

    def get_marks(self):
        return self.__marks

    # Setter methods
    def set_name(self, name):
        self.__name = name

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Invalid marks! Must be between 0 and 100.")


# Testing
s = Student("jadeja", 95)

print("Name:", s.get_name())
print("Marks:", s.get_marks())

s.set_marks(92)
print("Updated Marks:", s.get_marks())

s.set_marks(150)   # Invalid
