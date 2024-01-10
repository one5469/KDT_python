# [실습1] 2개의 정수를 입력 받은 후 사칙 연산 수행 결과를 반환하는 기능의 함수를 정의해주세요.
def fourCalc(n1, n2):
    return f'{n1}+{n2}={n1+n2}\n{n1}-{n2}={n1-n2}\n{n1}*{n2}={n1*n2}\n{n1}/{n2}={round(n1/n2, 2)}'

# [실습1] 문자열을 16진수 코드값으로 변환 후 반환하는 함수를 정의해주세요.
def getCode(message):
    result = ''
    for s in message:
        result += hex(ord(s)) + ' '
    return result

print(fourCalc(10, 3))
print()
print(getCode('Ace'))