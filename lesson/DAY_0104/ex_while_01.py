# 반복문 - 2 while 반복문
# - 반복의 횟수가 정해지지 않은 경우에 사용
# - 반복의 횟수가 정해진 경우에도 사용 가능

# [요청] 사용자로부터 좋아하는 음식명을 입력 받아 주세요.
#       => input()
#       단, Top 5로 가장 좋아 하는 음식 5개만 입력 받으세요.
#       => 사용자의 Top5 음식명 출력
foods = []
for i in range(5):
    food = input(f"좋아하는 음식을 입력하시오. ({5-i}번 남음) ")
    foods.append(food)
print(f'당신이 좋아하는 음식 Top 5 => {foods}')

foods2 = ''
for i in range(5):
    foods2 += input(f"좋아하는 음식을 입력하시오. ({5-i}번 남음) ")
    if i < 4:
        foods2 += ', '
print(f'당신이 좋아하는 음식 Top 5 => {foods2}')

# 기본 while 문법
# while 조건식 :
#   실행코드
#   실행코드

# 타이머 프로그램 만들기 => 다운카운팅 : 10 9 8 7 ... 1
# downCnt = 10
# while downCnt > 0:
#     print(f'다운 카운팅 {downCnt}초')
#     downCnt -= 1
# print()

for downCnt in range(10, 0, -1):
    print(f'다운 카운팅 {downCnt}초')
print()

# 타이머 프로그램 만들기 => 업카운팅 : 1 2 3 4 5 ... 10
# upCnt = 1
# while upCnt <= 10:
#     print(f'업카운팅 {upCnt}초')
#     upCnt += 1

for upCnt in range(1, 11):
    print(f'업카운팅 {upCnt}초')
print()

# [요청] 사용자로부터 좋아하는 음식명을 입력 받아 주세요.
#       => input()
#       단, 사용자가 '끝'이라는 음식명 입력 전까지 입력 받으세요.
#       => 몇 번 입력 받아야 입력이 끝날지 알 수 없음
