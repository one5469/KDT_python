# 반복문과 내장함수=> map(), zip()

xList = [1, 3, 5, 7]

# xList안에 모든 원소를 정수 int로 변환 후 저장해 주세요
# xList[0] = int(xList[0])
# xList[1] = int(xList[1])
# xList[2] = int(xList[2])
# xList[3] = int(xList[3])
for idx in range(len(xList)):
    xList[idx] = int(xList[idx])

print(f'xList => {xList}')

# 시퀀스 또는 반복이 가능한 객체의 요소/원소에 적용 후 값을 다시 저장해야 하는 경우
# 자주 사용되는 기능으로 내장함수로 제공 => map()
# - 문법 : map(함수명, 시퀀스 또는 반복이 가능한 객체)

# int 요소인 xList를 str요소로 변환
result = list(map(str, xList))
print('result =>', result)

# list 데이터를 dict 데이터로 생성
x = ['std01', 'std02', 'std03']
y = [90, 100 ,99]

# 방법 (1) ---> 기호/부호
xyDict = {}
for i in range(len(x)):
    xyDict[x[i]] = y[i]
print(f'xyDict => {xyDict}')

# 방법 (2) ---> dict() 생성자 함수
xyDict = dict()
for i in range(len(x)):
    xyDict[x[i]] = y[i]
print(f'xyDict => {xyDict}')

# 방법 (3) ---> dict([(키, 값), (키, 값), ...]) 생성자 함수
xy = []
for i in range(len(x)):
    xy.append((x[i], y[i]))
xyDict = dict(xy)
print(f'xyDict => {xyDict}')

# 방법 (4) ---> 내장함수 zip()
xyDict = dict(zip(x, y))
print(f'xyDict => {xyDict}')
