a = 30
if 1 < a < 29:
    print(" a입니다.")
else:
    print(" b입니다.")
    
age = int(input("나이를 입력하십시오."))
if age < 20:
    print("학생입니다.")
    print("공부를 해야합니다.")
else:
    print("성인입니다.")
    print("환영합니다.")
    
age = int(input("나이를 입력하십시오."))
if 1 <= age <=19:
    print("10대 입니다.")
elif 20 <= age <= 29:
    print("20대 입니다.")
elif 30 <= age <= 39:
    print("30대 입니다.")
elif 40 <= age <= 49:
    print("40대 입니다.")
else:
    print("50대 이상 입니다.")

man = True
age = 21
if man == True and age >=19:
    print("성인 남자입니다.")

man = True
age = 22
if man == True:
    if age >= 19:
        print("성인 남자입니다.")
    else:
        print("소년입니다.")
        
    
