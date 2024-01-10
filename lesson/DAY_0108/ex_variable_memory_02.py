# 참조형 변수 => 데이터의 주소 저장
# 저장된 데이터와 변수 타입 관계
num1 =[]
print(f'num1 => {id(num1)}, {type(num1)}')


num2 = [11,22.]
print(f'num2 => {id(num2)}, {type(num2)}')
print(f'num2[0] => {id(num2[0])}, {type(num2[0])}')
print(f'num2[1] => {id(num2[1])}, {type(num2[1])}')
print()

num = 'Happy'
print(f'num => {id(num)}, {type(num)}')

num2[0] = 100
print(f'num2 => {id(num2)}, {type(num2)}')
print(f'num2[0] => {id(num2[0])}, {type(num2[0])}')
print()

# 리스트를 다른 리스트로 새로 변경
num1 = num2
print(f'num1 => {id(num1)}, {type(num1)}')
print(f'num2 => {id(num2)}, {type(num2)}')

num1[0] = 77
print(f'num1 => {id(num1)}, {type(num1)}')
print(f'num2 => {id(num2)}, {type(num2)}')