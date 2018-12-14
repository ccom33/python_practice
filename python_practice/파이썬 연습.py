for i in range (1,10):
    if (i % 3 == 0):
        continue
    else:
        print(i)
num = 3
sum = 0
while num <= 200:
    sum += num
    num += 3
print(sum)
    
