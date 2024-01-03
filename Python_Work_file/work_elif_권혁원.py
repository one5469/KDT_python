# 연습문제: if, elif, else 모두 사용하기
x = int(input())

if x >= 11 and x <= 20:
    print('11~20')
elif x >= 21 and x <= 30:
    print('21~30')
else:
    print("아무것도 해당하지 않음")

# 심사문제: 교통카드 시스템 만들기
age = int(input())
balance = 9000

if age < 7:
    print("그런 나이는 존재하지 않아")
elif age >= 7 and age <= 12:
    print(9000 - 650)
elif age >= 13 and age <= 18:
    print(9000 - 1050)
else:
    print(9000 - 1250)