
myDict = {}

# 키만 읽어오는 메소드 => key() 메소드
keys = myDict.keys()

# 값만 읽어오는 메소드 => values() 메소드
values = myDict.values()

# 키와 값 묶어서 읽어오는 메소드 => items() 메소드
# (키, 값) 튜플 형식으로 묶어서
items = myDict.items()
print(f'myDict의 키/값 묶음들 : {items}, {type(items)}')

# 원소/요소 단위 접근 위해서는 형변환 필요함
items = list(myDict.items())
print(f'myDict의 키/값 묶음들 : {items[0]}, {type(items[0])}')

# 원소/요소 모두 삭제해주는 메소드 => clear() 메소드
myDict.clear()
print(f'myDict : {myDict}, {len(myDict)}')

# 원소/요소 데이터 읽기 메소드 => 변수명[키] ===> 값, get(키) 메소드
# => 키가 존재하지 않으면 None 반환
print(f'myDict.get("one") : {myDict.get("one")}, {myDict["one"]}')
print(f'myDict.get("three") : {myDict.get("three")}')

# 원소/요소 데이터 읽기 메소드 => 변수명[키] ===> 값, get(키, 기본값) 메소드
# => 키가 존재하지 않으면 기본값 반환
print(f'myDict.get("three", 0) : {myDict.get("three", 0)}')
print(f'myDict.get("three" "존재하지 않음") : {myDict.get("three", "존재하지 않음")}')

# 멤버 연산자 => 원소 in 여러개 저장 타입
#              원소 not in 여러개 저장 타입
# - 여러개 저장 타입 : str, list, tuple, dict, set
# - 연산 결과 => True / False

aList = [1, 2, 3]
aTuple = 11, 22
aDict = {1: 100, 2:100}

#                 =>  값 존재 여부
print(f'1 in aList  : {1 in aList}')
print(f'1 in aTuple : {1 in aTuple}')
#                 =>  키 존재 여부
print(f'1 in aDict  : {1 in aDict}')
print(f'1 in aDict  : {100 in aDict}')
