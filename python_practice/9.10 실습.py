country = input("국적은?")
age = int(input("나이는?"))
if country == "korea" and age >= 20:
    print("한국성인 입니다.")
    
score = int(input("점수를 입력하세요."))
if score >= 80:
    print("합격")
else:
    print("불합격")
    
anwser = input("한국의 수도는?")
if anwser == "서울":
    print("정답")
    print("축하합니다.")

age = int(input("나이는?"))
height = int(input("키는?"))
if age >= 8 and height >= 100:
    print("탑승가능합니다.")
else:
    print("이용이 불가능 합니다.")

g = input("성별을 입력하세요.")
age = int(input(

#------------ 몰랐던것들. ------
dir = input("방향을 입력하세요.")
if dir == '서':
    print('강서')
elif dir == '동':
    print('강동')
elif dir == '남':
    print('강남')
elif dir == '북':
    print('강북')
else:
    print("error")
    
서울우유 = 2500/1000
매일우유 = 4200/1800
if 서울우유 < 매일우유:
    print("매일우유 사세요.")
else:
    print("서울우유 사세요.")

정수 = int(input('숫자를 입력하세요.'))
if 정수%5 == 0:
    print("5의배수 입니다.")
else:
    print("5의배수가 아닙니다.")
