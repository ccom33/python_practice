score = [
    [65,70,58,82],
    [88,77,92,98],
    [82,80,78,88],
    [89,90,67,68],
    [78,91,34,75],
    [55,39,80,85],
    [97,77,82,73],
    [77,88,56,91]
    ]
total = 0
totalsub = 0
high = 0
for student in score:
    sum = 0
    for subject in student:
        sum += subject
    subject = len(student)
    if sum/subject >= high:
        high = sum/subject
    total += sum
    totalsub += subject
    print("총점은%d, 평균은%.2f" % (sum, sum/subject))
print("석차1등의 평균은 %.2f" % (high))
print("전체총점은%d, 전체평균은%.2f" % (total, total/totalsub))
          
