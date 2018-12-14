score = [80,90,95,75,65,100]
sum = 0
for s in score:
    sum += s
print("합계는 :%d" % (sum))
print("평균은 :%.2f" % (sum/len(score)))

a = int(input("수를 입력하세요. 1 "))
b = int(input("수를 입력하세요. 2 "))
c = int(input("수를 입력하세요. 3 "))

sum = 0

score = [a,b,c]

for s in score:
    sum += s
print("총합계는 : %d" % (sum))
print("총평균은 : %.2f" % (sum/len(score)))

score = [
    [88,90,100,98,97],
    [90,70,75,91,85],
    [96,91,79,87,90]
]
total = 0
totalsub = 0
for student in score:
    sum = 0
    for subject in student:
        sum += subject
    subject = len(student)
    print('총점은 : %d, 평균은 %.2f' % (sum, sum/subject))
    total += sum
    total += subject
print("전체 평균은 : %.2f" % (total / totalsub))
    
