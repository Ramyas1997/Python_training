class Father:
    def __init__(self,name):
        self.fname = name

    def show(self):
        print(self.fname," is father name")

class Mother:
    def __init__(self,name):
        self.mname = name

    def show(self):
        print(self.mname," is Mother name")

class Child(Father,Mother):
    def __init__(self,fname,mname,cname):
        self.cname=cname
        Father.__init__(self,fname)
        Mother.__init__(self,mname)

    def show(self):
        Father.show(self)
        Mother.show(self)
        print(self.cname," is the child name")

child1= Child("Rohan","Priya","Danial")
child1.show()