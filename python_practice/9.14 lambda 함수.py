score = [45, 89, 72, 54, 95]
for s in filter(lambda x:x >60, score):
    print(s)
for s in map(lambda x:x /2, score):
    print(s)

sale = float(input("할인율은?"))
price = int(input("가격은?"))

s = [sale, price]

for s in map(lambda x:x *int(sale), price):
    print(s)
