# 다양한 함수의 형태 - (2) 반환값 없는 함수

# - 함수 생성 문법
#   def 함수 이름(매개변수1, 매개변수2, ..., 매개변수n):
#       실행코드
#       실행코드

# 함수기능 : 2개의 정수를 덧셈 후 출력해주는 기능
# 함수이름 : addTwo
# 매개변수 : x, y
# 반환값 : 없음
def addTwo(x, y):
    value = x + y
    print(f'{x} + {y} = {value}')

# 함수 호출 시에 매개변수 갯수와 동일하게 데이터 전달해야 함
addTwo(10, 3)

# 함수기능 : 영어 단어를 입력 받아서 모두 대문자로 변환해주는 기능
# 함수이름 : convertCase
# 매개변수 : word
# 반환값 : 없음 ==> 아무 일을 안하게 됨 ==> return 하기

def convertCase(word):
    print(word.upper())

convertCase('str')

# 함수기능 : 시퀀스 객체의 모든 원소를 모두 대문자로 변환해주는 기능
# 함수이름 : convertCase2
# 매개변수 : str 타입의 원소로 구성된 list
# 반환값 : 없음

def convertCase2(dataList):
    dataList = [ s.upper() for s in dataList ]

def convertCase3(dataList):
    for idx, str in enumerate(dataList):
        dataList[idx] = str.upper()

# 함수 사용 즉, 함수 호술
data = ['abc', 'b', 'Ab']
print(f'[Before] {data}')

convertCase2(data)
print(f'[After] {data}')

convertCase3(data)
print(f'[After] {data}')



