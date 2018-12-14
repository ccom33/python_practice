import random

secret = random.randint(1,100)
while True:
    num = int(input("숫자를 입력하세요(끝낼때 0) : "))
    if num == 0:
        break
    if num == secret:
        print("맞췄습니다")
        break
    elif num > secret:
        print("입력한 숫자보다 더 작습니다.")
    else:
        print("입력한 숫자보다 더 큽니다.")

secret = random.randint(1,100)
count = 0
while True:
    num = int(input("숫자를 입력하세요(끝낼때 0) : "))
    if num == 0:
        print("종료하였습니다.")
        break
    count += 1
    if num == secret:
        print("정답입니다.")
        print("%d번만에 맞췄습니다." % count)
        break
    elif num > secret:
        print("입력한 숫자보다 더 작습니다.")
    else:
        print("입력한 숫자보다 더 큽니다.")

import sys

print("버전 :" , sys.version)
print("플랫폼 :" , sys.platform)
if (sys.platform == "win32"):
    print(sys.getwindowsversion())

print("바이트 순서:", sys.byteorder)
print("모듈 경로:", sys.path)
sys.exit(0)
