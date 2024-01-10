# 문제 1
hometown = '용인'
bloodtype = 'O'
season = 'Autumn'
height = 168
phone = '010-3118-5469'
country = 'Republic of Korea'

# 문제 2
mbti = 'INFP'
blood = 'A'
gender = 'M'
height = 171.7
weight = 77

# 여러데이터 출력 방식
print("[ 신상 정보 ]")
print('MBTI : ', mbti, '\t혈액형 : ', blood, '\t성별 : ', gender, sep='')
print('몸무게 : ', weight, '\t키 : ', height, sep='')
# 서식지정자 출력 방식
print("[ 신상 정보 ]")
print('MBTI : %s\t혈액형 : %s\t성별 : %s' %(mbti, blood, gender))
print('몸무게 : %d\t키 : %.1f' %(weight, height))
# F-스트링 출력 방식
print("[ 신상 정보 ]")
print(f'MBTI : {mbti}\t혈액형 : {blood}\t성별 : {gender}')
print(f'몸무게 : {weight}\t키 : {height}')
print()

# 문제 3
# 3-1
data1 = 50
data2 = 0.91
data3 = 'Winter'
data4 = False

print(f"데이터 {data1}\t\t=> ", type(data1), '타입')
print(f"데이터 {data2}\t\t=> ", type(data2), '타입')
print(f"데이터 {data3}\t=> ", type(data3), '타입')
print(f"데이터 {data4}\t\t=> ", type(data4), '타입')

# 3-2
answer1 = input("좋아하는 계절은? ")
print(f"당신은 {answer1}을 좋아하는 군요!")

answer2 = input("봄은 영어로? ")
print("봄은 Spring입니다.")  # 이게 맞는 것 같습니다.

# 문제 4
'''
    정답 : 힙 영역, 스택 영역
'''

# 문제 5
# 5-1
'''
    정답 : int, float, str, bool
'''

# 5-2
'''
    정답 : 이진수, 8진수, 16진수
'''

# 문제 6
horizonal = int(input("[질문] 직육면체 가로길이(cm) : "))
vertical = int(input("[질문] 직육면체 세로길이(cm) : "))
height = int(input("[질문] 직육면체 높이길이(cm) : "))
area = (horizonal * vertical) * 2 + (horizonal * height) * 2 + (vertical * height) * 2
volumn = horizonal * vertical * height
print(f"[결과] 직사각형 넓이 : {area}\n\t  직사각형 부피 : {volumn}")