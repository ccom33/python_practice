for student in [1,2,3,4,5]:
    print(student, "번 학생의 성적을 처리한다.")
#-------------------------    
sum = 0
for num in range(1,101):
    sum += num
print("합계는 =" ,sum)
#-------------------------
a = int(input("첫 숫자를 입력하세요."))
b = int(input("두번째 숫자를 입력하세요."))
sum = 0
for c in range(a,b+1,1):
    sum += c
print("첫수와 두번째수의 사이 합계는", sum)
#--------------------------
sum = 0
for num in range (2,101,2):
    sum += num
print("짝수 합계는", sum)
#--------------------------
for x in range (1,51):
    if (x % 10 == 0):
        print("+", end="")
    else:
        print('-', end="")
#--------------------------
a = int(input("\n첫번째 값을 입력하세요."))
b = int(input("두번째 값을 입력하세요."))
for d in range (a,b+1):
    if (d % 5 == 0):
        print("!", end="")
    else:
        print("-", end="")
#--------------------------

    
