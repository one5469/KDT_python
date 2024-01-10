DEBUG_NUM = int(input("Choose your solution : "))

# 29장
# 연습문제: 몫과 나머지를 구하는 함수 만들기
if DEBUG_NUM == 1:
    x, y = 10, 3

    def get_quotient_remainder(x, y):
        return x//y, x%y

    quotient, remainder = get_quotient_remainder(x, y)
    print(f'몫: {quotient}, 나머지: {remainder}')

# 심사문제: 사칙 연산 함수 만들기
if DEBUG_NUM == 2:
    x, y = map(str, input().split())

    def calc(x, y):
        return x + y, x - y, x * y, x / y

    if x.isdecimal() and y.isdecimal():
        x, y = int(x), int(y)

        a, s, m, d =calc(x, y)
        print(f'덧셈: {a}, 뺄샘: {s}, 곱셈: {m}, 나눗셈: {d}')

# 30장
# 연습문제: 가장 높은 점수를 구하는 함수 만들기
if DEBUG_NUM == 3:
    kor, eng, math, sci = 100, 86, 81, 91

    def get_max_score(*subject):
        return max(*subject)

    max_score = get_max_score(kor, eng, math, sci)
    print(f'높은 점수: {max_score}')

    max_score = get_max_score(eng, sci)
    print(f'높은 점수: {max_score}')

# 심사문제: 가장 낮은 점수, 높은 점수와 평균 점수를 구하는 함수 만들기
if DEBUG_NUM == 4:
    kor, eng, math, sci = map(int, input().split())

    def get_min_max_score(*subject):
        return min(*subject), max(*subject)

    def get_avergage(**subject):
        return sum(subject.values()) / len(subject)

    min_score, max_score = get_min_max_score(kor, eng, math, sci)
    avergage_score = get_avergage(kor=kor, eng=eng, math=math, sci=sci)
    print(f'낮은 점수: {min_score:.2f}, 높은 점수: {max_score:.2f}, 평균 점수: {avergage_score:.2f}')

    min_score, max_score = get_min_max_score(eng, sci)
    avergage_score = get_avergage(eng=eng, sci=sci)
    print(f'낮은 점수: {min_score:.2f}, 높은 점수: {max_score:.2f}, 평균 점수: {avergage_score:.2f}')