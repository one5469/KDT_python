# 전역 변수(Global Variable)와 지역 변수(Local Variable)
# - 함수 내에서 전역 변수 값 변경하고자 하는 경우는 추가 코드 필요
# - 추가 코드 : global 전역 변수명
# -> 주의 : 전역변수 값이 언제든지 함수로 변경이 될 수 있는 상황
#          사용 시에 주의 필요함

# 사용자 정의 함수
def currentDate(year, month, day):
    # year, month, day => 지역 변수
    print(f'Today: {year}/{month:0>2}/{day:0>2}')

def currentDate2(month, day):
    # month, day => 지역 변수
    # year => 전역변수
    # 함수 내에서 전역변부 값을 변경하고자 하는 경우는 global 전역변수명
    global year
    year = year+10
    print(f'Today: {year}/{month:0>2}/{day:0>2}')

# 전역변수
year, month, day = 2024, 1, 8

# 함수 사용 즉 함수 호출
currentDate2(month, day)

# 변수 값 확인 출력
print(f'year : {year}, month : {month}, day : {day}')

# 함수의 변수인 지여 변수는 함수 밖에서 사용 불가
# print(f'week : {week}')