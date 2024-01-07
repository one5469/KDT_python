# 16장
# ----------------------------------------------------
# 연습문제 : 리스트의 요소에 10을 곱해서 출력하기
x = [49, -17, 25, 102, 8, 62, 21]

for i in x:
    print(i * 10, end=' ')
print()


# 심사문제: 구구단 출력하기
num = (input(''))
if num.isdigit():
    num = int(num)
    for i in range(1, 10):
        print(f'{num} * {i} = {num*i}')
else:
    print("?")
print()


# 19장
# ----------------------------------------------------
# 대각선으로 별 출력하기
for i in range(5):
    print(' ' * i + '*')
print()


# 연습문제: 역삼각형 모양으로 별 출력하기
# 교재 정답 => 코드 길어서 치기 싫음 / O(n^2)
for i in range(5):
    for j in range(5):
        if j < i:
            print(' ', end='')
        else:
            print('*', end='')
    print()
print()

# for문 한번만
for i in range(5, 0, -1):
    star = '*' * i
    print(f'{star:>5}')


# 심사문제: 산 모양으로 출력하기
height = input('')

if height.isdigit():
    height = int(height)
    for i in range(0, height):
        numStar = i*2       # 출력되야 할 '*'의 개수
        numSpace = height - (i+1)   # 출력되야 할 한쪽 공백의 개수
        mountain = (' '*numSpace) + ('*'+'*'*(numStar)) + (' '*numSpace)    # 문자열 합성
        print(mountain)
else:
    print("?")
print()


# 22장
# ----------------------------------------------------
# 연습문제: 리스트에서 특정 요소만 뽑아내기
a = ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'hotel', 'india']

b = [ e for e in a if len(e) == 5 ]

print(b)
print()


# 심사문제: 2의 거듭제곱 리스트 생성하기
nums = input('').split()    # 표준 입력

# 입력 형식 판별
if nums[0].isdecimal() and nums[1].isdecimal():
    nums = [ int(n) for n in nums]
    if nums[0] < nums[1]:   # 숫자 대소 비교
        array = [ 2**n for n in range(nums[0], nums[1]+1) ]
        array.remove(array[-2])
        array.remove(array[1])
        print(array)
    else:
        print("First integer MUST be smaller than second integer!!")
else:
    print("Unacceptable input type!!")
