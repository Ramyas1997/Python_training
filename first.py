class Parent:
    def __init__(self,name="NoName"):
        self.name=name

    def show(self):
        print(self.name," is the name of the father")

class Child(Parent):
    def __init__(self,name,cname,toyname):
        self.cname=cname
        super().__init__(name)
        self.toyname=toyname

    def print(self):
        print(self.cname," is the name of the child")
        print(self.toyname," is the toyname of the child")

firstchild = Child("Robin","Elephant")

firstchild.print()
firstchild.show()
© 2022 GitHub, Inc.
Terms