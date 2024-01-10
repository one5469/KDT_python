# str 데이터 타입 연산

# 산술 연산 => 덧셈, 뺄셈, 곱셉, 나눗셈....

msg1 = 'Good'
msg2 = 'Happy'

# 덧셈 연산
# str + str만 가능
print(f'msg1 + msg2 => {msg1 + msg2}')
# print(f'msg1 + 10 => {msg1 + 10}')

# 뺄셈 연산
# 미지원
#print(f'msg1 - msg2 => {msg1-msg2}')

# 곱셉 연산
# str * int 또는 int * str ==> str 데이터를 int만큼 반복 연결
# print(f'msg1 * msg2 => {msg1 * msg2}')
print(f'msg1 * 10 => {msg1 * 10}')
print(f'3 * msg2 => {3 * msg2}')

# 비교 연산 => >, <, >=, <=, ==, !=
# - str안에 원소/요소 단위로 비교 됨. 즉, 코드값으로 비교
print(f'"H" > "I" => {"H">"I"}, {ord("H")}, {ord("I")}')
print(f'"H" > "h" => {"H">"h"}, {ord("H")}, {ord("h")}')
# 동일한 인덱스에 있는 요소의 코드값으로 비교
print(f'"Ha" > "HA" => {"Ha">"HA"}')
print(f'"ha" > "Ha" => {"ha">"Ha"}')
print(f'"ha" > "Hb" => {"ha">"Hb"}')

# 논리 연산 => and, or, not
# - not 문자열
# str => bool 관계
# - 요소/원소가 0개인 경우     => False
# - 요소/원소가 1개 이상인 경우 => True
print( f'not "Happy" => {not "Happy"}')
print( f'not ""      => {not ""}')

# 멤버 연산자 => 원소/요소가 있는 데이터 타입의 경우 사용
# - 요소 in 데이터       : 요소가 데이터에 포함되어 있는 경우 True
# - 요소 not in 데이터   : 요소가 데이터에 미포함되어 있는 경우 True
print(f'"H" in "Happy" : {"H" in "Happy"}')
print(f'"h" in "Happy" : {"h" in "Happy"}')

print(f'"H" not in "Happy" : {"H" not in "Happy"}')
print(f'"h" not in "Happy" : {"h" not in "Happy"}')

print(f'"1" in "1357" : {"1" in "1357"}')
print(f'"2" in "1357" : {"2" in "1357"}')