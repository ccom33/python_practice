sum = 0
num = 0
while num <= 200:
    sum += num
    num += 3
print("sum = ", sum)

for a in range (1,11):
    if(a % 3 == 0):
        continue
    else:
        print(a)

sum = 0
for b in range (3,201,3):
    sum += b
print("sum=", sum)
# 삼각형 그리는 문제. 반대로한 이등변 삼각형.
for y in range(1,11):
    for s in range(11-y):
        print(" ", end = "")
    for x in range(y):
        print("*", end ="")
    print()
# 이등변 삼각형.
for y in range (1,11):
    for x in range (y):
        print("*", end="")
    print()
# 
for y in range(1,11):
    for s in range(11-y):
        print(" ", end = "")
    for x in range(y*2-1):
        print("*", end ="")
    print()
