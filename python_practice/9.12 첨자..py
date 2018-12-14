def line():
    print("#", "-" * 40)
#-------------------------------
s = "I love python"
print(s[3])
print(s[7])
print(s[-6])

#-------------------------------

s = "python"
for c in s:
    print(c ,end = ',')

line()
#--------------------------------
s = "I love python"
for i in range(len(s)):
    print(s[i], end = ',')

line()
#---------------------------------
s = "I love python"
print(s[3:6])
print(s[6:10])

line()

#--------------------------------------
file = "20171224-104830.jpg"
print("촬영 날짜 :" + file[4:6] + "월" + file[6:8] + "일")
print("촬영 시간 :" + file[9:11] + "시" + file[11:13] + "분")
print("확장자 :" + file[-3:])
#---------------------------------------
a = input("사진 이름을 입력하세용.")
file = a
print("촬영 날짜 :" + file[4:6] + "월" + file[6:8] + "일")
print("촬영 시간 :" + file[9:11] + "시" + file[11:13] + "분")
print("확장자 :" + file[-3:])
