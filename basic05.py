#<그리디 알고리즘>
'''
그리디 알고리즘 : 현재 상황에서 지금 당장 좋은 것만 고르는 방법(정당성 분석이 중요)

'''

# <문제1> 거스름돈 - 가장 큰 화폐 단위부터 계산

n = 1260  #거스름돈
count = 0
array = [500, 100, 50, 10]

for coin in array:
    count += n // coin  # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    n %= coin

print(count)

#<문제2> 1이 될때까지 - 가능하면 최대한 많이 나누는 작업
#   1. N에서 1을 뺍니다.
#   2. N을 K로 나눕니다.

#N,K 공백을 기준으로 구분하여 입력 받기
n, k = map(int, input().split())

nmg = 0

while True:
    # N이 K로 나누어 떨어지는 수가 될때까지만 1씩 빼기
    target = (n // k) * k
    nmg += (n - target)
    n = nmg
    # N이 K보다 작을 때 반복물 탈출
    if n < k:
        break
    #K로 나누기
    nmg += 1
    n // k

#마지막으로 남은 수 에 대하여 1씩 빼기
nmg += (n - 1)
print(nmg)

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

##########################################

#<구현>
'''
구현 :
-알고리즘은 간단한데 코드가 지나칠 만큼 길어지는 문제
-실수 연산을 다루고,특정 소수점 자리까지 출력해야 하는 문제
-문자열을 특정한 기준에 따라서 끊어 처리해야 하는 문제
-적절한 라이브러리를 찾아서 사용해야 하는 문제 

일바적으로 알고리즘 문제에서의 2차원 공간은 행렬의 의미로 사용됩니다. 
'''

#<문제4> 시각 문제 - 가능한 모든 시간의 경우를 하나씩 모드 세서 푼다
# 하루는 86,400 초 , 따라서 단순히 시각을 1씩 증가시키녀서 3이 하나라도 포함되어 있느지를 확인하면 된다(완전 탐색)

# H 입력 받기
h = int(input())

count = 0
for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            #매 시각 안에 '3' 이 포함되어 있다면 카운트 증가
            if '3' in str(i) + str(j) + str(k):
                count += 1
print(count)

#<문제5> 상화좌우 - 시뮬레이션 유형

n = int(input())
x, y = 1, 1

plans = input().split()

# L, R,U,D 에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

#이동 계획을 하나씩 확인하기
for plan in plans:
    #이동 후 좌표 구학
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
        #공간을 벗어나는 경우 무시
        if nx < 1 or ny < 1 or nx > n or ny > n:
            continue
        #이동 수행
        x, y = nx, ny

print(x, y)

#<문제6> 문자열 재정렬

data = input()
result = []
value = 0

#문자를 하나씩 확인하며
for x in data:
    #알파벳인 경우 결과 리스트 삽입
    if x.isalpha():
        result.append(x)
    #숫자는 따로 더하기
    else:
        value += int(x)

#알파벳을 오름차순으로 정렬
result.sort()

#숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
if value != 0:
    result.append(str(value))

#최종 결과 출력(리스트를 문자열로 반환하여 출력)
print(''.join(result))
