import statistics

score = [30, 40, 60, 70, 80, 90]
print(statistics.mean(score))
print(statistics.harmonic_mean(score))
print(statistics.median(score))
print(statistics.median_low(score))
print(statistics.median_high(score))


import time

print(time.time())

t = time.time()
print(time.ctime(t))

import time
now = time.localtime()
print("%d년 %d월 %d일"%(now.tm_year,now.tm_mon,now.tm_mday))
print("%d:%d;%d"%(now.tm_hour,now.tm_min,now.tm_sec))


import time

start = time.time()
for a in range(1000):
    print(a)
end = time.time()
print(end - start)


print("안녕하세요.")
time.sleep(1)
print(" 밤에 성시경이 두명 잇으면 뭘가요?")
time.sleep(1)
print("야간투시경입니다.")



for dan in range(2,10):
    print(dan, "단")
    for hang in range(2,10):
        print(dan, "*", hang, "=", dan*hang)
        time.sleep(0.1)
    print()
    time.sleep(0.1)

import calendar

print(calendar.calendar(2018))
print(calendar.month(2019, 1))
