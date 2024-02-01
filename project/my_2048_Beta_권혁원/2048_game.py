import func_file as func
import game_file as game
import save_file as save

save.importFile()   # 데이터 파일 추출

while True:
    print("Welcome to 2048!!")
    print("What do you want to do?")
    func.printMenu()

    enter = input('')
    print()
    if enter == '1':        # 게임 시작
        game.playing()
    elif enter == '2':      # 저장본 불러오기
        while True:
            save.printLocal()
            save.loadsaveUI()
            answer = input()
            if answer == '1':
                loadfile = save.loadLocal()
                if loadfile == 'Canceled':      # 저장 데이터 없음
                    continue
                else:                           # 불러온 데이터로 게임 실행
                    print()
                    game.playing(saved=loadfile)
                    break
            elif answer == '2':                 # 데이터 삭제
                save.delLocal()
            elif answer == '3':                 # 메인메뉴로 돌아가기
                break
            else:                               # 뭐요
                continue
    elif enter == '3':      # 게임 설명
        func.HowToPlay()
    elif enter == '4':      # 점수표 출력
        g = ['st', 'nd', 'rd']
        print('------- Top 10 scoreboard -------')
        for grade, score in enumerate(func.getScoreboard(), 1):
            print(f' # {grade}', 'th' if grade > 3 else g[grade-1] ,f'grade : {score}', sep=' ')
        print('---------------------------------')
        input("Enter ANY key to continue : ")
        print()
    elif enter == '5':      # 빡종
        print("Are you really want to Quit? ( Enter Y or y to quit )")
        enter = input('')
        if enter == 'y' or enter == 'Y':
            break
    else:
        continue