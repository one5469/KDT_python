'''
    타입 캐스팅(Type Casting)
    - 정수 => 실수,     정수 => 문자열,      정수 => 논리
    다른 데이터 타입으로 변환하는 것
    - 함수 : 데이터 타입명()
        => 정수 형변환해주는 함수     int()
        => 실수 형변환해주는 함수     float()
        => 문자열 형변환해주는 함수    str()
        => 논리 형변환해주는 함수     bool()
'''

# int 데이터 타입으로 형변환
# int( 데이터 - 10진수 숫자 )
print( type(int('200')) )
# value = int('200')
# print(type(value))

# print( type(int('200Day')) ) => 오류 : 부적절한 데이터 타입
# print( type(int('200.4')) ) => 오류 : 부적절한 데이터 타입

# float ===> int : 소수점 이하 데이터 손실 발생
print( type(int(200.4)), int(200))

# bool ===> int
# => 0, 1 => False, True
print( type(int(False)), int(False), type(False))
print( type(int(True)), int(True), type(True))

# float 데이터 타입으로 형변환
# str ==> float('0~9, .')
print( type(float('3.5')), float('3.5'))
print( type(float('35')), float('35'))
print( type(float('-123')), float('-123'))
#print( type(float('0x123')), float('0x123'))

# int ===> float
print( type(float(45)), float(45))
print( type(float(-9)), float(-9))

# bool ===> float
print( type(float(False)), float(False))
print( type(float(True)), float(True))