while True:
    str = input("점수를 입력하세요: ")
    try:
        score = int(str)
        print("입력한 점수 :", score)
        break
    except:
        print("점수 형식이 잘못되엇습니다.")
print("작업완료")
