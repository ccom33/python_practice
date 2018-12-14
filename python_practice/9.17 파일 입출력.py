
try:
    f = open("live.txt", "rt")
    text = f.read()
    print(text)
except FileNotFoundError:
    print("파일이 없습니다.")
finally:
    f.close()

try:
    f = open("C:/Users/USER/Desktop/threadDump-20180912-083318.txt", "rt")
    text = f.read()
    print(text)
except FileNotFoundError:
    print("파일이 없습니다.")
finally:
    f.close()

f = open("live.txt", "rt")
while True:
    text = f.read(5)
    if len(text) == 0: break
    print(text, end ="")
f.close()
#---------------------------------------------------------

f = open("live.txt", "rt")
text = ""
line = 1
while True:
    row = f.readline()
    if not row: break
    text += str(line) + " : " + row
    line += 1
f.close()
print(text)

#------------------------------------------------ 입력값을 택스트로 바로 넣는함수.
a = input("이름을 입력하세요.")
f = open("name.txt", "wt")
f.write(a)
f.close()
#-------------------------------------------------- 입력값을 디스플레이함.
f = open("name.txt", "rt")
text = f.read()
print(text)

f = open("live.txt", "rt")
f.seek(12,0)
text = f.read()
f.close()
print(text)

f = open("live.txt", "at")
f.write("\n\n푸쉬킨 형님의 말씀이었습니다.")
f.close()

with open ("live.txt", "rt") as f:
    text = f.read()
print(text)

import shutil
shutil.copy("live.txt", "live2.txt")
