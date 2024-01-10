DEBUG_NUM = int(input("Choose your solution : "))

# 연습문제: 퍄일 경로에서 파일명만 가져오기
if DEBUG_NUM == 1:
   path = 'C:\\Users\\dojang\\AppData\\Local\\Programs\\Python\\Python36-32\\python.exe'
   path_split = path.split('\\')
   print(path_split[-1])

# 심사문제: 높은 가격순으로 출력하기
elif DEBUG_NUM == 2:
   str_list = list(map(int, input('').split(';')))

   str_list.sort()

   for i in str_list:
      output = ''
      i = str(i)
      mod = 0
      for j in range(len(i)-1, -1, -1):
         output = i[j] + output
         if mod == 2 and j != 0:
            output = ',' + output
            mod = 0
         else:
            mod += 1
      print(output)