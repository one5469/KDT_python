# 나의 프로그램 - 계산기
# [계산기]
# 0. 입력
# 1. 덧셈
# 2. 뺄셈
# 3. 곱셉
# 4. 나눗셈
# 5. 종료

# 사용자 정의 함수
# 함수 기능 : 연산결과 리스트에서 검색어에 해당하는 데이터만 출력
# 함수 이름 : searchResult
# 매개 변수 : search
# 함수 결과 : none
def searchResult(search):
    for calc in calcList:
        if search in calc:
            print(calc)


calcList = []

while True:
    print('[나의 계산기]')
    print('0. 입력')
    print('1. 덧셈')
    print('2. 뺄셈')
    print('3. 곱셉')
    print('4. 나눗셈')
    print('5. 기록보기')
    print('6. 종료')

    choice= input("메뉴 선택 : ")
    if choice.isdecimal():
        if choice == '0':
            data = input("2개 정수(예: 10 20) : ")
            n1, n2 = list(map(int, data.split()))
        elif choice == '1':
            calcList.append(f'{n1} + {n2} = {n1 + n2}')
            print(f'{n1} + {n2} = {n1 + n2}\n')
        elif choice == '2':
            calcList.append(f'{n1} - {n2} = {n1 - n2}')
            print(f'{n1} - {n2} = {n1 - n2}\n')
        elif choice == '3':
            calcList.append(f'{n1} * {n2} = {n1 * n2}')
            print(f'{n1} * {n2} = {n1 * n2}\n')
        elif choice == '4':
            calcList.append(f'{n1} / {n2} = {n1 / n2 if n2 else "0으로 나눌 수 없습니다."}')
            print(f'{n1} / {n2} = {n1 / n2 if n2 else "0으로 나눌 수 없습니다."}\n')
        elif choice == '5':
            for c in calcList:
                print(c)
        elif choice == '6':
            print("프로그램 종료합니다.")
            break
        else:
            print("메뉴 1 ~ 6까지 선택 가능합니다.")
    else:
        print("없는 메뉴입니다.")