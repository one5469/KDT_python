# 내장함수 zip()
x = [1,2,3,4,5]
y = [11,22,33,44,55]
z = [111,222,333,444,555]

result = zip(x, y, z)
result2 = zip(x, y, z)
print(f'result  => {type(result)}')
print(f'result2 => {tuple(result2)}')
print(f'result2 => {(result2)}')