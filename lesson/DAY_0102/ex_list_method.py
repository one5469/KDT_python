# 메소드 => 특정 데이터 타입의 전용 함수를 메소드(Method)라고 부름
# - 범용의 함수와 식별하기 위해서 지정한 호칭
# - 사용법 : 데이터.메소드명() 또는 변수명.메소드명()

# List 전용 메소드 살펴보기
# [1] 리스트에 데이터 추가해주는 메소드 => append() 맨 끝에 원소로 추가
nums = []

print(f'nums : {len(nums)}')

nums.append(3)
nums.append('8')
nums.append(True)
print(f'nums : {len(nums)}, {nums}')

# [1] 리스트에 데이터 추가해주는 메소드 => insert(위치인덱스, 데이터) 지정 위치에 추가
nums.insert(0, 2024)
print(f'nums : {len(nums)}, {nums}')

nums.insert(-1, ["ABC", "DEF"])
print(f'nums : {len(nums)}, {nums}')

# 'DEF' 데이터 삭제
del nums[3][1]
print(f'nums : {len(nums)}, {nums}')

# 리스트 안에 모든 원소 삭제해서 빈 리스트 만들기
del nums[0:]
print(f'nums : {len(nums)}, {nums}')

# [2] 리스트 안에 원소/요소 정렬해주는 메소드 => sort() 오름차순 정렬
# - 오름차순 : 작은 데이터 >>> 큰 데이터
nums.append(98)
nums.append(-2)
nums.append(4)
nums.append(0)
nums.append(1.3)

nums.sort()
print(f'nums : {len(nums)}, {nums}')

# 내림차순 : 큰 데이터 >> 작은 데이터 순서로
nums.sort(reverse=1)    # 역순 매개변수값을 True 설정
print(f'nums : {len(nums)}, {nums}')

# [3] 리스트 안에 원소/요소의 현재 위치를 반대로 뒤집어 주는 메소드 => reverse()
# 원소/요소 데이터 값 비교 안 함!! 순서만 변경함
nums.reverse()
print(f'nums : {len(nums)}, {nums}')

# [4] 리스트 안에 원소/요소를 삭제해주는 메소드 => remove()
# - 리스트에서 지정된 값의 원소 삭제
# - 없는 값/데이터 삭제 요청시 Error 발생시킴!!
nums.remove(0)
print(f'nums : {len(nums)}, {nums}')

# [5] 리스트 안에 모든 원소/요소를 삭제해주는 메소드 => clear()
nums.clear()
print(f'nums : {len(nums)}, {nums}')

# [6] 리스트에 원소/요소를 꺼내는 메소드 => pop()
nums.append(10)
nums.append(-3)
nums.append(7)
print(f'nums : {len(nums)}, {nums}')

# 제일 마지막 원소/요소 데이터 꺼내기 => pop()
nums.pop()
print(f'nums : {len(nums)}, {nums}')

# 특정 위치에 원소/요소 데이터 꺼내기 => pop(인덱스)
nums.pop(0)
print(f'nums : {len(nums)}, {nums}')

# [7] 리스트에서 특정 원소/요소 데이터가 몇 개 존재하는지 카운팅해주는 메소드 => count(데이터)
print(nums.count('A'))
print(nums.count(-3))

# [8] 리스트를 확장시키는 메소드 => extend(여러개 데이터 저장한 데이터 타입)
nums.extend([11,22,33])
print(f'nums : {len(nums)}, {nums}')

nums.extend([])
print(f'nums : {len(nums)}, {nums}')

nums.extend("새해 복 많이 받으세요.")
print(f'nums : {len(nums)}, {nums}')

nums.extend(["새해 복 많이 받으세요"])
print(f'nums : {len(nums)}, {nums}')

# nums.extend(2024)     # 시퀀스 또는 반복 가능한 데이터만 가능

# [9] 리스트를 복사해주는 메소드 => 얕은 복사 copy()
nums.append([100, 200])
nums2 = nums.copy()
print(f'nums2 : {nums2}')

# nums에 [-2]번 요소의 데이터를 2024로 변경
nums[-2] = 2024
print(f'nums  : {nums}')
print(f'nums2 : {nums2}')

# nums의 [-1]번 요소의 [0]번 요소의 데이터를 77로 변경
nums[-1][0] = 77
print(f'nums  : {nums}')
print(f'nums2 : {nums2}')