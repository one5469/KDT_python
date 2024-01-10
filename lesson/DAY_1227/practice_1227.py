# ap = 102
# skill_damage = ap * 0.6 + 225
#
# print(skill_damage)
#
# a = 50
# b = 100
# c = None
#
# print(a)
# print(b)
# print(c)

# kor = int(input("국어 점수를 입력하시오. "))
# eng = int(input("영어 점수를 입력하시오. "))
# math = int(input("수학 점수를 입력하시오. "))
# sci = int(input("과학 점수를 입력하시오. "))
# kor, eng, math, sci = map(int, input().split())
# avg = (kor + eng + math + sci) // 4
# print(avg)

year, month, day, hour, minute, second = input().split()

print(year, month, day, sep='-', end='T')
print(hour, minute, second, sep=':')