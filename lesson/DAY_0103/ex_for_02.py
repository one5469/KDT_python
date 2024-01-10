# 반복문 => for in 반복문
# - 여러 개의 데이터를 가지고 있는 데이터에서 한 개씩 원소/요소를 읽어와줌
# for 요소저장변수 in 여러 개 데이터 가진 타입:
#   요소/원소 반복할 코드
#   요소/원소 반복할 코드

msg = "Happy New Year 2024! Good Luck"

# msg를 구성하는 문자 한 줄에 한개씩 화면에 출력해주세요
for e in msg:
    print(e)

# [실습1] 'Hello Wolrd' 100번 출력
for cnt in range(100):
    print('Hello Wolrd!')

# [실습2] 좋아하는 음식명을 리스트에 저장하기 (단, 10개 )
foods = ['황금올리브치킨', '뼈해장국', '장충동왕족발보쌈', '화이트하임', '돼지국밥', '제육볶음', '안심스테이크', '대방어']

for cnt in foods:
    print(cnt)