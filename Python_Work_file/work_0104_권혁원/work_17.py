DEBUG_NUM = 0

# 연습문제: 변수 두 개를 다르게 반복하기
if DEBUG_NUM == 1:
    i, j = 2, 5

    while i <= 32 and i > 0:
        print(i, j)
        i *= 2
        j -= 1

# 심사문제: 교통카드 잔액 출력하기
elif DEBUG_NUM == 2:
    card = input('')
    cost = 1350

    if card.isdecimal():
        card = int(card) - cost
        while card > 0:
            print(card)
            card -= cost
    else:
        print("Wrong data type!!")