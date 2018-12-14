def line():
    print ("#", "-" *40)

sosi = "태연,서연,수영"

sing = sosi.split(",")
for s in sing:
    print(s, "사랑해")
line()
#-------------------------------------------------------
s1 = "아침에 커피로 시작하고 밥 먹고 커피 마시고 자기 전에도 커피를 마신다."
print(s1)
print(s1.replace("커피","우유"))
line()
#---------------------------------------------------------
scan = "901231-1914983"
birth = scan[0:2]
if (int(scan[7]) % 2 == 1):
    gen = "남자"
else:
    gen = "여자"
print("%s년생 %s" % (birth,gen))
#---------------------------------------------------------
line()

sum = 356
avg = 89.2785
print("총점 :", "%d" % sum ,"평균 :", "%4.2f" % avg)

sale = float(input("할인율"))
price = int(input("가격"))

print("가격은", price * sale)
            
