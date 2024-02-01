from random import randint
from copy import deepcopy

scoreboard = []
score = 0

def initGame():        # 게임판 딕셔너리 생성 및 게임 시작
    row, col = 0, 0
    dict = {}

    while row < 4 and col < 4:
        dict[(row, col)] = 0

        if row >= 3:
            row = 0
            col += 1
        else:
            row += 1

    t1 = (randint(0, 3), randint(0, 3))
    t2 = (randint(0, 3), randint(0, 3))

    dict[t1] = 2
    dict[t2] = 2

    return dict


def printMenu():        # 메뉴 출력
    print("=======================================")
    print("1. Let's play!!")
    print("2. Load local data")
    print("3. How to play?")
    print("4. The scoreboard")
    print("5. Quit")
    print("=======================================")


def HowToPlay():        # 게임 방법 출력
    print('-----------------The rules----------------------')
    print('Press "W" or "w" to move your tiles to top.')
    print('Press "A" or "a" to move your tiles to left.')
    print('Press "S" or "s" to move your tiles to right.')
    print('Press "D" or "d" to move your tiles to bottom.')

    print()
    print('Your goal is make highest number as you can.')
    print('If all tiles are full and can\'t move tiles, you\'ll lose.')

    input("Enter ANY key to continue : ")


def tilesGUI(tiles):    # 게임판 출력
    row, col = 0, 0

    while row < 4 and col < 4:
        tile = tiles[row, col]
        if tile == 0:
            print('-----', end=' | ')
        else:
            print(f'{tiles[(row, col)]:^5}', end=' | ')

        if row >= 3:
            row = 0
            col += 1
            print('\n')
        else:
            row += 1


def randomTile(tiles):  # 타일 생성
    spawn = (randint(0, 3), randint(0, 3))
    while tiles[spawn] != 0:
        spawn = (randint(0, 3), randint(0, 3))

    return spawn


def moveTiles(tiles, direct):   # 타일 이동 후 게임판 반환
    if direct == 'W' or direct == 'w':      # 위로 이동
        for i in range(4):
            tiles = moveVertical((i, 1), tiles, -1)
        return tiles
    elif direct == 'A' or direct == 'a':    # 왼쪽 이동
        for i in range(4):
            tiles = moveHorizonal((1, i), tiles, -1)
        return tiles
    elif direct == 'S' or direct == 's':    # 아래로 이동
        for i in range(4):
            tiles = moveVertical((i, 2), tiles, 1)
        return tiles
    elif direct == 'D' or direct == 'd':    # 오른쪽 이동
        for i in range(4):
            tiles = moveHorizonal((2, i), tiles, 1)
        return tiles
    else:
        return tiles   # 이상한거 입력하면 그대로 반환


def moveVertical(tile, tiles, direct):                      # 위아래 타일 이동
    row, col = tile                                         # 아니 이거 좀 빡세네
    while col > -1 and col < 4:                             # 난 시간 복잡도 따윈 몰라
        tiles = moveVOne((row, col), tiles, direct)     # 내가 왜 이걸 하려고 했지
        col -= direct

    return tiles


def moveVOne(tile, tiles, direct):      # 더이상 최적화따윈 신경 안쓰겠다
    row, col = tile

    if checkVertical((row, col), tiles, direct):
        origin = tiles[(row, col)]
        tiles[(row, col + direct)] += tiles[(row, col)]
        tiles[(row, col)] = 0
        if origin != tiles[(row, col + direct)]:
            return tiles
        if col+direct != 0 and col+direct != 3:
            tiles = moveVOne((row, col+direct), tiles, direct)

    return tiles


def checkVertical(tile, tiles, direct):         # 위아래 한칸 이동 가능 여부
    row, col = tile
    if tiles[(row, col + direct)] == tiles[(row, col)]:
        global score
        score += tiles[(row, col)] * 2
    return tiles[(row, col+direct)] == 0 or tiles[(row, col+direct)] == tiles[(row, col)]


def moveHorizonal(tile, tiles, direct):                  # 양쪽 타일 이동
    row, col = tile
    while row > -1 and row < 4:
        tiles = moveHOne((row, col), tiles, direct)  # 집에 가고 싶다
        row -= direct

    return tiles


def moveHOne(tile, tiles, direct):
    row, col = tile

    if checkHorizonal((row, col), tiles, direct):
        origin = tiles[(row, col)]
        tiles[(row + direct, col)] += tiles[(row, col)]
        tiles[(row, col)] = 0
        if origin != tiles[(row + direct, col)]:
            return tiles
        if row+direct != 0 and row+direct != 3:
            tiles = moveHOne((row+direct, col), tiles, direct)

    return tiles


def checkHorizonal(tile, tiles, direct):         # 양옆 한칸 이동 가능 여부
    row, col = tile
    if tiles[(row + direct, col)] == tiles[(row, col)]:
        global score
        score += tiles[(row, col)] * 2
    return tiles[(row+direct, col)] == 0 or tiles[(row+direct, col)] == tiles[(row, col)]


def updateScore():         # 상위 점수 갱신
    global score, scoreboard
    scoreboard.append(score)
    scoreboard.sort(reverse=1)
    if len(scoreboard) > 10:
        scoreboard.pop()


def importScoreboard(array):
    global  scoreboard
    scoreboard = deepcopy(array)


def resetScore():           # 점수 초기화
    global score
    score = 0


def getScore():             # 점수 출력
    global score
    return score


def loadScore(save):
    global score
    score = save


def getScoreboard():         # 랭킹 불러오기
    global scoreboard
    return scoreboard


def checkFull(tiles):       # 게임판이 꽉찼는지 확인
    return 0 not in tiles.values()


def checkMerge(tiles):      # 더이상 움직일 구간이 있는지 확인
    locations = tiles.keys()
    for row, col in locations:
        if (row-1, col) in locations and tiles[(row-1, col)] == tiles[row, col]:
            return False
        elif (row, col-1) in locations and tiles[(row, col-1)] == tiles[row, col]:
            return False
        elif (row+1, col) in locations and tiles[(row+1, col)] == tiles[row, col]:
            return False
        elif (row, col+1) in locations and tiles[(row, col+1)] == tiles[row, col]:
            return False

    return True