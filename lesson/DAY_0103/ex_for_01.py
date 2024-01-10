# 1~100 범위에서 2의 배수에 해당하는 정수로 리스트 생성
twos = list(range(2, 101, 2))
print(twos)

# 시퀀스 데이터 타입에서 원소/요소를 하나식 빼서 반복코드 수행 => for in 반복문
strNum = ''
for num in twos:
    strNum = strNum + str(num)
print(strNum)

# 리스트 안에 모든 원소를 str 타입으로 변환해서 저장
for idx in range(len(twos)):
    twos[idx] = str(twos[idx])
print(twos)