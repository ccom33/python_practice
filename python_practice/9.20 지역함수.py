def makeHello(message):
    def hello(name):
        print(message + ", " + name)
    return hello

enghello = makeHello("Good Mornig")
hanhello = makeHello("안녕하세요")

enghello("Mr kim")
hanhello("홍길동")

def inner():
    print("결과를 출력합니다.")

def outer(func):
    print("_" *40)
    func()
    print("-" *40)

outer(inner)

def inner():
    print("결과를 출력합니다.")

def outer(func):
    def wrapper():
        print("-"* 50)
        func()
        print("-"* 50)
    return wrapper

inner= outer(inner)
inner()

def outer(func):
    def wrapper():
        print("-"* 50)
        func()
        print("-"* 50)
    return wrapper

@outer
def inner():
    print("결과를 출력합니다.")

inner()

def para(func):
    def wrapper():
        return "<p>" + str(func()) + "</p>"
    return wrapper

@para
def outname():
    return "김상형"
@para
def outage():
    return "29"

print(outname())
print(outage())
