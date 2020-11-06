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
