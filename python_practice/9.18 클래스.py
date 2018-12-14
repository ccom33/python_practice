balance = 8000

def deposit(money):
    global balance
    balance += money

def inquire():
    print("잔액은 %d원 입니다." % balance)
#-------------------------------------------------------------
deposit(1000)
inquire()

class Account:
    def __init__(self, balance):
        self.balance = balance
    def deposit(self, money):
        self.balance += money
    def inquire(self):
        print("잔액은 %d원입니다." % self.balance)

sinhan = Account(8000)
sinhan .deposit(1000)
sinhan.inquire()

nonghyup = Account(1200000)
nonghyup.inquire()

#------------------------------------------------------------

class Human:
    def __init__(self, age, name):
        self.age = age
        self.name = name
    def intro(self):
        print(str(self.age) + "살" + self.name + "입니다.")
kim = Human(29, "김상형")
kim.intro()
lee = Human(45, "이승우")
lee.intro()








