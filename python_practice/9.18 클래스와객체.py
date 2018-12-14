class Book:
    def __init__(self,author,company,page,price):
        self.author = author
        self.company = company
        self.page = page
        self.price = price
    def intro(self):
        print(self.author + "입니다." + str(self.price) + "입니다.")

justice = Book("마이클 샌델", "북앤클럽", "967page", "19,500")
bonobono = Book("김신회", "북앤클럽", "320page", "16,000")
cho = Book("권오현" , "쌤앤파커스", "336page", "16,200")

justice.intro()
#----------------------------------------------------------------------

class Human:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def intro(self):
        print(str(self.age) + "살" + self.name + "입니다")

class Student(Human):
    def __init__(self, age, name, stunum):
        super().__init__(age,name)
        self.stunum = stunum

    def intro(self):
        super().intro()
        print("학번 :" + str(self.stunum))
    def study(self):
        print("1교시 전공, 2교시 교양")

kim = Human(29, "김상형")
kim.intro()
lee = Student(34, "이승우", 930011)
lee.intro()
lee.study()
sun = Student(21, "선우희", 981231)
doe = Student(23, "도경수", 960327)
hyun = Human(25, "김현수")
sun.intro()
doe.intro()
hyun.intro()
#---------------------------------------------------------------------

kim.name = "정우성"
kim.age = 45
print(kim.name, kim.age)

#----------------------------------------------------------------------

class Date:
    def __init__(self, month):
        self.month = month
    def getmonth(self):
        return self.month
    def setmonth(self, month):
        if 1 <= month <= 12:
            self.month = month

today = Date(8)
today.setmonth(15)
print(today.getmonth())

