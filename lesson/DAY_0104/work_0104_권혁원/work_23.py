DEBUG_NUM = int(input("Choose your solution : "))

# 연습문제: 3차원 리스트 만들기
if DEBUG_NUM == 1:
    a = [[[0 for col in range(3)] for row in range(4)] for depth in range(2)]

    print(a)

# 심사문제: 지뢰찾기
# X친 지뢰새X
elif DEBUG_NUM == 2:
    # 입력 판별 아직 안함
    # 행과 열의 개수 입력
    col, row = map(int, input('').split())

    # 행렬 구조 입력
    matrix = []
    for i in range(row):
        matrix.append(input(''))

    mine_dict = {}  # 각 좌표에 대한 공간 정보
    c, r = 0, 0
    while c < col and r < row:
        mine_dict[(c, r)] = []

        # 공간 정보 딕셔너리에 좌표 추가
        if c != 0:  # 좌표가 왼쪽 끝인지 판별
            mine_dict[(c, r)].append((c-1, r))
        if r != 0:  # 좌표가 위쪽 끝인지 판별
            mine_dict[(c, r)].append((c, r-1))
        if c != col-1:  # 좌표가 오른쪽 끝인지 판별
            mine_dict[(c, r)].append((c+1, r))
        if r != row-1:  # 좌표가 아래쪽 끝인지 판별
            mine_dict[(c, r)].append((c, r+1))
        if c != 0 and r != 0:  # 좌표가 좌상단 끝인지 판별
            mine_dict[(c, r)].append((c-1, r-1))
        if c != 0 and r != row-1:  # 좌표가 좌하단 끝인지 판별
            mine_dict[(c, r)].append((c-1, r+1))
        if c != col-1 and r != 0:  # 좌표가 우상단 끝인지 판별
            mine_dict[(c, r)].append((c+1, r-1))
        if c != col-1 and r != row-1:  # 좌표가 우하단 끝인지 판별
            mine_dict[(c, r)].append((c+1, r+1))

        # 지뢰 수 판별
        if matrix[r][c] == '.':
            mines = 0
            for x, y in mine_dict[(c, r)]:
                if matrix[y][x] == '*':
                    mines += 1
            matrix[r] = matrix[r][:c] + str(mines) + matrix[r][c+1:]

        # 다음 좌표 판별
        if c < col-1:
            c += 1
        else:
            c = 0
            r += 1

    for i in matrix:
        print(i)
