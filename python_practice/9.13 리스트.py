def line():
    print("#","-"*40)
#-------------------------------------------
line()
score = [88, 95, 70, 100, 90]

for i in range(len(score)):
    print("#", score[i])

print(list("korea"))

print(score[0:4:2])

print(list("0123456789"))
#--------------------------------------------
line()
score = [80, 90, 100, 98, 76, 46, 92]
s = score[3:6]
sum = 0
for i in s:
    sum += i
    m = sum/len(s)
print("사회,경제,문화의 평균은", "%4.2f" % m)
print(score[6])
score[6] = 90
print(score[6])
print(score[2:5])
score[2:5] = [80, 79, 87]
print(score[2:5])
#------------------------------------------
nums = [0,1,2,3,4,5,6,7,8,9,]
nums[2:5] = [20,30,40]
print(nums)
nums[6:8] = [90,91,92,93,94]
print(nums)
nums[2:5] = []
print(nums[2:5])
del nums[4]
print(nums)

#-----------------------------------------
scoreandnums = score + nums
print(scoreandnums)
scoremulti = score * 4
print(scoremulti)
#------------------------------------------
line()
lol = [ [1,2,3,4], [4,5], [6,7,8,9]]
print(lol[0][2])

for sub in lol:
    for item in sub:
        print(item, end = '')
    print()

score = [ [88,76,92,98], [65,70,58,82], [82,80,78,88] ]
total = 0
talsub = 0
for s in score:
    sum = 0
    for sj in s:
        sum += sj
    sj = len(s)
    print("총점%d, 평균 %.2f" % (sum, sum / sj))
    total += sum
    talsub += sj
print("전체평균 %.2f" % (total / talsub))

score = [90, 89, 79, 93, 89, 100, 83, 84]
sum = 0
for s in score:
    sum += s
    m = sum / len(score)
print("총점은 :", sum , "평균은 :", "%.2f" % m)
