# set 데이터 타입
# - 제일 마지막에 추가된 타입
# - 목적 : 중복 데이터 제거
# - 특징 : 이미 존재하는 데이터는 저장하지 않음
# - 문법 : { 데이터1, 데이터2, ... , 데이터n }

# 빈 데이터 타입 생성
aStr = ''
aList = []
aTuple = ()
aDict = {}
aSet = set()

print(f'aStr   => {type(aStr)},     {len(aStr)}개')
print(f'aList  => {type(aList)},    {len(aList)}개')
print(f'aTuple => {type(aTuple)},   {len(aTuple)}개')
print(f'aDict  => {type(aDict)},    {len(aDict)}개')
print(f'aSet   => {type(aSet)},     {len(aSet)}개')
print()

# 생성자 메소드 => 타입 이름과 동일한 함수명
# - 힙 영역에 메모리 공간 잡고 데이터 초기화 기능 수행
aStr = str()
aList = list()
aTuple = tuple()
aDict = dict()
aSet = set()

print(f'aStr   => {type(aStr)},     {len(aStr)}개')
print(f'aList  => {type(aList)},    {len(aList)}개')
print(f'aTuple => {type(aTuple)},   {len(aTuple)}개')
print(f'aDict  => {type(aDict)},    {len(aDict)}개')
print(f'aSet   => {type(aSet)},     {len(aSet)}개')

# set 타입의 데이터 생성
a1 = {1,1,2,3,4,5,1,1,1,1,1,1,1,1}
a2 = [1,1,2,3,4,5,1,1,1,1,1,1,1,1]

print(f'a1   => {type(a1)},     {len(a1)}개, {a1}')
print(f'a2   => {type(a2)},     {len(a2)}개, {a2}')

# 다른 데이터 타입에서 중복 데이터 제거 시에 활용 => 형변환
a2 = list(set(a2))
print(f'a2   => {type(a2)},     {len(a2)}개, {a2}')

# set 타입의 연산 수행 => 미지원
a1 = {1,3,5,1,2}
b1 = {1,2,3,4,5,6,7,8,9,10}

# print(a1 + b1)
# print(a1 * 2)

# 연산 수행 ==> 형변환
a1 = list(a1)
print(a1 * 2)

# 원소/요소 읽기/수정/삭제/추가 ===> 인덱스X, 키X ==> 메소드 제공

# 원소/요소 추가 => 1개 추가 : append() 메소드
a1 = set(a1)
a1.add(10)
a1.add(10)
print(f'a1   => {type(a1)},     {len(a1)}개, {a1}')

a1.add('A')
print(f'a1   => {type(a1)},     {len(a1)}개, {a1}')

# 여러개의 원소/요소 추가 => update() 메소드
a1.update([11,22,33,44])
print(f'a1   => {type(a1)},     {len(a1)}개, {a1}')

a1.update("Good Luck")
print(f'a1   => {type(a1)},     {len(a1)}개, {a1}')

a1.add("Good Luck !!")
print(f'a1   => {type(a1)},     {len(a1)}개, {a1}')

# 원소/요소 삭제 => remove(데이터)
a1.remove("G")
print(f'a1   => {type(a1)},     {len(a1)}개, {a1}')

# 원소/요소 꺼내기 => pop()
data = a1.pop()
print(f'a1   => {data}, {type(a1)},     {len(a1)}개, {a1}')

a1.discard('g')
print(f'a1   => {type(a1)},     {len(a1)}개, {a1}')

# 집합에 관련된 메소드들과 기호 / 연산자

# 교집합
# - 여러 개의 집합에 공통으로 존재하는 데이터만 추출
# - 기호/연산자 : & and 연산자
# - 메소드 : intersection()
a1.clear()
a1.update('Happy')
print(f'a1 => {a1}')

a2 = a1.intersection({'a', 'A', 'b', 'B'})
print(f'a2 => {a2}', a1 & {'a', 'A', 'b', 'B'})

# 합집합
# - 여러 개의 집합에 공통으로 존재하는 데이터만 추출
# - 기호/연산자 : | or 연산자
# - 메소드 : union()
a2 = a1.union({'a', 'A', 'b', 'B'})
print(f'a2 => {a2}', a1 | {'a', 'A', 'b', 'B'})

# 차집합
# - 교집합 데이터 제외한 나머지 데이터
# - 기호/연산자 : - 뺄셈 연산자
# - 메소드 : difference()
a2 = a1.difference({'a', 'A', 'b', 'B'})
print(f'a2 => {a2}', a1 - {'a', 'A', 'b', 'B'})

# 정렬
# => 원소 값을 서로 비교해서 작은 데이터 >> 큰 데이터 순서로 저장 => 오름차순 정렬
# => 원소 값을 서로 비교해서 큰 데이터 >> 작은 데이터 순서로 저장 => 내림차순 정렬
# => set 타입에는 정렬 메소드 없음 ==> 내장함수 sorted()
a1 = sorted(a1)
print(f'a1 => {type(a1)}, {a1}')