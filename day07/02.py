# Inheritance
class A:
    def __init__(self) -> None:
        print("Init : A")
    def m1(self):
        print("Hello m1 in A")
class B(A): # classNAme(Parent_CLassNAme)
    def __init__(self) -> None:
        print("Init : B")
    def m2(self):
        print("Hello m2 in B")

a1 = A()
a1.m1()

b1=B()
b1.m2()
b1.m1()