# str 데이터 타입 전용의 함수 즉 메소드(Method) 살펴 보기
# - 메소드(Method)
#   특정 데이터 타입에서만 사용 가능한 함수를 의미
# - 사용방법
#   변수명.메소드명() ==> msg = "Good"
#                      msg.메소드명()
#   데이터.메소드명() ==> "Good".메소드명()

# str을 대문자로 변환 ==> upper()
print("Good".upper())
# str을 소문자로 변환 ==> lower()
print("Good".lower())

# str이 모두 대문자인지 검사 후 결과 반환 => isupper() 메소드
print("Good".isupper())

# str이 모두 소문자인지 검사 후 결과 반환 => islower() 메소드
print("Good".islower())

# str이 0~9로 구성되어 있는지 검사 후 결과 반환 => isdecimal() 메소드
print("Good".isdecimal(), '012'.isdecimal(), '-9'.isdecimal())

# str이 문자로만 구성되어 있는지 검사 후 결과 반환 => isalpha() 메소드
print("Good".isalpha(), "하하하".isalpha(), '五'.isalpha())
print("カタカナ".isalpha(),  'русскийалфавит'.isalpha())
print('Good2024'.isalpha())
print('----'.isalpha())

# str이 문자, 숫자로만 구성되어 있는지 검사 후 결과 반환 => isalnum() 메소드
print("Good2024".isalnum(), 'nice_'.isalnum())

# str 문자에서 특정 문자/문자열로 시작하는지 검사 후 결과 반환 => startswith() 메소드
print("?????".startswith("??"))
print("?????".startswith("!"))

# str 문자에서 특정 문자/문자열로 끝나는지 검사 후 결과 반환 => endswith() 메소드
print("flower.jpg".endswith("jpg"))
print("flower.png".endswith("jpg"))
print("flower.txt".endswith(("jpg", "png", "txt")))

# str 특정 인덱스 문자를 변경해주는 메소드 => replace()
name = "HongGulDong"
# name[5] = 'i' ==> 인덱싱으로는 미지원 기능 ==> 메소드 제공
print(name.replace('u', 'i'))
print(name.replace('o', '*'))
print(name.replace('o', '*', 1))

