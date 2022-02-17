# n, k를 공백을 기준으로 입력 받기
n, k = map(int, input().split())

answer = 0

# n이 1이 되기 전까지 반복문을 돈다.
while n != 1:
  if k <= n:
    # 3. N이 K의 배수이면 N을 K로 나눈다.
    if n % k == 0:
      answer += 1
      n //= k
      
    else:
      # 2. N이 K보다 크거나 같고, N이 K의 배수가 아니면 N % K 만큼 빼고, 연산 횟수는 N % K만큼 더한다. 
      answer += (n % k)
      n -= (n % k)
  else:
    # 2. N이 K보다 작으면, N - 1 만큼 빼고, 연산 횟수는 N - 1만큼 더한다.
    answer += (n - 1)
    n = 1

# 연산을 수행하는 횟수의 최솟값 출력
print(answer)