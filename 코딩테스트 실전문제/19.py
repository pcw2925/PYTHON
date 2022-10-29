# 연산자 끼워넣기
n =int(input())

data =list(map(int,input().split()))
# 더하기 빼기 곱하기 나누기 연산자 개ㅜㅅ
add,sub,mul,div =map(int,input().split())

# 최솟값과 최댓값 초기화
min_value =1e9
max_value =-1e9

# 깊이우선 탐색 메서드
def dfs(i,now):
    global min_value,max_value,add,sub,mul,div
    # 모든 연산자를 다 사용한 경우 최솟값과 최댓값 업데이트
    if i == n:
        min_value =(min_value,now)
        max_value =(min_value,now)
    else:
        # 각 연산자에 대하여 재귀적으로 수행
        if add > 0:
           add -=1
           dfs(i+1,now+data[i])
           add +=1
        if sub > 0:
           sub -= 1
           dfs(i+1,now-data[i])
           sub +=1
        if mul > 0:
           mul -=1
           dfs(i+1,now*data[i])
           mul +=1
        if div > 0:
           div -=1
           dfs(i+1,int(now/data[i]))
           div +=1
            
# dfs 메서드 호출
dfs(1,data[0])

# 최댓값과 최솟값 차례대로 출력
print(max_value)
print(min_value)            
                
    