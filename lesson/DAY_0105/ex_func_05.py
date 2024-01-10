# 다양한 함수의 형태 - (4) 매개변수가 존재하지 않는 형태
# - 함수에게 전달되는 데이터
# - 함수 생성 문법
#   def 함수 이름( ):
#       조건 코드와 return 결과값
#       실행코드
#       실행코드
#       return 결과값

# 함수기능 : 인사 메시지 출력 기능
# 함수이름 : welcome
# 매개변수 : 없음
# 반환값  : 없음
def welcome():
    print("반갑네!")

welcome()

# 함수기능 : 프로그램 정보 출력 기능
# 함수이름 : printInfo
# 매개변수 : 없음
# 반환값  : str
def printInfo():
    return "MYGAME VERSION 1.0\nDEVELOPER KK\nEMAIL:master@game.com"

# 함수 사용 즉, 호출
print(printInfo())