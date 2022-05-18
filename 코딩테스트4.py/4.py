n, m = map(int, input().split())

# 캐릭터가 방문한 위치를 저장하기 위한 2차원 배열을 생성하여 0으로 초기화
d = [[0] * m for _ in range(n)]

# 현재 캐릭터의 X 좌표, Y 좌표, 방향
x, y, direction = map(int, input().split())

d[x][y] = 1  # 현재 좌표 방문 처리

# 전체 맵 정보를 입력받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향 벡터
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def turn_left():
	# 전역변수 direction 사용을 위한 global 키워드 사용
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


count = 1  # 이미 현재 좌표에 방문했으므로 count는 1부터 시작.
turn_time = 0

while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    # 회전한 이후 가보지 않은 칸인 경우 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        # 캐릭터 방문 위치 저장
        d[nx][ny] = 1
        # 캐릭터 좌표 이동
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue

    # 회전 이후 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1

    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        
        # 뒤로 갈 수 있는 경우
        if array[nx][ny] == 0:
            x = nx
            y = ny
            
        # 뒤가 바다로 다 막힌 경우
        else:
            break
        turn_time = 0

print(count)
