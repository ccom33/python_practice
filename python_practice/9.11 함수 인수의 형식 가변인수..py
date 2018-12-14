print("태스트 진행중 입니다.")

def voidlay():
    pass
# 가변함수 입니다.
def intsum(*ints):
    sum = 0
    for num in ints:
        sum += num
    return sum

print(intsum(0,1,0,8,5,6,4,3,3,7,6))
print(intsum(3,10,20))

def calcstep(begin, end, step):
    sum = 0
    for num in range(begin, end + 1, step):
        sum += num
    return sum

print('1~10 =', calcstep(1,10,2))
