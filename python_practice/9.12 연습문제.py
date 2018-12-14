def line():
    print("#", "-" * 40)
#---------------------
a = int(input("숫자를 입력하세요.(1)"))
b = int(input("숫자를 입력하세요.(2)"))
c = int(input("숫자를 입력하세요.(3)"))
def avg():
    sum = a + b + c
    return sum / 3
avg()
print(avg())
line()
#-----------------------
def avg2(a,b,c):
    sum = a + b + c
    return sum / 3
print(avg2(80,90,70))
line()
#-----------------------
def intt(*nums):
    m = nums[0]
    for a in nums:
        if (a > m):
            m = a
    return m
print(intt(8,9,3,4,5,6,7,10))
line()
#----------------------------------    
def find_(*ints):
    num = 0
    for i in ints:
        if i >= num:
            num = i
        else:
            continue
    return num

print(find_(8,10,13))
line()
#-----------------------------------
