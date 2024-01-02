# 연습문제: if 조건문 사용하기
x = 5
if x != 10:
    print('ok')

# 심사문제: 온라인 할인 쿠폰 시스템 만들기
# 야매로 만들기 (if만 사용, 하드코딩)
cost = int(input(''))
coupon = input('')

if coupon == 'Cash3000':
    print(cost - 3000)

if coupon == 'Cash5000':
    print(cost - 5000)

# 제대로 만들기
# 가격과 쿠폰 입력 받기
cost = input('')
coupon = input('')
discount = 0

# 자료형 형식 확인
if not cost.isdigit():
    print("적합하지 않은 입력 형식입니다.")
elif len(cost) < 1:
    print("가격 혹은 쿠폰을 입력하지 않았습니다.")
else:
    cost = int(cost)
    if len(coupon) > 0 and coupon[:4] == 'Cash':
        discount = int(coupon[-4:])

print(cost - discount)

