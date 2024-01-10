# filter(함수명, 반복가능객체)
# - 조건에 맞는 데이터만 반환
from functools import reduce

# 예) 5초과 10미만 데이터만 추출
a = [8,3,2,10,15,7,1,9,0,11]

def check(data):
    return data>5 and data<10

print(list(filter(check, a)))

def f(x, y):
    return x+y

print(reduce(f, a))
print(reduce(lambda  x, y : x+y, a))