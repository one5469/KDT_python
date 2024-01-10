# 반복문 - 2 while 반복문
# - 반복의 횟수 정해지지 않은 경우

# [요청] 사용자가 'x' 입력 전까지 입력바은 데이터 저장해 주세요.
# => 몇 번 입력할지 알 수 없음 ==> 무한히 입력 받기
# => 종료 조건 ==> 사용자가 'x' 입력
while True:
    data = input("저장하고 싶은 데이터 입력 ( 종료 x ) : ")
    # 종료 검사 => break ; 키워드가 있는 부분에서 바로 반복 종료, 아래 코드 실행 안됨
    # if data == 'x' or data == 'X':
    if data in ('x', 'X'):
        break
    print("OK")

print("프로그램 종료")

# [요청] 사용자로부터 x/X 입력 전까지 계속 정수를 입력
#       입력 받은 정수 만큼 알파벳을 출력
# [예시] 출력 원하는 알파벳 수 입력 : 5
#        abced
#        출력 원하는 알파벳 수 입력 : 1
#        a
#        출력 원하는 알파벳 수 입력 : 10
#        abcdefghij
#        출력 원하는 알파벳 수 입력 : 27
#        abcdefghijklmnopqrstuvwxyz 종료
#        출력 원하는 알파벳 수 입력 : 1
#        a
#        출력 원하는 알파벳 수 입력 : x
#        종료
alpha = 'abcdefghijklmnopqrstuvwxyz'

while True:
    num = input("출력 원하는 알파벳 수 입력 : ")

    if num in ('x', 'X'): break
    elif not num.isdecimal():
        pass
    else:
        num = int(num)
        for i in range(ord('a'), ord('a')+num):
            print(chr(i), end='')
            if i == ord('z'):
                print(' 종료')
                break

print("--- 프로그램 종료 ---")

# isEnd = False
# for n in range(100):
#     print(f'out -> {n}')
#     if isEnd:
#         print("프로그램을 종료합니다.")
#         break
#
#     for n2 in range(100):
#         if n2>10:
#             isEnd = True
#             break
#         print(f'in -> {n2}')

# [요청] 내부에 반복문에서 데이터가 10초과되면 프로그램 종료
outNum = 1
isEnd = False
while outNum <= 100 and not isEnd:
    print(f'outNum => {outNum}')

    # 내부 while
    inNum = 1
    while inNum <= 100:
        if inNum > 10:
            print("내부 while 종료")
            isEnd = True
            break
        print(f'inNum => {inNum} ===> [{outNum}번째]')
        inNum += 1

    outNum += 1