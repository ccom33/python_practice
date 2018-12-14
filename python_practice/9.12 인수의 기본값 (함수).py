def line():
    print("#", "-" * 35)
    
def calstep(begin, end,step = 1):
    sum = 0
    for num in range(begin, end+1, step):
        sum += num
    return sum

print("1~10 =", calstep(1,10,2))

def calcstep(begin, end, step):
    sum = 0
    for num in range(begin, end+1, step):
        sum += 0
    return sum

print("3~5 = ", calstep(begin = 3, step = 1, end = 5))
print("3~5 = ", calstep(end = 5, step = 1, begin = 3))
#-----------------------------------------------------
line()

salerate = 0.9

def kim ():
    print("오늘의 할인율 :", salerate)

def lee():
    price = 1000
    print("가격 :", price * salerate)

kim()
salerate = 1.1
lee()

line()
#---------------------------------------    
def k():
    temp = "김과장의 함수"
    print(temp)

def l():
    temp = 2**10
    return temp

def park(a):
    temp = a*2
    print(temp)

k()
print(l())
park(10)
line()
#---------------------------------------
price = 1000
def sale():
    price = 500
sale()
print(price)
line()
#-----------------------------------------
price = 1000

def sal():
    price = 500
    print("sale", id(price))

sale()
print("global", id(price))
line()
#-----------------------------------------
price = 1000

def sale():
    global price
    price = 400

sale()
print(price)

a = int(input("숫자를 입력하세요.(1)"))
b = int(input("숫자를 입력하세요.(2)"))
c = int(input("숫자를 입력하세요.(3)"))
def avg():
    sum = a + b + c
    return sum / 3
avg()
print(avg())

def avg2(a,b,c):
    sum = a + b + c
    return sum / 3
print(avg2(80,90,70))
line()
