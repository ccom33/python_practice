def line():
    print("#", "-" * 40)
#---------------------------
line()
s = "python programming"
print(len(s))
print(s.find('o'))
print(s.rfind('o'))
print(s.index('r'))
print(s.count('n'))
line()
#----------------------------------
s = """ 생각이란 생각할수록 생각나므로 생각하지 말아야 할 생각은 생각하지
않으려고 하는 생각이 옳은 생각이라고 생각합니다."""
print("생각의 출현 횟수 :" , s.count('생각'))
line()
#------------------------------------
name = "김한결"
if name.startswith("김"):
    print("김가입니다.")
if name.startswith("한"):
    print("한가입니다.")
#-----------------------------------------
line()
file = "girl.jpg"
if file.endswith(".jpg"):
    print("그림파일입니다.")
line()
#----------------------------------------
while True:
    alpha = input("알파벳을 입력하세요.")
    if alpha == "Q":
        break
    elif alpha.isalpha():
        print("모두 알파벳입니다.", alpha)
        break
    else:
        print("알파벳만 입력하세요.")
    continue
#----------------------------------------
s = input("영어를 입력하세요.")
print(s.lower())
print(s.upper())
print(s)

print(s.title())
