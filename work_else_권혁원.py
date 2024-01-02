# 연습문제: 합격 여부 판단하기
written_test = 75
coding_test =True

if written_test >= 80 and coding_test:
    print("합격")
else:
    print("불합격")

# 심사문제: 합격 여부 판단하기
# 난 반복문 같은거 몰라
scores = input('').split()
avg = (float(scores[0]) + float(scores[1]) + float(scores[2]) + float(scores[3])) / 4

if avg >= 80.0:
    print("합격")
else:
    print("불합격")