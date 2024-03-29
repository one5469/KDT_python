'''
수치 데이터 살펴보기
- 정수 => class int       : 양수, 0, 음수
- 실수 => class float     : 소수점 존재
- 복소수 => class complex
'''

# [실습] 2개 정수를 입력 받기
# -> input() 함수 2개 사용
# -> str => int 타입 캐스팅
print("정수 2개 각각 입력")
num1 = input("")
num2 = input("")

num1 = int(num1)
num2 = int(num2)

# 비교 연산 결과 출력
# [출력] 10 > 3 => True
print(f'{num1} > {num2} => {num1>num2}')
print(f'{num1} < {num2} => {num1<num2}')
print(f'{num1} >= {num2} => {num1>=num2}')
print(f'{num1} <= {num2} => {num1<=num2}')
print(f'{num1} == {num2} => {num1==num2}')
print(f'{num1} != {num2} => {num1!=num2}')

