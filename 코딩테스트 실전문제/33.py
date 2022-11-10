n = int(input())
t =[]
p =[]
dp =[0] * (n+1)
max_value = 0

for _ in range(n):
    x,y=map(int,input().split())
    t.append(x)
    p.append(y)
    
for i in range(n-1,-1,-1):
    time = t[i] + i
        # 상담 기간안에 끝나는 경우
    if time <= n:
            # 점화식에 맞게, 현재까지의 최고 이익 계산
        dp[i] =max(p[i]+dp[time],max_value)
        max_value =dp[i]
    else:
        dp[i] =max_value
print(max_value)