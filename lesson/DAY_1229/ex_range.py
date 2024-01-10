# range() 내장함수
# - 숫자의 범위를 생성해주는 함수
# - 반환값/결과값/리턴값 : range 타입
# - 범위에 포함되는 숫자 데이터 는 원소/요소라고 함 => 인덱싱

# 1 ~ 20으로 구성된 정수 데이터 생성
nums = range(20)

print(f'nums     => {nums}, {type(nums)}')
print(f'nums[0]  => {nums[0]}, {type(nums[0])}')
print(f'nums[-1] => {nums[-1]}, {type(nums[-1])}')

print(f'len(nums) = {len(nums)}')

# 앞부분 5개 원소까지만 추철
print(nums[:5])

# range ==> list 형 변환하기 => list(데이터)
print(f'list(nums) => {list(nums)}')

# 1~100으로 구성된 정수 리스트 생성
toHundred = list(range(1, 101))
print(toHundred)

# range(시작값, 끝값)
# - 시작값 => 기본 : 0             range(10)  => 0~9
# - 시작값 => 기본 : 1             range(1,10)=> 1~9
# - 시작값 => 기본 : 5             range(5,10)=> 1~9


# range(시작값, 끝값, 증감)
# 시작값 => 기본 : 0, 증감 : 1      range(10)  => 0,1,2,3,4,5,6,7,8,9
# 시작값 => 기본 : 1, 증감 : 1      range(1,10)=> 1,2,3,4,5,6,7,8,9
# 시작값 => 기본 : 1, 증감 : 2      range(1,10,2)=> 1,3,5,7,9

# 1~30 범위에서 3의 배수만으로 구성된 리스트 생성
threes = list(range(3,31,3))
print(threes)