# # N 입력 받기
# n = int(input())
# x, y = 1, 1
# plans = input().split()

# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]
# move_types = ['L', 'R', 'U', 'D']

# # 이동 계획을 하나씩 확인하기
# for plan in plans:
#   # 이동 후 좌표 구하기
#   for i in range(len(move_types)):
#     nx = x + dx[i]
#     ny = y + dy[i]
  
#   # 공간을 벗어나는 경우 무시
#   if nx < 1 or ny < 1 or nx > n or ny > n:
#     continue
#   x, y = nx, ny

# print(x, y)

n = 3
m = 3
array = [[0] * m for _ in range(n)]  # 리스트 컴프리 헨션을 이용한 2차원 배열 초기화

# 방향 벡터 이용
dx = [0, -1, 0, 1]  # 행, row
dy = [1, 0, -1, 0]  # 열, column

x, y = 1, 1  # 3 X 3 크기의 2차원 배열에서 1, 1을 기준으로 우, 상, 좌, 하에 순서대로 값을 넣습니다.

cnt = 1  # 들어갈 값

for i in range(4):
    array[x + dx[i]][y + dy[i]] = cnt
    print(f"{cnt} 넣을 위치는 {x + dx[i] + 1}행 {y + dy[i] + 1}열 입니다.")

    cnt += 1

for i in array:
    for j in i:
        print(j, end=' ')  
    print()