def line():
    print('#','-' *40)
score = [88, 95, 70, 100, 99, 89, 90, 85]
print("학생수는 %d명입니다." % len(score))
print("최고 점수는 %d점입니다." % max(score))
print("최저 점수는 %d점입니다." % min(score))
#--------------------------------------------
score.sort()
print(score)
score.reverse()
print(score)
#----------------------------------------------
country = ["korea", "japan", "CHINA", "america"]
country.sort()
print(country)
country.sort(key = str.lower)
print(country)
#-----------------------------------------------
