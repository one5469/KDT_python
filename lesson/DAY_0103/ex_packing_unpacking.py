# 팩킹(Packing) & 언팩킹(Unpacking)

# 팩킹(Packing) 방식
msg = "Happy New Year"
msgList = msg.split()
print(msgList[0], msgList[1], msgList[2])

# 언팩킹(Unpacking) 방식
# 데이터 수와 변수 수가 동일해야함
m1, m2, m3 = msg.split()
print(m1, m2, m3)

# 변수를 여러 개 생성하는 경우
age = 12
name = "Hong"
job = '학생'

# 튜플을 언팩킹으로 생성 가능
age1, name1, job1 = 12, 'Hong', '학생' # (12, 'Hong', '학생')

