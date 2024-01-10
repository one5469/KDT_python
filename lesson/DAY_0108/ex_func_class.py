import random
# 함수와 클래스
# 변수에 어떤 데이터를 저장하고 있는 지 확인 함수 => type(함수명)
data = 1
print(f'data Type => {type(data)}')

data = 'Good'
print(f'data Type => {type(data)}')

# 함수명의 타입
print(f'id() Type => {type(id)}')

# 사용자 정의 함수 생성
# 함수 기능 : 2개 정수 더한 후 결과 출력 기능
# 함수 이름 : addTwo
# 매개 변수 : n1, n2
# 함수 결과 : 없음
def addTwo(n1, n2):
    print(n1+n2)

# 함수의 타입 ===> type() 내장함수 사용 => class function
print(type(addTwo))

# 함수와 변수
# - 함수명은 코드의 시작 주소를 저장하고 있음
# - 함수명을 변수에 대입 가능
test = addTwo
print(f'test   => {id(test)}, {type(test)}')
print(f'addTwo => {id(addTwo)}, {type(addTwo)}')

test(10, 2)

# [활용예]
# - 1~10 범위에서 임의의 정수 5개를 저장
# - 중복된 정수 저장 가능
def randomFive():
    result = [ random.randint(1, 10) for i in range(5) ]

    return result

nums = randomFive()

# 5개의 정수에서 최대값, 최소값, 내림차순 정렬된 값 출력
print(f'최대값 : {max(nums)}')
print(f'최소값 : {min(nums)}')
print(f'정렬  : {sorted(nums, reverse=1)}')
print(f'합계  : {sum(nums)}')
print(f'개수  : {len(nums)}')

# 여러 개의 함수 이름을 변수에 저장 => 리스트 사용함
funs = [max, min, sorted, sum, len]
for f in funs:
    if f == sorted:
        print(f(nums, reverse=1))
    else:
        print(f(nums))

funs_dict = {'최대값':max, '최소값':min, '정렬':sorted, '합계':sum, '개수':len}
for k, v in funs_dict.items():
    if v == sorted:
        print(f'{k} : {v(nums, reverse=1)}')
    else:
        print(f'{k} : {v(nums)}')