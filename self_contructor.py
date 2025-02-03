class computer:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def fun2(self):
       print(self.name, self.age)
    
    def compare(self,others):
        if self.name == others.name:
            print("Names are same")
        elif self.age == others.age:
            print("Ages are same")




c1= computer("Mithun",22)
c2= computer("Dileep",22)
# c1.name="Dileep"
print(c1.fun2())
c1.compare(c2)
