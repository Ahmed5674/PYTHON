# Super class
class A:
    def __init__(self):
        self.__private_field = "Private field of A"
        self._protected_field = "Protected field of A"
        self.public_field = "Public field of A"

    def __private_method(self):
        print("Private method of A")

    def _protected_method(self):
        print("Protected method of A")

    def public_method(self):
        print("Public method of A")

    def call_private_method(self):
        self.__private_method()


# Sub class B
class B(A):
    def __init__(self):
        super().__init__()
        self.__private_field = "Private field of B"
        self._protected_field = "Protected field of B"
        self.public_field = "Public field of B"

    def __private_method(self):
        print("Private method of B")

    def _protected_method(self):
        print("Protected method of B")

    def public_method(self):
        print("Public method of B")


# Sub class C
class C(B):
    def __init__(self):
        super().__init__()
        self.__private_field = "Private field of C"
        self._protected_field = "Protected field of C"
        self.public_field = "Public field of C"

    def __private_method(self):
        print("Private method of C")

    def _protected_method(self):
        print("Protected method of C")

    def public_method(self):
        print("Public method of C")


# Main method
def main():
# Creating instances of classes A, B, and C
    objA = A()
    objB = B()
    objC = C()

# Accessing fields and methods of class A
    print(objA.public_field)
    objA.public_method()
    objA.call_private_method()
    print()

# Accessing fields and methods of class B
    print(objB.public_field)
    objB.public_method()
    objB.call_private_method()
    print()

# Accessing fields and methods of class C
    print(objC.public_field)
    objC.public_method()
    objC.call_private_method()
    print()


# Calling the main method
if __name__ == "__main__":
    main()

