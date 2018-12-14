for dan in range(2,10):
    print(dan, "단")
    for hang in range(2,10):
        print(dan, "*", hang, "=", dan * hang)
    print()

print("")
#-------------------------------
for y in range(1,11):
    for x in range(y):
        print("*", end = "")
    print()
#--------------------------------
print("3+4=?")
while True:
    a = int(input("정답을 입력하세요."))
    if (a == 7): break
print("축하합니다.")

for ten in range(0,5):
    for num in range(ten * 10, ten * 10 + 10):
        print(num, end = ",")
    print()

sum = 0
num = 0
while num <= 200:
    sum += num
    num += 3
print("sum = ", sum)

sum = 0

