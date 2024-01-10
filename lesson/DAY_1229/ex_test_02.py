# [실습 1] 임의의 숫자 데이터 7개를 저장한 리스트를 생성
#         리스트에 원소를 화면에 한 줄에 한개씩 출력하세요
list = [1,2,3,4,5,6,7]

print(f'list[0] : {list[0]}')
print(f'list[1] : {list[1]}')
print(f'list[2] : {list[2]}')
print(f'list[3] : {list[3]}')
print(f'list[4] : {list[4]}')
print(f'list[5] : {list[5]}')
print(f'list[6] : {list[6]}')

# [실습 2] 아래 리스트에서 원소를 화면에 한 줄에 한개씩 출력하세요.
datas = [   [10, 20], [40, 50], [70, 80, 90]    ]

print(f'datas[0]    : {datas[0]}')
print(f'datas[0][0] : {datas[0][0]}')
print(f'datas[0][1] : {datas[0][1]}')
print(f'datas[1]    : {datas[1]}')
print(f'datas[1][0] : {datas[1][0]}')
print(f'datas[1][1] : {datas[1][1]}')
print(f'datas[2]    : {datas[2]}')
print(f'datas[2][0] : {datas[2][0]}')
print(f'datas[2][1] : {datas[2][1]}')
print(f'datas[2][2] : {datas[2][2]}')

# [실습 3] 좋아하는 계절과 월(month)를 입력 받은 후 각각 변수에 저장하세요.
#         변수명은 season, month입니다.
msg = input("좋아하는 계절과 월은? (공백으로 구분) : ").split()
season = msg[0]
season = msg[1]

# [실습 4] 1~20으로 구성된 정수 리스트를 생성하세요.
#         * 3의 배수 인덱스에 해당하는 정수만 출력하세요.
#         * 3의 배수 인덱스에 해당하는 정수의 합계를 출력하세요.
nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

print(f'3의 배수       : {nums[3::3]}')
print(f'3의 배수 합계   : {nums[3::3][0]+nums[3::3][1]+nums[3::3][2]+nums[3::3][3]+nums[3::3][4]+nums[3::3][5]}')