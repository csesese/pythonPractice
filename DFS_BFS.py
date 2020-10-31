
# 탐색 이란 남은 양의 데이터 중에서 원하는 데이터를 찾는 과정
'''
1)스택 자료 구조 :
    -선입후출(입구와 출구가 동일한 형태  ex. 박스 쌓기)
'''
stack =[]
stack.append(5)
stack.append(2)
stack.append(3)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack[::-1]) #최상단부터
print(stack) #최하단부터


'''
2) 큐 : 
    -선입선출(입구와 출구가 모두 뚫려 있는 터널과 같은 형태 ex. 은행창구)
'''
from collections import deque # 파이썬에 저장되어 있는 함수 사용

que = deque()
que.append(5)
que.append(2)
que.append(3)
que.append(7)
que.popleft()
que.append(1)
que.append(4)
que.popleft()

print(que) #먼저 들어온 순서대로 출력
que.reverse() #역순으로 바꾸기
print(que)


'''
3) 재귀함수 : 
    -자기 자신을 다시 호출하는 함수
'''
def recursive_function():
    print("재귀함수 호출")
    recursive_function()
recursive_function()


##종료 조건을 포함한 재귀함수
def recur_function(i):
    #100번째 호출을 했을 때 종료되도록 종료 조건 명시
    if i==100:
        return
    print(i,'번째 재귀함수에서',i+1,'번째 재귀함수를 호출합니다')
    recur_function(i+1)
    print(i,'번재 재귀함수를 종료합니다')
recur_function(1)

## 팩토리얼 구현 예제
def factorial(n):
    result=1
    for i in range(1,n+1):
        result=result*i
    return result

def recursive(n):
    if n<=1:
        return 1
    # n!= n* (n-1)!
    return n * recursive(n-1)

print('반복적으로 구현:',factorial(5))
print('재귀적으로 구현:',recursive(5))

'''
#최대공약수 계산(유클리드 호제법)
    - 두 자연수 A,B 에 대하여 (A>B) A를 B로 나눈 나머지를 R이라고 합시다
    -이때 A와B의 최대공약수는 B와R의 최대공약수와 같다.
'''
def gcd(a,b):
    if a%b==0:
        return b
    else:
        return gcd(b, a%b)

print(gcd(192,162))

'''
4) DFS:
    -깊이 우선 탐색 (깊은 부분을 우선적으로 탐색하는 알고리즘)
    -스택 자료구조 이용
'''

def dfs(graph , v, visted):
    #현재 노드를 방문 처리
    visted[v]=True
    print(v,end=' ')
    #현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visted[i]:
            dfs(graph,i,visted)

#각 노드가 연결된 정보를 표현
graph=[
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]

]
#각 노드가 방문된 정보를 표현(1차원 리스트)
visted=[False]*9

dfs(graph,1,visted)

'''
5)BFS :
    - 너비 우선 탐색 (가까운 노드부터 우선적으로 탐색하는 알고리즘)
    - 큐 자료구조 이용
'''

from collections import deque

def bfs(graph, start,visted):
    #큐 구현을 위해 deque 라이브러리 사용
    que=deque([start])
    #현재 노드를 방문 처리
    visted[start]=True
    #큐가 빌 때 까지 반복
    while que:
        # 큐에서 하나의 원소를 뽑아 출력하기
        v=que.popleft()
        print(v,end=' ')
        #아직 방문하지 않은 인접한 원소들을 큐에 삽입
        for i in graph[v]:
            if not visted[i]:
                que.append(i)
                visted[i]=True

#각 노드가 연결된 정보를 표현
graph=[
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]

]
#각 노드가 방문된 정보를 표현(1차원 리스트)
visted=[False]*9

bfs(graph,1,visted)
