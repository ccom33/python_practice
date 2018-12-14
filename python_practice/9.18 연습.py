

class Geforce:
    def __init__(self,model,price):
        self.model = model
        self.price = price
    def intro(self):
        print(str(self.model) + "입니다." + str(self.price) +"입니다.")
Gtxmain = Geforce(960, 120000)
Gtxmain.intro()
