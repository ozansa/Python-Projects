# Class demonstrating encapsulation
class Protected:
    def __init__(self):
        # Protected attribute (by convention, a single underscore is used)
        self._protectedVar = 0
        # Private attribute (by convention, a double underscore is used)
        self.__privateVar = 12

    # Getter for private attribute
    def getPrivate(self):
        print(self.__privateVar)

    # Setter for private attribute
    def setPrivate(self, private):
        self.__privateVar = private

# Create an object of the class
obj = Protected()

# Access and modify the protected attribute
print(obj._protectedVar)   # Accessing the protected variable directly
obj._protectedVar = 34      # Modifying the protected variable
print(obj._protectedVar)

# Access and modify the private attribute using getters and setters
obj.getPrivate()            # Getting the private variable's value
obj.setPrivate(23)          # Setting a new value to the private variable
obj.getPrivate()            # Getting the updated private variable's value
