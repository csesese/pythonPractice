#<문제> 음료수 얼려 먹기(dfs 사용)

#dfs로 특정 노드를 방문하고 연결된 모든 노드들도 방물
def dfs(x,y):
    #주어진 범위를 벗어나는 경우에는 즉시 종료
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False
    #해당 노드를 아직 방문하지 않았다면
    if graph[x][y] ==0:
        #해당 방문 노드를 방문 처리
        graph[x][y]=1
        #상.하,좌,우의 위치들도 모두 재귀적으로 호출
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False



#n,m 을 입력 받기
n,m = map(int,input().split())

#2차원 리스트의 맵 정보 입력 받기
graph=[]
for i in range(n):
    graph.append(list(map(int,input())))

#모든 노드에 대하여 음료수 채우기
result=0
for i in range(n):
    for j in range(m):
        #현재 위치에서 dfs 수행
     if dfs(i,j) ==Tre:
         result+=1

print(result)

####################

#<문제> 미로탈출(bfs 사용)
from collections import deque
#bfs 소스코드 구현
def bfs(x,y):
    #큐 구현을 위해 deque라이브러리 사용
    que=deque()
    que.append((x,y))
    #쿠가 빌 때까지 반복
    while que:
        x,y=que.popleft()
        #현재 위치에서 4가지 방향으로 위치 학인
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            #미로 찾기 공간을 벗어난 경우 무시
            if(nx<0 or nx>=n or ny<0 or ny>=m):
                continue
            #벽인 경우 무시
            if graph[nx][ny]==0:
               continue
            if graph[nx][ny]==1:
                graph[nx][ny]=graph[x][y]+1
                que.append((nx,ny))
    #가장 오른쪽 아래까지의 최단거리 반환
    return graph[n-1][m-1]
n,m = map(int,input().split())

graph=[]
for i in range(n):
    graph.append(list(map(int,input())))

#이동할 네가지 방향 정의
dx=[-1,1,0,0]
dy=[0,0,-1,1]

print(bfs(0,0))

