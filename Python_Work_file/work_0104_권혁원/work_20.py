DEBUG_NUM = int(input("Choose your solution : "))

# 연습문제: 2와 11의 배수, 공배수 처리하기
if DEBUG_NUM == 1:
    for i in range(1, 100):
        if not i % 2 and not i%11:
            print('FizzBuzz')
        elif not i % 11:
            print('Buzz')
        elif not i%2:
            print('Fizz')
        else:
            print(i)


# 심사문제: 5와 7의 배수, 공배수 처리하기
elif DEBUG_NUM == 2:
    nums = input("").split()

    if len(nums) != 2:
        print("You MUST enter exactly 'two' numbers!!")
    elif not (nums[0].isdecimal() and nums[1].isdecimal()):
        print("Input data MUST be integer type!!")
    elif nums[0] >= nums[1]:
        print("First number MUST be smaller than second one!!")
    else:
        x, y = map(int, tuple(nums))
        for i in range(x, y+1):
            if not i % 5 and not i % 7:
                print('FizzBuzz')
            elif not i % 7:
                print('Buzz')
            elif not i % 5:
                print('Fizz')
            else:
                print(i)