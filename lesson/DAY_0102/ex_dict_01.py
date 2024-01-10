# [질문] 10명 학생에 대한 학점을 저장하기
# - 학생의 이름과 학점

# 방법1) 학생 이름 변수 5개 => stdName1 ~ stdName10
#       학점 변수 5개 => jumsu1 ~ jumsu10

# 방법2) 학생 이름 변수 5개 => stdNames = [학생 이름1, ...., 학생 이름2]
#       학점 변수 5개 => stdJumsus = [점수1, ...., 점수10]
stdNums = ['std01', 'std02', 'std03', 'std04', 'std05']
stdJumsus = [90, 89, 100, 76, 34]

# => 학번03번 학생의 학번과 점수를 출력하세요
idx = stdNums.index('std03')
print(f'{stdNums[idx]}학번의 점수 {stdJumsus[idx]}')

# 방법3)
stdnumsJumsu = [['std01', 90], ['std02', 89], ['std03', 100], ['std04', 76], ['std05', 34]]

# dict 자료형
# - 연관되어 있는 데이터를 하나로 묶어서 저장하는 방식 => 연관배열
# - 형태 => 키 : 데이터    (예: 주민번호:이름, 학번:전공)
# - 조건 => 키가 중복되면 안됨!
# - 문법 => { 키1:데이터, 키2:데이터, ... , 키n:데이터 }

stdnumsJumsu = {'std01':90, 'std02':89, 'std03':100, 'std04':76, 'std05':34}

print(f'stdnumJumsu : {len(stdnumsJumsu)}개, {type(stdnumsJumsu)}, {stdnumsJumsu}')

# 원소 읽는 방법 => 변수명[키]
print(f'stdnumsJumsu["std03"] => {stdnumsJumsu["std03"]}')