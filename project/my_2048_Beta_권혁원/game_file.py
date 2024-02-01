import func_file as func
import save_file as save
from copy import deepcopy

FIRST_PLAY = True
FIRST_2048 = False

def playing(saved = None):
    global FIRST_PLAY
    if FIRST_PLAY == True :
        func.HowToPlay()
        FIRST_PLAY = False

    if saved == None:
        tiles = func.initGame()
        func.resetScore()

    else:
        tiles = deepcopy(saved)
    print('Game started. You can save game to enter \'save\'.')

    while True:                         # 게임 시작 : 루프 가동
        func.tilesGUI(tiles)
        if 2048 in tiles.values() and not FIRST_2048:       # 2048 달성 여부
            print("Wow, you make 2048!")
            print("But you can keep playing to make high score.")
            input("Enter ANY key to continue : ")
            FIRST_2048 = True

        print('Current score => ', func.getScore())         # 현재 점수 출력
        print('Enter direction to move tiles. (If you want to stop, press "Q" or "q")')     # 방향 입력
        enter = input('::: ')

        if enter == 'Q' or enter == 'q':  # 빡종
            print('Are you really want to quit? Your progress will be delete. ( Enter Y or y to quit )')
            enter = input('')
            if enter == 'Y' or enter == 'y':
                break
        elif enter.lower() == 'save':
            save.printLocal()
            save.saveLocal(tiles, func.getScore())
        else:
            origin = deepcopy(tiles)
            tiles = func.moveTiles(tiles, enter)            # 입력을 받아 타일을 움직임 : 함수 호출
            if tiles == origin:
                if func.checkFull(tiles) and func.checkMerge(tiles):       # 너 짐 ㅅㄱ
                    print('You can\'t move any tiles. You lose!')
                    print(f'Your score : {func.getScore()}')
                    func.updateScore()     # 점수 업데이트
                    input("Enter ANY key to continue : ")
                    break
                else:
                    continue
            else:
                tiles[func.randomTile(tiles)] = 2