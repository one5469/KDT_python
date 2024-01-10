# 다양한 함수의 형태 - (3) return 키워드
# - 함수 호출한 곳으로 돌아가게 하는 기능
#   결과값이 함께 있다면 결과값을 가지고 돌아감
#
# - 함수 생성 문법
#   def 함수 이름(매개변수1, 매개변수2, ..., 매개변수n):
#       조건 코드와 return 결과값
#       실행코드
#       실행코드
#       return 결과값

# 함수기능 : 팩토리얼을 계산 후 계산 결과를 반환해주는 기능
# 함수이름 : factorial
# 매개변수 : x
# 반환값  : 계산 과정
def factorial2(x):
    if x == 0:
        return 1    # 즉시 함수 종료 후 호출한 곳으로 반환
    elif x <= 2:
        return x
    else:
        return x * factorial2(x-1)