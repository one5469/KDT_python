# 다양한 함수의 형태 - 특별한 함수 (1)
# - 매개변수의 갯수를 유동적으로 가변으로 하는 함수
# - 형태 : def 함수명( *data ):
# - 가변 인자 함수
# - 매개변수 갯수 : 0개 ~ n개

# 2개의 정수를 덧셈 후 결과를 반환하는 함수 생성
def addFive(x, y):    return x+y

# 5개의 정수를 덧셈 후 결과를 반환하는 함수 생성
def addFive(a, b, c, d, e):     return a+b+c+d+e

# 3개의 정수를 덧셈 후 결과를 반환하는 함수 생성
def addFive(a, b, c):     return a+b+c

#   :
#   :
#   :

# 함수기능 : 전달 받은 숫자를 모두 덧셈한 결과 반환 기능
# 함수이름 : addNumber
# 매개변수 : *nums
# 반환값  : 계산 결과
def addNumber(*data):
    print(type(data))
    total = 0
    for i in data:
        total += i
    return total

print(addNumber(1,2,3))
print(addNumber(1))
print(addNumber())
print(addNumber(*(range(1, 11))))

aList = [11, 22, 33, 44]
aTuple = 'a', 'b', 'c'
aDict = {'yabal':'Hong', 'age':100}
print(*aList)
print(*aTuple)
print(*aDict)
print(**aDict)