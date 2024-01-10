# 컨프리헨션(Comprehension)
# - List Comprehension, Dict Comprehension, Set Comprehension

# [실습1] aList의 원소 값을 제곱한 값을 원소로 가지는 bList 생성하세요.
aList = [1,2,3,4]
bList = []

# 일반적 for 방식
for a in aList:
    bList.append(a**2)

print(f'aList => {aList}')
print(f'bList => {bList}')

# 컨프리헨션 방식
cList = [ a**2 for a in aList ]
print(f'cList => {cList}')

# [실습2] aList의 원소 값에서 짝수인 데이터만 제곱한 값을 원소로 가지는 bList 생성하세요.
# 일반적 for 방식
bList = []
for a in aList:
    if not a%2:
        bList.append(a**2)

print(f'aList => {aList}')
print(f'bList => {bList}')

# 컨프리헨션 방식
cList = [ a**2 for a in aList if not a%2 ]
print(f'cList => {cList}')

# [실습3] aList의 원소 값 중에서 짝수인 데이터는 제곱, 홀수인 데이터는 그대로 저장한 bList 생성하세요.
cList = [ a**2 if not a%2 in aList else a for a in aList  ]
print(f'cList => {cList}')