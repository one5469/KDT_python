DEBUG_NUM = int(input("Choose your solution : "))

# 연습문제: 평균 점수 구하기
if DEBUG_NUM == 1:
    maria = {'korean' : 94, 'english' : 91, 'mathematics' : 89, 'science' : 83}
    keys = list(maria.keys())
    total = 0
    for k in keys:
        total += maria[k]

    average = total / 4
    print(average)

# 심사문제: 딕셔너리에서 특정 값 삭제하기
elif DEBUG_NUM == 2:
   keys = input().split()
   values = input().split()

   x = dict(zip(keys, values))

   x = [(x,y) for (x,y) in x.items() if x != 'delta' and y != '30']

   print(x)