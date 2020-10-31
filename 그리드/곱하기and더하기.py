#<문제3> 곱하기 혹은 더하기 - 가장 큰수 만들기
# 두 수에 대하여 연산을 수행할 때, 두수중에서 하나라도 1 이하인 경우에는 더하며 두 수가 모두 2 이상인 경우에는 곱하면 된다

data = input()

result = int(data[0])

for i in range(1, len(data)):
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num
print(result)
