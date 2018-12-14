class Outer:
    def __init__(self,func):
        self.func = func

    def __call__(self):
        print("-" *20)
        self.func()
        print("-" *20)

def inner():
    print("결과를 출력합니다.")

inner = Outer(inner)
inner()

#------------------------------------------------------------------

inner()

class outer:
    def __init__(self,func):
        self.func = func

    def __call__(self):
        print("#","-"*50)
        self.func()
        print("#","-"*50)

@outer
def inner():
    print("결과를 출력합니다.")

inner()
