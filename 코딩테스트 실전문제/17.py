# 경쟁적 전염
from collections import deque
n,k =map(int,input().split())

graph=[]
data =[]

for i in range(n):
    # 보드 정보를 한줄로 입력
    graph.append(list(map(int,input().split())))
    for j in range(n):
        # 해당위치에 바이러스가 존재하는 경우
        if graph[i][j] !=0:
            # 바이러스 종류 시간 위치x 위치y 삽입
            data.append((graph[i][j],0,i,j))
# 정렬 이후에 큐로 옮기기
data.sort()
q =deque(data)

target_s,target_x,target_y =map(int,input().split())

# 바이러스가 퍼져나갈수 있는 4가지 위치
dx =[-1,0,1,0]
dy =[0,1,0,-1]

# 너비우선 탐색 진행
while q:
    virus,s,x,y=q.popleft()
    # 정확히 s초가 지나거나 큐가 빌때까지 반복
    if s == target_s:
        break
# 현재 노드에서 주변 4가지 위치를 각각 확인
for i in range(4):
    nx =x +dx[i]
    ny =y +dy[i]
    # 해당 위치를 이동할수 있는 경우
    if 0 <=nx and nx < n and 0<= ny and ny < n:
        # 아직 방문하지 않은 위치라면 그 위치에 바이러스 넣기
        if graph[nx][ny] == 0:
            graph[nx][ny] =virus
            q.append((virus,s+1,nx,ny))

print(graph[target_x-1][target_y-1])

            