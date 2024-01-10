# 단순 조건문 ===> (1) 조건이 True인 경우만 처리하는 조건문
# if 조건:
#   실행코드
#   실행코드
#   실행코드

# 단순 조건문 ===> (2) 조건이 True인 경우 / False인 경우 처리하는 조건문
# if 조건:
#   실행코드    T
#   실행코드
#   실행코드
# else:
#   실행코드    F
#   실행코드
#   실행코드

# 복잡 조건문 ===> (3) 조건이 여러개인 경우의 조건문 : 다중 조건문
# if 조건:
#   실행코드
#   실행코드
# elif 조건:
#   실행코드
#   실행코드
# elif 조건:
#   실행코드
#   실행코드
# else:
#   실행코드

# 복잡 조건문 ===> (4) 조건문 안에 조건문이 존재하는 조건문 : 중첩 조건문
# if 조건:
#   실행코드
#   실행코드
#   if 조건:
#       실행코드
#       실행코드
#   else:
#       실행코드
#       실행코드
# else:
#   실행코드

# 조건부 표현식 ===> (5) 1줄 조건문
# 조건 True인 경우 실행될 코드 if 조건 else 조건 False일 때 실행 코드

# 홀수 & 짝수 식별 후 결과 출력하는 코드
# 방법 (1) 단순 조건문
num = 27
if num%2:
    print(f'{num} 홀수')
else:
    print(f'{num} 짝수')

# 방법 (2) 조건부 표현식
print(f'{num} 홀수') if num%2 else print(f'{num} 짝수')

result = '홀수' if num%2 else "짝수"

# 양수, 0, 음수 식별 후 결과 출력
if num>0:
    print(f'{num} 양수')
elif num<0:
    print(f'{num} 음수')
else:
    print(f'{num} 0')

result = '양수' if num>0 else '음수' if num<0 else '0'
print(f'{num} result')

