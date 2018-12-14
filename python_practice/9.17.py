def line():
    print("#","-"*45)
#-----------------------------------------------------------------
line()
import random

for i in range(6):
    print(random.random())

for i in range(5):
    print(random.randint(1,50))

for i in range(6):
    print("랜덤수는 %.2f 입니다." % random.uniform(1,100))
#-----------------------------------------------------------------
line()
import random

food = ["짜장면", "짬뽕", "군만두", "탕수육"]

print(random.choice(food))

random.shuffle(food)
print(food)

print(random.sample(food,2))
#-----------------------------------------------------------------
line()

nums = random.sample(range(1,46),6)
nums.sort()
print(nums)

a = random.randint(1,9)
b = random.randint(1,9)
question = "%d + %d = ? " % (a,b)
c = int(input(question))

if c == a + b:
    print("정답입니다.")
else:
    print("틀렸습니다.")
#----------------------------------------------------------------
line()

correct = 0
while True:
    a = random.randint(10,99)
    b = random.randint(10,99)
    op = random.randint(1,3)

    if op == 1:
        ans = a+ b
        mark = "+"
    elif op == 2:
        if (a<b):
            a,b = b,a
        ans = a - b
        mark = "-"
    else:
        ans = a *b
        mark = "*"

    question = "%d %s %d = ? (끝낼때는 0) " % (a, mark,b)
    c = int(input(question))

    if c == 0:
        break
    elif c == ans:
        print("정답입니다.")
        correct = correct + 1
    else:
        print("틀렸습니다.")

print("%d개 맞췄습니다." % correct)

#---------------------------------------------------------------
line()

