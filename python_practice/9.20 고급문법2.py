def calc(op,a,b):
    op(a,b)

def add(a,b):
    print(a+b)
    return a+b

def minus(a,b):
    print(a-b)

def star(a,b):
    print(a**b)

def multi(a,b):
    print(a*b)

calc(star,6,2)
calc(minus,9,4)


def calcsum(n):
    def add(a,b):
        return a+b

    sum = 0
    for i in range(n+1):
        sum = add(sum,i)
    return sum

    
    
print("~10 =", calcsum(10))

    
