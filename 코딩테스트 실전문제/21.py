from collections import deque

# 땅의 크기 n,l,r 값 입력받기
n,l,r =map(int,input().split())

# 전체 나라의 정보를 입력받기
graph =[]
for _ in range(n):
    graph.append(list(map(int,input().split())))
    
dx =[-1,0,1,0]
dy =[0,-1,0,1]

result =0
# 특정 위치에서 출발하여 모든 연합을 체크한 뒤에 데이터 갱신

def process(x,y,index):
    #(x,y) 의 위치와 연결된 나라 정보를 담는 리스트
    united =[]
    united.append((x,y))
    # 너비우선 탐색을 위한 큐 자료구조 정의
    q =deque()
    q.append((x,y))
    Union[x][y] =index # 현재 연합의 번호 할당
    summary =graph[x][y]
    count =1
    # 큐가 빌때 까지 반복
    while q:
        x,y=q.popleft()
        # 현재 위치에서 4가지 방향을 확인하며
        for i in range(4):
            nx =x+ dx[i]
            ny =x+ dy[i]
            # 바로 옆에 있는 나라를 확인하여
            if 0 <= nx < n and 0 <= ny < n and Union[nx][ny] == -1:
                # 옆에 있는 나라와 인구 차이가 L명 이상 R명 이하라면
                if l <= abs(graph[nx][ny] -graph[x][y]) <=r:
                    q.append((nx,ny))
                    # 연합에 추가
                    Union[nx][ny] =index
                    summary += graph[nx][ny]
                    count +=1
                    united.append((nx,ny))
                # 연합 국가끼리 인구를 분배
    for i,j in united:
         graph[i][j] =summary // count
    return count
total_count =0
# 더이상 인구 이동을 할 수 없을때 까지 반복
while True:
    Union =[[-1] *n for _ in range(n)]
    index =0
    for i in range(n):
        for j in range(n):
            if Union[i][j] == -1:
                process(i,j,index)
                index +=1
                # 모든 인구 이동이 끝난 경우
                if index == n* n:
                    break
                total_count +=1
        print(total_count)
                