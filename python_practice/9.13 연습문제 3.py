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
    if sum >= high:
        high = sum
    total += sum
    totalsub += subject
    print("총점은 %d, 평균은 %.2f" % (sum, sum/subject))
print("전체 총점은 %d, 평균은 %.2f" % (total, total/totalsub))
print("전교 1등의 총점은 %d" % (high))
