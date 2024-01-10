# list의 원소/요소 데이터 변경 및 삭제

# "Merry Christmas"의 문자 하나하나를 리스트로 생성하기
msg = "Merry Christmas"
list = list(msg)
print(list)

# => ' ' 데이터를 '***' 변경하기
list[list.index(' ')] = '***'
print(list)

# 삭제 == > del 데이터 또는 del(데이터)
del list[5]
print({list})