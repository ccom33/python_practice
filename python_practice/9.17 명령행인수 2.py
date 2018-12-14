import sys
import time


#---------------------------------------------------------
str = "89점"
try:
    score = int(str)
    print(score)
except:
    print("예외가 발생했습니다.")
print("작업완료")

num1 = int(input("수를 입력하세요.1  "))
num2 = int(input("수를 입력하세요.2  "))

try:
    reslut = num1/num2
    print("결과는 %d 입니다." % reslut)
except ZeroDivisionError:
    print("결과를 0으로 나눌수없습니다.")

dic = {'boy':'소년', 'school':'학교', 'book':'책'}
try:
    print(dic['girl'])
except:
    print("찾는 단어가 없습니다.")

try:
    print("네트워크 접속")
    a = 2/0
    print("네트워크 통신 수행")
finally:
    print("접속 해제")
print("작업 완료")
