
# [실습 1] 단어를 입력 받은 후 아래 코드를 작성하세요.
# - 입력 받은 단어가 알파벳으로만 구성되어 있는지 검사
# - 입력 받은 단어가 숫자로만 구성되어 있는지 검사
# - 입력 받은 단어가 모두 대문자로 구성되어 있는지 검사
# - 입력 받은 단어가 모두 소문자로 구성되어 있는지 검사
word = input("단어를 입력 : ")
print('문자들인가? ', word.isalpha())
print('숫자들인가? ', word.isdecimal())
print('숫자들인가? ', word.isnumeric())
print('숫자들인가? ', word.isdigit())
print('대문자들인가? ', word.isupper())
print('소문자들인가? ', word.islower())

# [실습 2] 파일명을 입력 받은 후 아래 코드를 작성하세요. => str 전용 함수인 메소드 활용
# - 입력 받은 파일이 text 파일인지 검사
# - 입력 받은 파일이 jpg 파일인지 검사
# - 입력 받은 파일이 py 파일인지 검사
filename = input("파일명 : ")
print('text 파일 여부 : ', filename.endswith('.text'))
print('jpg 파일 여부  : ', filename.endswith('.jpg'))
print('py 파일 여부   : ', filename.endswith('.py'))