class A:
    def display(self):
        print("Display Inside class A")

    def show(self):
        print("Show Inside class A")


class B(A):
    def print(self):
        print("Print Inside class B")

    def show(self):
        print("Show Inside class B")


class C(B):
    def show(self):
        print("Show Inside class C")


# Driver code
a = A()
a.display()
a.show()

b = B()
b.display()
b.print()
b.show()

c = C()
c.display()
c.print()
c.show()

# Call overridden method with super class reference
super_ref_b = B()
super_ref_b.show()

super_ref_c = C()
super_ref_c.show()

