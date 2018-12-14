def line():
    print("#","-"*40)
line()
#--------------------------------------------
score = [80, 95, 70, 100, 99, 80, 78, 50]
score.remove(100)
print(score)
del(score[2])
print(score)
score[1:4]=[]
print(score)
#--------------------------------------------- 현재 시간을 보여주는 함수.
line()

import time

def gettime():
    now = time.localtime()
    return now.tm_hour, now.tm_min

result = gettime()
print("지금은 %d시 %d분입니다" % (result[0], result[1]))

line()
#----------------------------------------------------

score = [88, 95, 70, 100, 90]
tu = tuple(score)
# tu[0] = 100
print(tu)
li = list(tu)
li[0] = 100
print(li)
line()
#-------------------------------------------------------
dic = {'boy' : '소년', 'school' : '학교', 'book' : ' 책' }
print(dic)
line()
#-----------------------------------------------------------
dic = {'boy' : '소년', 'school' : '학교', 'book' : ' 책' }
print(dic.get('student'))
print(dic.get('student', '사전에 없는 단어입니다.'))
#-----------------------------------------------------------
line()
dic = {'boy' : '소년', 'school' : '학교', 'book' : ' 책' }
if 'student' in dic:
    print("사전에 있는 단어입니다.")
else:
    print("이 단어는 사전에 없습니다.")
#-----------------------------------------------------------
line()
print(dic.keys())
print(dic['boy'])
print(dic.get('water', '사전에 없는 단어 입니다.'))

a = input("단어를 입력하세요.")
dic = {'boy' : '소년', 'school' : '학교', 'book' : ' 책' }
if a in dic:
    print('사전에 있는 단어 입니다.')
else:
    print('사전에 없는 단어 입니다.')
print(dic.keys())
print(dic.values())
print(dic.items())
#-----------------------------------------------------------
line()
dic2 = {'student' : '학생', 'teacher' : '선생님'}
dic.update(dic2)
print(dic)

