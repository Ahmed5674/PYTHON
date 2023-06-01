from abc import ABC, abstractmethod

# Abstract class
class AbstractClass(ABC):

    @abstractmethod
    def abstract_method(self):
        pass

    def non_abstract_method(self):
        print("This is a non-abstract method")

# Subclass
class SubClass(AbstractClass):

    def abstract_method(self):
        print("This is the implementation of abstract_method in SubClass")

# Main method
def main():
    # Creating an object of SubClass
    obj = SubClass()

    # Accessing the non-abstract method of AbstractClass
    obj.non_abstract_method()

    # Calling the abstract method of SubClass
    obj.abstract_method()

# Calling the main method
if __name__ == "__main__":
    main()

