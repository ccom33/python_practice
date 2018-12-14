a = [n for n in range (1,11)]
b = [n*n for n in range(1,11)]
dic = dict(zip(a,b))
print(dic[6])

price = [ 1000, 2000, 3000, 4000, 5000]
price2 = map(lambda p:p *0.8, price)
for p in price2:
    print("가격은: %d" % p)

price = [ 1000, 2000, 3000, 4000, 5000]
price2 = map(lambda p:p *0.8, price)
for p in price2:
    print("가격은: %d" % p)

