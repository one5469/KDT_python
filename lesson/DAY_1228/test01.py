# [실습 1] 2개 숫자 데이털 입력 받은 후 2개의 값을 산술 연산 결과를 출력해 주세요.
num1 = int(input('첫번째 숫자: '))
num2 = int(input('두번째 숫자: '))

print(f'{num1} + {num2}\t= {num1+num2}')
print(f'{num1} - {num2}\t= {num1-num2}')
print(f'{num1} * {num2}\t= {num1*num2}')
print(f'{num1} / {num2}\t= {num1/num2}')
print(f'{num1} % {num2}\t= {num1%num2}')
print(f'{num1} // {num2}\t= {num1//num2}')
print()

# [실습 2] [실습 1]에서 입력 받은 숫자 데이터를 활용하여 비교 연산 결과를 출력하세요.
print(f'{num1} > {num2}\t=> {num1>num2}')
print(f'{num1} < {num2}\t=> {num1<num2}')
print(f'{num1} >= {num2}\t=> {num1>=num2}')
print(f'{num1} <= {num2}\t=> {num1<=num2}')
print(f'{num1} == {num2}\t=> {num1==num2}')
print(f'{num1} != {num2}\t=> {num1!=num2}')
print()

# [실습 3] [실습 1]에서 입력 받은 숫자 데이터를 활용하여 최대값과 최소값을 추가로 입력 받은 후 논리연산 결과 출력하세요.
max = int(input('최대값: '))
min = int(input('최소값: '))

print(f'{num1} > {num2} and {num1} > {max}\t=> {num1 > num2 and num1 > max}')
print(f'{num1} > {num2} and {num1} > {min}\t=> {num1 > num2 and num1 > min}')
print(f'{num1} > {num2} or {num1} > {max}\t=> {num1 > num2 or num1 > max}')
print(f'{num1} > {num2} or {num1} > {min}\t=> {num1 > num2 or num1 > min}')
print(f'not {num1} => {not num1}')