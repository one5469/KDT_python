# 다양한 함수의 형태 - (1) 기본

# 함수기능 : 팩토리얼을 계산 후 계산 결과를 반환해주는 기능
# 함수이름 : factorial
# 매개변수 : x
# 반환값  : 결과

def factorial(x):
    result = 1
    for i in range(x, 0, -1):
        result *= i

    return result

def factorial2(x):
    if x == 0:
        return 1
    elif x <= 2:
        return x
    else:
        return x * factorial2(x-1)

def factorial3(x):
    result = 1
    array = [ i for i in range(1, x+1) ]
    for i in array:
        result *= i
    return result

print(factorial(5), factorial2(5), factorial3(5))
print(factorial(0), factorial2(0), factorial3(0))

# 함수기능 : 팩토리얼을 계산 후 계산 결과를 반환해주는 기능
# 함수이름 : factorial
# 매개변수 : x
# 반환값  : 계산 과정

def fatorial4(x):
    print(f'{x}! ', end='= ' if x != 0 else '')
    result = 1
    for i in range(x, 0, -1):
        print(f'{i}', end=' * ' if i != 1 else ' ')
        result *= i
    print(f'= {result}')

fatorial4(2)