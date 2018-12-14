nums = [1,2,3,4,5]
print(nums)
nums.append(6)
print(nums)
nums.insert(2,99)
print(nums[2])
print(nums)
nums.insert(5,80)
print(nums[5])
print(nums)

nums = [1,2,3,4]
nums[2:2] = [90,91,92]
print(nums)

nums = [1,2,3,4]
nums[2] = [90, 91 ,92]
print(nums)

nums = [1,2,3,4]
nums.append(70)
nums.append(80)

print(nums)

list1 = [1,2,3,4,5,6,7,8,9]
list2 = [10,11,12,13,14]
list1.extend(list2)
print(list1)

list3 = [20,21,22,23,24]

print(list1 + list3)

score = [88,98,100,97,81,78]
score.remove(100)
print(score)

print(score.pop())
print(score.pop(3))
