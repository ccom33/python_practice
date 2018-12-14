def line():
    print("#","-"*40)
#----------------------------------------------------------- 
line()

def flunk(s):
    return s>60

score = [45, 89, 72, 54, 95]
for s in filter(flunk, score):
    print(s)

def half(s):
    return s*2

for s in map(half, score):
    print(s, end = ",")

s = 0

score = [45, 89, 72, 54, 95]
for s in filter(lambda x:x < 60, score):
    print(s)
    
