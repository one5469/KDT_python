# [실습1]
# 좋아하는 정수를 하나 저장한 후 짝수이면 '--은 짝수입니다.'
# 홀수면 '--은 홀수입니다.'를 출력
myNum = 71

# 숫자 % 2 == 0 : 짝수,     숫자 % 2 == 1 : 홀수
if myNum % 2 == 0 :
    print(f'{myNum} 짝수입니다.')
else :
    print(f'{myNum} 홀수입니다.')

# [실습2]
# 좋아하는 정수를 하나 저장한 후 양수면 '--은 양수입니다.'
# 음수면 '--은 음수입니다.'
# 0이면 '--은 0입니다.' 출력해주세요

# 다중 조건문 => 조건문이 2개 이상 되는 경우
if myNum > 0 :
    print(f'{myNum} 양수입니다.')
elif myNum < 0 :
    print(f'{myNum} 음수입니다.')
else:
    print(f'{myNum} 0입니다.')

# 중첩 조건문 => 조건문 안에 조건문이 존재하는 경우
if myNum == 0 :
    print(f'{myNum} 0입니다.')
else:
    if myNum > 0:
        print(f'{myNum} 양수입니다.')
    else:
        print(f'{myNum} 음수입니다.')

if myNum :
    if myNum > 0:
        print(f'{myNum} 양수입니다.')
    else:
        print(f'{myNum} 음수입니다.')
else:
    print(f'{myNum} 0입니다.')