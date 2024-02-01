import game_file as game
import func_file as func
import os.path
from copy import deepcopy
from datetime import datetime

local_data = {'1':None, '2':None, '3':None} # 로컬 세이브 데이터
savepath = os.getcwd() + '\\savefiles'      # 현재 디렉토리에 있는 저장 디렉토리 위치

def loadsaveUI():                           # 저장 및 불러오기 메뉴
    print('Choose number what to do')
    print('--------------------------------')
    print('1. Load data')
    print('2. Delete data')
    print('3. Back to main menu')
    print('--------------------------------')


def printLocal():                           # 로컬 데이터 출력
    print('  --- Local Data --- ')
    for k, v in local_data.items():
        print(f'Slot {k} :: ', end='')
        if v == None:
            print('No data detected')
            continue
        else:
            print(v[-1], 'Score :', v[1])
    print('=======================================')


def saveLocal(tiles, score):                # 데이터 저장
    while True:
        num = input('Choose number where to save data ( Enter Q or q to cancel ) : ')

        if num == 'Q' or num == 'q':        # 나가
            print()
            break
        elif num not in ('1', '2', '3'):    # 입력 오류
            print()
            print('You must enter available input.')
            print()
            continue
        else:                               # 데이터 저장
            date, time = str(datetime.now()).split()
            savetime = date + ' ' + time.split('.')[0]                 # 현재 시각 저장 : datetime 모듈
            local_data[num] = (deepcopy(tiles), func.getScore(), savetime)      # 저장 형식 = ( 게임판 딕셔너리, 점수, 저장시간 )
            exportFile(num, local_data[num])        # 파일 출력
            print('Data was successfully saved')
            input("Enter ANY key to continue : ")
            print()
            break


def loadLocal():                            # 데이터 로드
    while True:
        num = input('Choose number to load data ( Enter Q or q to cancel ) : ')

        if num == 'Q' or num == 'q':         # 나가
            print()
            return 'Canceled'
        elif num not in ('1', '2', '3'):     # 입력 오류
            print()
            print('You must enter available input.')
            print()
            continue
        else:
            if local_data[num] == None:     # 데이터 없을 시
                print('No data exist')
                input("Enter ANY key to continue : ")
                print()
                continue
            func.loadScore(local_data[num][1])  # 데이터 로딩
            return local_data[num][0]


def delLocal():                             # 데이터 삭제
    while True:
        num = input('Choose number what data to delete ( Enter Q or q to cancel ) : ')

        if num == 'Q' or num == 'q':        # 나가라고
            print()
            break
        elif num not in ('1', '2', '3'):    # 입력 오류
            print()
            print('You must enter available input.')
            print()
            continue
        else:                               # 삭제할거니?
            print()
            print('Do you really want to erase your data? Your data will be permanently lost.')
            answer = input('( Enter Y or y to commit ) ')
            if answer == 'Y' or answer == 'y':
                local_data[num] = None          # 로컬 데이터 삭제
                delFile(num)                    # 파일 삭제
                print('Data was successfully deleted.')
                input("Enter ANY key to continue : ")
                print()
                break


def importFile():                   # 파일 입력
    for slot in local_data.keys():  # 슬롯 별로 파일 입력
        importOne(slot)

    try:                            # 점수판 불러오기
        filename = savepath + '\\scoreboard.txt'
        f = open(filename, 'r')
    except FileNotFoundError:                                   # 점수 파일이 없다면...?
        print('Wait... WTF there is no scoreboard file!!!')     # 내 컴퓨터 누가 해킹했어
        exit(1)
    else:
        array = []
        while True:
            line = f.readline()
            if not line:
                break
            else:
                array.append(int(line[:-1]))

        func.importScoreboard(array)

        f.close()


def importOne(slot):                            # 파일 한개 저장
    try:                                        # 아니 왜 점점 길어지냐
        filepath = savepath + f'\\Slot{slot}.txt'
        f = open(filepath, 'r')
    except FileNotFoundError:
        pass
    else:
        score = 0
        loc_dict = {}
        while True:
            line = f.readline()
            if not line:
                break
            if line[0] == '(':
                loc, value = line.split(':')
                loc_dict[int(loc[1]), int(loc[-2])] = int(value)
            elif '-' in line:
                savetime = line[:-2]
            elif line[:-1].isdecimal():
                score = int(line[:-1])

        f.close()
        local_data[slot] = (loc_dict, score, savetime)


def exportFile(slot, localData):                 # 파일 출력
    # 게임 데이터 저장
    filename = savepath + f'\\Slot{slot}.txt'
    f = open(filename, 'w')
    for k, v in localData[0].items():
        table_info = str(k) + ':' + str(v) + '\n'
        f.write(table_info)
    f.write(str(localData[1]) + '\n')
    f.write(str(localData[2]) + '\n' )

    f.close()

    # 점수판도 저장
    filename = savepath + '\\scoreboard.txt'
    f = open(filename, 'w')                     # 이거까진 하지 말걸 그랬나
    scoreboard = func.getScoreboard()
    for score in scoreboard:
        f.write(str(score) + '\n')

    f.close()


def delFile(slot):              # 파일 삭제
    filepath = savepath + f'\\Slot{slot}.txt'

    if os.path.isfile(filepath):
        os.remove(filepath)