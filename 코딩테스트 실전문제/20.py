# 감시 피하기
from itertools import combinations
n =int(input())
board =[]
teachers =[]
spaces =[]

for i in range(n):
    board.append(list(input().split()))
    for j in range(n):
        # 선생님이 존재하는 위치 저장
        if board[i][j] == 'T':
            teachers.append((i,j))
            # 장애물을 설치할 수 있는 위치 저장
            if board[i][j] == 'X':
                spaces.append((i,j))
                # 특정 방향으로 감시를 진행
def watch(x,y,direction):
    # 왼쪽 방향으로 감시
     if direction == 0:
         while y >= 0:
             if board[x][y] == 'S':
                 return True
             if board[x][y] == '0':
                 y -=1
     if direction == 1:
         while y < n :
             if board[x][y] == 'S':
                 return True
             if board[x][y] =='0':
                 return False
             y +=1
             if direction == 2:
                 while x >= 0:
                     if board[x][y] =='S':
                         return True
                     if board[x][y] == '0':
                         return False
                     x -=1
             if direction == 3:
                 while x < n:
                    if board[x][y] =='S':
                        return True
                    if board[x][y] == '0':
                        return False
                    x += 1
                    return False
# 장애물 설치 이후에 한명이라도 학생이 감지되는지 검사
def process():
    # 모든 선생님이 위치를 하니씩 확인
    for x,y in teachers:
        # 4가지 방향으로 학생을 감지할 수 있는지 확인
        for i in range(4):
            if watch(x,y,1):
                return True
            return False
find = False # 학생이 한명도 감지되지 않도록 설치할수 있는지의 여부

# 빈 공간에서 3개를 뽑는 모든 조합을 확인
for data in combinations(spaces,3):
    # 장애물 설치해보기
    for x,y in data:
        board[x][y] ='0'
        # 학생이 한명도 감지되지 않는 경우
        if not process():
            # 원하는 경우를 발견한 것
            find =True
            break
        # 설치된 장애물을 다시 없애기
        for x,y in data:
            board[x][y] ='X'
if find:
    print('YES')
else:
    print("No")
                

                      
                     
     
                 
                 