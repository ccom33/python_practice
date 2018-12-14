score = [
    [65,70,58,82],
    [88,77,92,98],
    [82,80,78,88],
    [89,90,67,68],
    [78,91,34,75],
    [55,39,80,85],
    [97,77,82,73],
    [77,88,56,91], # '스코어'의 리스트 값.
    ]
total = 0 # '토탈' 변수값
totalsub = 0 # '토탈서브' 변수값
high = 0 # 석차 1등의 변수값
for student in score: # 스코어 리스트에서 스튜던트로 읽어옴
    sum = 0 # sum 초기화
    for sj in student: # 스튜던트 리스트에서 sj로 읽어옴
        sum += sj
    sj = len(student) # len 함수로 스튜던트함수의 개수를 구함.
    if sum >= high: # 총합의값이 기존의 high (초기값은 0) 보다 높으면
        high = sum / sj # high 변수는 그 리스트의 sum값을 불러와서 평균을 구하고 high에 넣는다.
    total += sum # 전체 총점을 구하기위한 토탈 변수.
    totalsub += sj # 전체 평균을 구하기 위한 토탈 서브변수. (sj 값이 계속 더해짐.)
    print("총점%d, 평균,%.2f" % (sum, sum/sj)) 
print("전체 총점은%d, 전체 평균은%.2f" % (total, total/totalsub))
print("석차 1등의 평균은 %.2f" % high)
#------------------------------------------------
print("#","-"*40)



score = [90, 89, 79, 93, 89, 100, 83, 84]
sum = 0
for s in score:
    sum += s
    m = sum / len(score)
print("총점은 :", sum , "평균은 :", "%.2f" % m)
