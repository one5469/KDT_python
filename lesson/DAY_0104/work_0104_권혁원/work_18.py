DEBUG_NUM = int(input("Choose your solution : "))

# 연습문제: 3으로 끝나는 숫자만 출력하기
if DEBUG_NUM == 1:
    i= 0
    while i < 74:
        print(i, end=' ') if i % 10 == 3 else print('', end='')
        i += 1

# 심사문제: 두 수 사이의 숫자 중 3으로 끝나지 않는 숫자 출력하기
elif DEBUG_NUM == 2:
   start, stop = map(int, input().split())

   i = start

   while True:
       if i > stop:
           break
       print(i, end=' ') if i % 10 != 3 else print('', end='')
       i += 1