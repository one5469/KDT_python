# 전역 변수(Global Variable)와 지역 변수(Local Variable)
# - 함수 내에서 전역 변수 값 변경하고자 하는 경우는 추가 코드 필요
# - 추가 코드 : global 전역 변수명
# -> 주의 : 전역변수 값이 언제든지 함수로 변경이 될 수 있는 상황
#          사용 시에 주의 필요함

# 사용자 정의 함수
def currentDate(today):
    # todays => 년, 월, 일을 담고 있는 데이터 타입
    print(f'Today: {today[0]}/{today[1]:0>2}/{today[2]:0>2}')

# 전역변수
year, month, day = 2024, 1, 8
todayList = [year, month, day]

# 함수 사용 즉 함수 호출
currentDate(todayList)

# 변수 값 확인 출력
print(f'year : {year}, month : {month}, day : {day}')

# 함수의 변수인 지여 변수는 함수 밖에서 사용 불가
# print(f'week : {week}')