for i in range (1,6):
    print("-"*9, end = "")
    print("+", end = "")
print("")
for x in range (1,51):
    if (x % 10 == 0):
        print("!", end="")
    else:
        print("-", end="")
####        
print("")
for y in range (1,51):
    if (y % 10 == 5):
        print("+", end = "")
    else:
        print("_", end = "")


