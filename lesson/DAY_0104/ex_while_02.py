# 반복문 - 2 while 반복문
# - 반복의 횟수가 정해진 경우 사용 가능함

# [요청] 사용자가 알고 싶어하는 단을 입력 받아서 해당 단의 구구단을 출력하기
#       단, while 반복문 사용하기
# [예시] 알고 싶은 단 입력 :
#       -- 3단 --
#       3 * 1 = 3
#       3 * 2 = 6
#       3 * 3 = 9
num = int(input("단 입력 : "))
i = 1
print(f' -- {num}단 --')
while i < 10:
    print(f'{num} * {i} = {num*i:>2}')
    i += 1
print()

# [요청] 2단 ~ 9단 출력
#       단, while 반복문 사용하기
# [예시] 알고 싶은 단 입력 :
#       -- 2단 --
#       2 * 1 = 3
#       2 * 2 = 6
#       2 * 3 = 9
#           :
#       -- 3단 --
#       3 * 1 = 3
#       3 * 2 = 6
#       3 * 3 = 9
#           :
a, b  = 2, 1

#
while a < 10:
    print(f' -- {a}단 -- ') if b == 1 else print('', end='')
    print(f'{a} * {b} = {a*b:2}')

    if b < 9:
        b += 1
    else:
        b = 1
        a += 1
print()

#
a, b = 2, 1

for i in range(a, 10):
    print(f' ---{i}단---', end='\t')
print()

while b < 10:
    print(f'{a} * {b} = {a*b:2}', end='\t')

    if a < 9:
        a += 1
    else:
        a = 2
        b += 1
        print()