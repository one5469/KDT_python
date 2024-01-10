DEBUG_NUM = int(input("Choose your solution : "))

# 연습문제: 공배수 구하기
if DEBUG_NUM == 1:
    a = {i for i in range(1, 101) if i%3==0}
    b = {i for i in range(1, 101) if i%5==0}

    print(a & b)

# 심사문제: 공약수 구하기
elif DEBUG_NUM == 2:
   x, y = input().split()

   if x.isdecimal() and y.isdecimal():
       x, y = map(int, (x, y))
       xset = { i for i in range(1, x+1) if x%i==0}
       yset = { i for i in range(1, y+1) if y%i==0}
       xyset = xset.intersection(yset)

       print(sum(xyset))