# 딕셔너리 만들기
lux = {'health':490, 'mana':334, 'melee':550, 'armor':18.72}
print(lux) # {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}

# 키 이름 중복
lux = {'health':490, 'health':800, 'mana':334, 'melee':550, 'armor':18.72}
print(lux['health']) # 800 : 키가 중복되면 가장 뒤에 있는 값만 사용함
# 중복되는 키는 저장되지 않음
print(lux) # {'health': 800, 'mana': 334, 'melee': 550, 'armor': 18.72}

# 딕셔너리 키의 자료형
# 키에는 리스트와 딕셔너리를 사용할 수 없음
x = {100:'hundred', False:0, 3.5:[3.5, 3.5]}
print(x) # {100: 'hundred', False: 0, 3.5: [3.5, 3.5]}

# 빈 딕셔너리 만들기
x = {}
print(x) # {}

# dict로 딕셔너리 만들기
lux1 = dict(health=490, mana=334, melee=550, armor=18.72)
lux2 = dict([('health', 490), ('mana', 334), ('melee', 550), ('armor', 18.72)])
lux3 = dict({'health':490, 'health':800, 'mana':334, 'melee':550, 'armor':18.72})

# 딕셔너리 키 접근
print(lux1['health'])    # 490
print(lux1['armor'])     # 18.72

# 딕셔너리 값 할당
lux1['health'] = 2037
print(lux1) # {'health': 2037, 'mana': 334, 'melee': 550, 'armor': 18.72}

# 딕셔너리 키와 값 추가
lux1['mana_regen'] = 3.28
print(lux1) # {'health': 2037, 'mana': 334, 'melee': 550, 'armor': 18.72, 'mana_regen': 3.28}

# 딕셔너리에 키가 있는지 확인
print('health' in lux1) # True
print('attack speed' in lux1) # False

# 딕셔너리 키 개수 구하기
print(len(lux1)) # 5

# 연습문제 : 딕셔너리에 게임 캐릭터 능력치 저장하기
# 캐릭터의 체력(health)와 이동 속도(movement speed) 출력
camille = {
    'health' : 575.5,
    'health_regen' : 1.7,
    'mana' : 338.8,
    'mana_regen' : 1.63,
    'melee' : 125,
    'attack_damage' : 60,
    'attack_speed' : 0.625,
    'armor' : 26,
    'magic_resistance' : 32.1,
    'movement_speed' : 340
}

print(camille['health'])
print(camille['movement_speed'])

# 심사문제 : 딕셔너리에 게임 캐릭터 능력치 저장하기
# 능력치를 입력받아 딕셔너리에 저장
# 반복문이랑 내장함수 안쓰고..
# 어캐하노
spec = input('').split()
values = input('').split()

champ = dict()