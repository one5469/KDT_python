# 숫자 데이터 관련 내장 함수들 살펴보기

# 내장 함수 => 빌트인함수, 기본으로 제공되는 함수

# 절대값 반환하는 내장함수 => abs(숫자 데이터)
num = 3

print(f'{num} 절대값 : {abs(num)}')

num = -3

print(f'{num} 절대값 : {abs(num)}')

# 실수값에서 소수점 이하 자릿수 처리해주는 내장함수 => round(실수데이터, 소수점 이하 자리숫자)
# 지정된 자릿수 바로 뒤에 값이 5이상이면 반올림
num = 1.23456789

print(f'{num} => {round(num, 1)}')
print(f'{num} => {round(num, 3)}')
print(f'{num} => {round(num)}')

num = 1.56789
print(f'{num} => {round(num)}')

# 가장 큰 수 / 가장 작은 수 찾아주는 내장함수 => max()/min()
print(f'max(1,2,3) => {max(1,2,3)}')
print(f'max(9,0,-3) => {max(9,0,-3)}')

print(f'min(1,2,3) => {min(1,2,3)}')
print(f'min(9,0,-3) => {min(9,0,-3)}')

# 거듭제곱 계산해주는 내장함수 => pow()
print(f'pow(2,3) => {pow(2, 3)}')
print(f'pow(2,8) => {pow(2, 8)}')

# 숫자 표현 방식으로 변환 내장함수
# - 16진수로 변환 내장함수   hex(정수) => 0x숫자 => str
# - 8진수로 변환 내장함수    oct(정수) => 0o숫자 => str
# - 2진수로 변환 내장함수    bin(정수) => 0b숫자 => str
num = 72
numHex = hex(num)
numOct = oct(num)
numBin = bin(num)

print(f'{num}의 16진수 {numHex}, 8진수 {numOct}, 2진수 {numBin}')