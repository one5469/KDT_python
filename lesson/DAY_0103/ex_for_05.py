# [실습1] 알고 싶은 단을 입력 받고 해당 단을 출력하세요.
# - input()
# - 특정 단의 구구단을 출력 => 반복문 사용하기
num = (input("숫자를 입력하세요. "))

if num.isdigit():
    num = int(num)
    print(f'-----{num}단-----')
    for i in range(1, 10):
        print(f'{num} * {i} = {num * i}', end='\t')
        if i % 3 == 0:
            print()
else:
    print("올바른 입력 형식이 아님")
print()

# [실습2] 2단 ~ 9단까지 모두 출력하세요. 반복문 사용하기
for i in range(2, 10):
    print(f'---{i}단---', end='\t')
print()
for i in range(1, 10):
    for j in range(2, 10):
        print(f'{j} * {i} = {i*j}', end='\t')
    print()

