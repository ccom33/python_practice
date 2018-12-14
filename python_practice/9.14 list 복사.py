a = 3
b = a
print("a = %d, b = %d" % (a,b))
a = 5
print("a = %d, b = %d" % (a,b))

list1 = [1,2,3]
list2 = list1

list2[1] = 100
print(list1)
print(list2)

list1 = [1,2,3]
list2 = list1.copy()

list2[1] = 100
print(list1)
print(list2)

list0 =['a','b']
list1 =[list0, 1, 2,]
list2 = list1.copy()

list2[0][1] = 'c'
print(list1)
print(list2)

import copy

list0 = ["a","b"]
list1 = [list0, 1, 2]
list2 = copy.deepcopy(list1)

list2[0][1] = "c"
print(list1)
print(list2)

list1 = [1,2,3]
list2 = list1
list3 = list1.copy

print("1 == 2" , list1 is list2)
print("1 == 3" , list1 is list3)
print("2 == 3" , list2 is list3)


