# 리스트(list) 데이터 타입
# - 여러 종류의 여러 개의 데이터를 저장하는 타입
# - 문법 : [ 데이터 1, 데이터2, ......, 데이터n ]
# - 특징 : 데이터 하나하나를 요소/원소라고 함
#         하나하나의 요소/원소를 식별하기 위해서 인덱싱(Indexing)
# - 순서가 있는 데이터 타입 => 시퀸스 데이터 타입

# 리스트 데이터 생성
# 숫자 10개를 메모리에 저장
no1 = 10
no2 = 25
no3 = 49
no4 = 12
no5 = 94
no6 = 80
no7 = 76
no8 = 35
no9 = 14
no10 = 64

no = [10, 25, 49, 12, 94, 80, 76, 35, 14, 64]
print(f'id(no)    => {id(no)}')
print(f'id(no[0]) => {id(no[0])}')
print(f'id(no[1]) => {id(no[1])}')

# 리스트의 원소/요소 한 개씩 접근하는 방법 => 변수명[인덱스]
# - 왼쪽 => 오른쪽 : 0 ~
# - 오른쪽 => 왼쪽 : -1 ~
# => 슬라이싱 가능

print(no[-3:])

# 짝수번째 인덱스 요소만 출력 => 0 2 4 6 8 10
print('짝수 요소만 출력 :', no[::2])
print('홀수 요소만 출력 :', no[1::2])