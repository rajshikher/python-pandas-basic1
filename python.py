l = [1,2,3]
print(l)

class Smartphone():

    def __init__(self, price, brand, camera, os, ram):
        print("pehle yahan")
        # super().__init__(price, brand, camera)
        self.os = os
        self.ram = ram
        print("inside the smartphone")

phone = Smartphone(344, "nike", "camera1", "windows", "12gb")
print(phone.ram)