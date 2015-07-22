class Mother():
    def normalMethod(self):
        print("I'm your father. -Darth Vader")

    def MotherPower(self):
        print("Power!!!!!!!!!!!!!!!!")

class Son(Mother):
    #overloading
    def normalMethod(self, name):
        print("I'm your son. -%s"%name)

    def OneOfKind(self):
        print("But.. You're not the only one")

print("*****Testing Mother class*****")
A=Mother()
A.normalMethod()
A.MotherPower()

print("\n")

print("*****Testing Son class*****")
B=Son()
B.normalMethod("Kim")
B.MotherPower()
B.OneOfKind()
