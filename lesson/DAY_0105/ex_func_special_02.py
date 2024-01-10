# 다양한 함수의 형태 - 특별한 함수 (2)
# - 매개변수의 갯수를 유동적으로 가변으로 하는 함수
# - 키와 값의 덩어리 데이터
# - 형태 : def 함수명( **data ):
# - 가변 인자 함수
# - 매개변수 갯수 : 0개 ~ n개
# - 호출: 함수명(키1=값1)
#        함수명(키1=값1, 키2=값2, 키3=값3)
#        함수명()

def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(name='Kim', age=21, gender='F')

# 함수기능 : 회원 가입 기능
# 함수이름 : joinMember
# 매개변수 : 이름, 전화번호, 아이디, 이메일, 취미, 주소, 생일, ...
#          가변 + 데이터 정보 함께
#          키워드파라미터 **info
# 반환값  : '가입 완료 되었습니다.' str
def joinMember(**member):
    # print(type(member))
    # members.update(**member)
    members[f'M{len(members)+1}'] = member

# 함수 사용 즉 호출

# 가입된 회원들 저장 변수
members = {}
print(members)

# 회원가입 기능 함수 호출
joinMember(name='Hong', age=17, birth='2020/10/10')
joinMember(id='Hong84', phone='010-1111-2222', job='actor', blood='B')
joinMember(id='baby', birth='2024/01/01', blood='A')
print(members)
# m = {'name':'Hong', 'age':17}
# print(m.keys())
# print(m.values())
# print(m.items())

# 함수기능 : 회원 가입 기능
# 함수이름 : joinMember2
# 매개변수 : 필수 => id, pw
#          선택 => 이름, 전화번호, 이메일, 취미, 주소, 생일, ...
#          가변 + 데이터 정보 함께
#          키워드파라미터 **info
# 반환값  : '가입 완료 되었습니다.' str
members = {}

def joinMember2(id, pw, **option):
    op = {'id':id, 'pw':pw}
    op.update((option))
    members[f'M{len(members)+1}'] = op

joinMember2(id='ha', pw='123')
joinMember2(id='Hong84', pw='012345678', job='actor', blood='B')
print(members)

# 함수기능 : 회원 가입 기능
# 함수이름 : joinMember3
# 매개변수 : 필수 => id, pw, loc, gender
#          선택 => 이름, 전화번호, 이메일, 취미, 생일, ...
#          가변 + 데이터 정보 함께
#          키워드파라미터 **info
# 반환값  : '가입 완료 되었습니다.' str
members = {}

def joinMember3(id, pw, loc='내국인', gender='남자', **option):
    op = {'id': id, 'pw': pw, 'loc':loc, 'gender':gender}
    op.update((option))
    members[f'M{len(members) + 1}'] = op

joinMember3(id='Hong84', pw='1234')
joinMember3(id='Hong1', pw='123', gender='여자')
print(members)

def testPrinth(*a, **kw):
    print(*a, **kw)