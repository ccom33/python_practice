score = [92, 99, 89, 103, 59]
for s in score:
    if (s < 0 or s > 100):
        break
    print(s)
print("성적처리종료")

score = [92, 89, -1, 103, 78]
for s in score:
    if (s < 0 or s > 100):
        continue
    print(s)
print("성적처리종료")
