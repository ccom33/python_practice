print("*" * 50, end = "p.141")
# print( 함수 (n)) 정보가 입력되있는 함수.
def calcsum(n):
    sum = 0
    for num in range(n + 1):
        sum += num
    return sum

# 선의 정보가 입력되어있는 함수.
def line():
    print("#","-"*50 )

print("\n")
print("~4 =", calcsum(4))
line()
print("~100 =", calcsum(100))
line()
print("~51 =", calcsum(51))
line()

# 1~10의 합을 입력해놓은 함수.
def teen10():
    sum = 0
    for num in range (1,11):
        sum += num
    print(sum)
# 함수 () 안에 인수값까지 1에서 부터 합을 구하는 함수.
def ten(n):
    sum = 0
    for num in range (n+1):
        sum += num
    print("~", n , "=", sum)

ten(9)
ten(10)
teen10()
# 나이를 입력 받아서 20세 이하이면 튕김. 100세 이상은 에러. 성인이면 환영합니다.
def test():
    while True:
        a = int(input("나이를 입력하세요.:"))
        if (a < 20):
            print("애들은 가라.")
        elif (a > 100):
            print("error")
        else:
            print("환영합니다.")
            break


test()
# 1~100의 수 중 3의배수의합 함수와 1~50중 4의배수의합 함수를 비교하는 프로그램.
def one():
    sum = 0
    for a in range (3,101,3):
        sum += a
    print(sum)
    return sum

def two ():
    sum = 0
    for b in range (4,51,4):
        sum += b
    print(sum)
    return sum

if (one()> two()):
    print("one 이 더 높습니다.")
else:
    print("two 가 더 높습니다.")
line()
